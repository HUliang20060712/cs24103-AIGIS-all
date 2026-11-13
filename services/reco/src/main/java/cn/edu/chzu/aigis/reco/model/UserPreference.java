package cn.edu.chzu.aigis.reco.model;

import java.util.List;

public record UserPreference(long userId, List<String> categories, double weight) {
}
