package com.jinhuajia.configuration_management_02.properties;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;

/**
 * @author: WuPeng
 * @description: user配置
 * @date: 2025/2/6 11:24
 */
//@SpringBootConfiguration
@Data
@ConfigurationProperties(prefix = "user")
public class UserProperties {

    private String name2;

    private Integer age;

    private String sex;

    private Integer phone;

    private Addr addr;

    private Addr2 addr2;

    public static class Addr {
        private String city;

        public String getCity() {
            return city;
        }

        public void setCity(String city) {
            this.city = city;
        }
    }

    public static class Addr2 {
        private String city2;

        public String getCity2() {
            return city2;
        }

        public void setCity2(String city2) {
            this.city2 = city2;
        }
    }

}
