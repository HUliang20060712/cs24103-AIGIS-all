package cn.edu.chzu.aigis.reco.dao;

import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Map;

@Repository
public class ItemDao {

    private final JdbcTemplate jdbc;

    public ItemDao(JdbcTemplate jdbc) {
        this.jdbc = jdbc;
    }

    public List<Map<String, Object>> byCategory(List<String> categories, int limit) {
        if (categories == null || categories.isEmpty()) {
            return List.of();
        }
        String placeholders = String.join(",", categories.stream().map(c -> "?").toList());
        Object[] args = new Object[categories.size() + 1];
        for (int i = 0; i < categories.size(); i++) {
            args[i] = categories.get(i);
        }
        args[categories.size()] = limit;
        return jdbc.queryForList(
                "select item_id, name, category from item_meta where category in ("
                        + placeholders + ") order by item_id limit ?", args);
    }

    public List<Map<String, Object>> hot(String category, int limit) {
        return jdbc.queryForList(
                "select i.item_id, i.name, i.category, h.score "
                        + "from hot_rank h join item_meta i on i.item_id = h.item_id "
                        + "where h.category = ? and h.stat_date = current_date "
                        + "order by h.score desc limit ?",
                category, limit);
    }

    public int count() {
        Integer n = jdbc.queryForObject("select count(*) from item_meta", Integer.class);
        return n == null ? 0 : n;
    }
}
