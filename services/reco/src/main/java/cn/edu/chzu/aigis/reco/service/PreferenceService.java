package cn.edu.chzu.aigis.reco.service;

import cn.edu.chzu.aigis.reco.dao.PreferenceDao;
import cn.edu.chzu.aigis.reco.model.UserPreference;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class PreferenceService {

    private final PreferenceDao dao;

    public PreferenceService(PreferenceDao dao) {
        this.dao = dao;
    }

    public Optional<UserPreference> find(long userId) {
        return dao.find(userId);
    }

    public void save(long userId, List<String> categories, double weight) {
        dao.upsert(userId, categories, weight);
    }

    public void clear(long userId) {
        dao.delete(userId);
    }
}
