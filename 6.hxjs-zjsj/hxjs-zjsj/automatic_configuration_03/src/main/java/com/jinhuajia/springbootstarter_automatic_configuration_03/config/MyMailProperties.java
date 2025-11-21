package com.jinhuajia.springbootstarter_automatic_configuration_03.config;

import lombok.Data;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringBootConfiguration;
import org.springframework.boot.autoconfigure.mail.MailProperties;
import org.springframework.boot.context.properties.ConfigurationProperties;

/**
 * @author: WuPeng
 * @description:
 * @date: 2025/2/15 15:00
 */
@SpringBootConfiguration
public class MyMailProperties{

    @Value("${mail.from}")
    private String from;

    @Value("${mail.personal}")
    private String personal;

    @Value("${mail.subject}")
    private String subject;

    public String getFrom() {
        return from;
    }

    public void setFrom(String from) {
        this.from = from;
    }

    public String getPersonal() {
        return personal;
    }

    public void setPersonal(String personal) {
        this.personal = personal;
    }

    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
}
