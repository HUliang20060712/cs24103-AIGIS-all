package cn.edu.chzu.aigis.reco.service;

import cn.edu.chzu.aigis.reco.config.RecoProperties;
import cn.edu.chzu.aigis.reco.dao.ItemDao;
import cn.edu.chzu.aigis.reco.model.RecoItem;
import cn.edu.chzu.aigis.reco.model.UserPreference;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Service;

import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * 推荐主流程：偏好 -> 候选 -> 混合打分 -> Top-N。
 * Redis 不可用时直接查库并跳过缓存，不向前端返回 5xx。
 */
@Service
public class RecommendationService {

    private static final String CACHE_KEY = "reco:feed:%d:%d:%d";

    private final ItemDao itemDao;
    private final PreferenceService preferenceService;
    private final RecoProperties props;
    private final StringRedisTemplate redis;

    public RecommendationService(ItemDao itemDao,
                                 PreferenceService preferenceService,
                                 RecoProperties props,
                                 StringRedisTemplate redis) {
        this.itemDao = itemDao;
        this.preferenceService = preferenceService;
        this.props = props;
        this.redis = redis;
    }

    public List<RecoItem> feed(long userId, int page, int size) {
        String key = CACHE_KEY.formatted(userId, page, size);
        try {
            String cached = redis.opsForValue().get(key);
            if (cached != null && !cached.isBlank()) {
                return decode(cached);
            }
        } catch (RuntimeException ignored) {
            // 缓存不可用，走数据库
        }

        UserPreference pref = preferenceService.find(userId).orElse(null);
        List<RecoItem> items = rank(pref, page, size);

        try {
            redis.opsForValue().set(key, encode(items), Duration.ofSeconds(props.cacheTtlSeconds()));
        } catch (RuntimeException ignored) {
            // 写缓存失败不影响主流程
        }
        return items;
    }

    private List<RecoItem> rank(UserPreference pref, int page, int size) {
        int need = page * size;
        List<String> categories = pref == null
                ? List.of("水体", "植被", "建筑")
                : pref.categories();
        List<Map<String, Object>> candidates = itemDao.byCategory(categories, need);
        if (candidates.isEmpty()) {
            return coldStart(size);
        }

        double weight = pref == null ? 0.5 : pref.weight();
        List<RecoItem> ranked = new ArrayList<>(candidates.size());
        for (Map<String, Object> row : candidates) {
            long itemId = ((Number) row.get("item_id")).longValue();
            String name = String.valueOf(row.get("name"));
            String category = String.valueOf(row.get("category"));
            double cf = Math.min(1.0, 0.35 + 0.05 * categories.indexOf(category));
            double score = props.cfWeight() * cf + props.contentWeight() * weight;
            ranked.add(new RecoItem(itemId, name, category, round(score),
                    new RecoItem.RecoReason(pref == null ? "hot" : "cf",
                            pref == null ? "按类别热度推荐" : "与你偏好的" + category + "相近")));
        }
        ranked.sort((a, b) -> Double.compare(b.score(), a.score()));

        int from = Math.min((page - 1) * size, ranked.size());
        int to = Math.min(need, ranked.size());
        return ranked.subList(from, to);
    }

    private List<RecoItem> coldStart(int size) {
        List<RecoItem> hot = new ArrayList<>();
        for (Map<String, Object> row : itemDao.hot("水体", Math.min(size, props.hotFallbackSize()))) {
            long itemId = ((Number) row.get("item_id")).longValue();
            hot.add(new RecoItem(itemId, String.valueOf(row.get("name")),
                    String.valueOf(row.get("category")),
                    round(((Number) row.get("score")).doubleValue()),
                    new RecoItem.RecoReason("hot", "热门榜兜底")));
        }
        return hot;
    }

    private static double round(double v) {
        return Math.round(v * 1000.0) / 1000.0;
    }

    private static String encode(List<RecoItem> items) {
        StringBuilder sb = new StringBuilder();
        for (RecoItem it : items) {
            sb.append(it.itemId()).append('|').append(it.name()).append('|')
                    .append(it.category()).append('|').append(it.score()).append('|')
                    .append(it.reason().type()).append('|').append(it.reason().text()).append('\n');
        }
        return sb.toString();
    }

    private static List<RecoItem> decode(String cached) {
        List<RecoItem> list = new ArrayList<>();
        for (String line : cached.split("\n")) {
            if (line.isBlank()) {
                continue;
            }
            String[] p = line.split("\\|", 6);
            list.add(new RecoItem(Long.parseLong(p[0]), p[1], p[2], Double.parseDouble(p[3]),
                    new RecoItem.RecoReason(p[4], p[5])));
        }
        return list;
    }
}
