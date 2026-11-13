package cn.edu.chzu.aigis.reco.controller;

import cn.edu.chzu.aigis.reco.model.RecoItem;
import cn.edu.chzu.aigis.reco.service.RecommendationService;
import org.springframework.http.ResponseEntity;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/reco")
public class RecoController {

    private final RecommendationService service;
    private final JdbcTemplate jdbc;

    public RecoController(RecommendationService service, JdbcTemplate jdbc) {
        this.service = service;
        this.jdbc = jdbc;
    }

    @GetMapping("/feed")
    public Map<String, Object> feed(@RequestParam long userId,
                                    @RequestParam(defaultValue = "1") int page,
                                    @RequestParam(defaultValue = "10") int size) {
        List<RecoItem> list = service.feed(userId, page, Math.min(size, 50));
        return Map.of("page", page, "size", size, "total", list.size(), "list", list);
    }

    @PostMapping("/feedback")
    public ResponseEntity<Void> feedback(@RequestBody FeedbackRequest req) {
        jdbc.update("insert into feedback (user_id, item_id, action) values (?, ?, ?)",
                req.userId(), req.itemId(), req.action());
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/items/{itemId}/similar")
    public List<RecoItem> similar(@PathVariable long itemId,
                                  @RequestParam(defaultValue = "6") int limit) {
        return jdbc.query(
                "select i.item_id, i.name, i.category from item_meta i "
                        + "where i.category = (select category from item_meta where item_id = ?) "
                        + "and i.item_id <> ? order by i.item_id limit ?",
                (rs, n) -> new RecoItem(rs.getLong(1), rs.getString(2), rs.getString(3), 0.5,
                        new RecoItem.RecoReason("content", "同类地物")),
                itemId, itemId, Math.min(limit, 20));
    }

    public record FeedbackRequest(long userId, long itemId, String action) {
    }
}
