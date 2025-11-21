package com.jinhuajia.log_management;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.ansi.AnsiOutput;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class LogManagementApplication {

	public static void main(String[] args) {
		System.setProperty("LOG_PATH","./logs");
		System.setProperty("LOGBACK_ROLLINGPOLICY_MAX_FILE_SIZE","1KB");
		SpringApplication.run(LogManagementApplication.class, args);
	}

	private static final org.apache.commons.logging.Log logger =
			org.apache.commons.logging.LogFactory.getLog(LogManagementApplication.class);

	private static final org.slf4j.Logger logger2 =
			org.slf4j.LoggerFactory.getLogger(LogManagementApplication.class);

	@Bean
	public CommandLineRunner commandLineRunner() {
		return args -> {
			logger.error("commons logging error...");
			logger.info("commons logging info...");
			logger.debug("commons logging debug...");

			logger2.error("slf4j logging error...");
			logger2.info("slf4j logging info...");
			logger2.debug("slf4j logging debug...");

		};

	}

}
