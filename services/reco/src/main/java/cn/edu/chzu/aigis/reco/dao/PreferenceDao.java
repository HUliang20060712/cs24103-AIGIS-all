package cn.edu.chzu.aigis.reco.dao;

import cn.edu.chzu.aigis.reco.model.UserPreference;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Repository;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

@Repository
public class PreferenceDao {

    private final JdbcTemplate jdbc;

    public PreferenceDao(JdbcTemplate jdbc) {
        this.jdbc = jdbc;
    }

    public Optional<UserPreference> find(long userId) {
        List<UserPreference> rows = jdbc.query(
                "select user_id, categories, weight from preference where user_id = ?",
                (rs, i) -> new UserPreference(
                        rs.getLong("user_id"),
                        Arrays.asList(rs.getString("categories").split(",")),
                        rs.getDouble("weight")),
                userId);
        return rows.stream().findFirst();
    }

    public void upsert(long userId, List<String> categories, double weight) {
        jdbc.update(
                "insert into preference (user_id, categories, weight, updated_at) values (?, ?, ?, now()) "
                        + "on conflict (user_id) do update set categories = excluded.categories, "
                        + "weight = excluded.weight, updated_at = now()",
                userId, String.join(",", categories), weight);
    }

    public void delete(long userId) {
        jdbc.update("delete from preference where user_id = ?", userId);
    }
}
