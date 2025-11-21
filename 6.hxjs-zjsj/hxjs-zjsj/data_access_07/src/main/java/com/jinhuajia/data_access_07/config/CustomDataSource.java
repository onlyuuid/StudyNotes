//package com.jinhuajia.data_access_07.config;
//
//import org.springframework.boot.context.properties.ConfigurationProperties;
//import org.springframework.boot.jdbc.DataSourceBuilder;
//import org.springframework.context.annotation.Bean;
//import org.springframework.context.annotation.Configuration;
//import org.springframework.context.annotation.Primary;
//
//import javax.sql.DataSource;
//
///**
// * @author: WuPeng
// * @description:
// * @date: 2025/2/22 17:32
// */
//@Configuration(proxyBeanMethods = false)
//public class CustomDataSource {
//
//    @Primary
//    @Bean
//    @ConfigurationProperties(prefix = "spring.datasource.xx.one")
//    public DataSource dataSource1() {
//        return DataSourceBuilder.create().build();
//    }
//
//    @Bean
//    @ConfigurationProperties(prefix = "spring.datasource.xx.tow")
//    public DataSource dataSource() {
//        return DataSourceBuilder.create().build();
//    }
//}
