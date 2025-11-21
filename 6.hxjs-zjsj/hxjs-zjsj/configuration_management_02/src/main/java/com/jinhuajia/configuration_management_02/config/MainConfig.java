package com.jinhuajia.configuration_management_02.config;

import com.jinhuajia.configuration_management_02.properties.OtherMember;
import lombok.Data;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringBootConfiguration;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Import;
import org.springframework.context.annotation.ImportResource;

import org.springframework.core.env.Environment;
import org.springframework.web.client.RestTemplate;

/**
 * @author: WuPeng
 * @description: 主配置类
 * @date: 2025/2/5 17:56
 */
@SpringBootConfiguration
//@Import({DataSoureceConfiguration.class,RedisConfiguration.class})
//@ImportResource({"classpath:config/mybatis-config.xml"})
public class MainConfig {

//    @Autowired
//    private Environment env;

//    @Value("${user.name}")
//    public String name;
//
//    @Value("${user.age}")
//    public Integer age;
//
//    @Value("${user.sex}")
//    public String sex;

//    public String getProperty(String key){
//        return env.getProperty(key);
//    }
//
//    @Bean
//    public RestTemplate restTemplate(){
//        return new RestTemplate();
//    }

    @Bean
    @ConfigurationProperties(prefix = "nickname")
    public OtherMember otherMember(){
        return new OtherMember();
    }


}
