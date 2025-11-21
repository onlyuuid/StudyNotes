package com.jinhuajia.configuration_management_02;

import com.jinhuajia.configuration_management_02.properties.JavaStackProperties;
import com.jinhuajia.configuration_management_02.properties.NumberProperties;
import com.jinhuajia.configuration_management_02.properties.OtherMember;
import com.jinhuajia.configuration_management_02.properties.UserProperties;
//import com.jinhuajia.configuration_management_02.properties.NumberProperties;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.ConfigurationPropertiesScan;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
//@EnableConfigurationProperties(value = {UserProperties.class, NumberProperties.class})
@ConfigurationPropertiesScan
@RequiredArgsConstructor
@Slf4j
public class ConfigurationManagement02Application {

    private final UserProperties userProperties;

    private final NumberProperties numberProperties;

    private final OtherMember otherMember;

    private final JavaStackProperties javaStackProperties;

    @Value("${javastack.username}")
    private String username;

    @Value("${javastack.password}")
    private String password;

    @Bean
    public CommandLineRunner commandLineRunner(){
        return args -> {
            log.info("userProperties:{}", userProperties);
            log.info("numberProperties:{}", numberProperties);
            log.info("otherMember:{}", otherMember);
            log.info("javaStackProperties:{}", javaStackProperties);
            log.info("username:{},password:{}", username, password);

        };
    }



    public static void main(String[] args) {
        SpringApplication.run(ConfigurationManagement02Application.class, args);

    }
}
