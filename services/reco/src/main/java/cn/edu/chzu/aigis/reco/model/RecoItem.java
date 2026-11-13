package cn.edu.chzu.aigis.reco.model;

public record RecoItem(long itemId, String name, String category, double score, RecoReason reason) {

    public record RecoReason(String type, String text) {
    }
}
