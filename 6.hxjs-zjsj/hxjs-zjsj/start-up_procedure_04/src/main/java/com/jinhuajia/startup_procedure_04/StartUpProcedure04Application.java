package com.jinhuajia.startup_procedure_04;

import com.jinhuajia.startup_procedure_04.exception.JavaStackException;
import com.jinhuajia.startup_procedure_04.listenner.JavastackListenner;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
@Slf4j
public class StartUpProcedure04Application {

    public static void main(String[] args) {
//        new SpringApplicationBuilder()
//                .sources(StartUpProcedure04Application.class)
//                .child(StartUpProcedure04Application.class)
//                .run(args);

        SpringApplication springApplication = new SpringApplication(StartUpProcedure04Application.class);
        springApplication.setLogStartupInfo(false);
        springApplication.run(args);
        springApplication.addListeners(new JavastackListenner());
        log.info("启动成功！");
    }

    @Bean
    public CommandLineRunner commandLineRunner() {
        return args -> {
            log.info("commandLineRunner...");
            throw new JavaStackException("commandLineRunner");
        };
    }

}
