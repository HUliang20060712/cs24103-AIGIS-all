package cn.edu.chzu.aigis.reco.config;

import org.springframework.boot.context.properties.ConfigurationProperties;

@ConfigurationProperties(prefix = "reco")
public record RecoProperties(
        double cfWeight,
        double contentWeight,
        int cacheTtlSeconds,
        int hotFallbackSize
) {
}
