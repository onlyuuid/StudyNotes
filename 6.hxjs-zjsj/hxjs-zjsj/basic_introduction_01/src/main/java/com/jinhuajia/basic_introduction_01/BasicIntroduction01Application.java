package com.jinhuajia.basic_introduction_01;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@RestController
public class BasicIntroduction01Application {

    public static void main(String[] args) {
        SpringApplication.run(BasicIntroduction01Application.class, args);
    }

    @GetMapping("/")
    public String hello() {
        return "Hello World!";
    }

}
