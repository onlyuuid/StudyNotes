package com.example.javastack_spring_boot_starter_sample;
import cn.javastack.springboot.starter.service.TestService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@Slf4j
@SpringBootApplication
public class JavastackSpringBootStarterSampleApplication {

	public static void main(String[] args) {
		SpringApplication.run(JavastackSpringBootStarterSampleApplication.class, args);
	}

	@Bean
	public CommandLineRunner commandLineRunner(TestService testService) {
		return args -> {
			log.info(testService.getServiceName());
		};
	}
}
