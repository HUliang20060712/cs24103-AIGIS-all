package cn.edu.chzu.aigis.reco;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class ScoreFusionTest {

    private double fuse(double cf, double content, double wCf, double wContent) {
        return Math.round((wCf * cf + wContent * content) * 1000.0) / 1000.0;
    }

    @Test
    void weightsShouldSumToOne() {
        assertEquals(1.0, 0.6 + 0.4, 1e-9);
    }

    @Test
    void fusionStaysInRange() {
        assertEquals(0.88, fuse(0.8, 1.0, 0.6, 0.4), 1e-9);
    }

    @Test
    void zeroScoresStayZero() {
        assertEquals(0.0, fuse(0, 0, 0.6, 0.4), 1e-9);
    }
}
