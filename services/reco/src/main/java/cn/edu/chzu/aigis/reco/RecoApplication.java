package cn.edu.chzu.aigis.reco;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.ConfigurationPropertiesScan;

@SpringBootApplication
@ConfigurationPropertiesScan
public class RecoApplication {

    public static void main(String[] args) {
        SpringApplication.run(RecoApplication.class, args);
    }
}
