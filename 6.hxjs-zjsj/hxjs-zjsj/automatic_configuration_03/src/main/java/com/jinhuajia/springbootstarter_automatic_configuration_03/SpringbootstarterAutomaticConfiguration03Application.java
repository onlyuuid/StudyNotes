package com.jinhuajia.springbootstarter_automatic_configuration_03;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;

@SpringBootApplication
public class SpringbootstarterAutomaticConfiguration03Application {

    public static void main(String[] args) {
        SpringApplication.run(SpringbootstarterAutomaticConfiguration03Application.class, args);
    }
}
