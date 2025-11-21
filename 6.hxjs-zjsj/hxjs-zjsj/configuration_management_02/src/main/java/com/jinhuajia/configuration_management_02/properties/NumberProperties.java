package com.jinhuajia.configuration_management_02.properties;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.context.properties.bind.ConstructorBinding;

/**
 * @author: WuPeng
 * @description: user配置
 * @date: 2025/2/6 11:24
 */
@ConfigurationProperties(prefix = "number")
public class NumberProperties {

    private final String xxx; // 字段必须是 final

//    @ConstructorBinding 可选
    public NumberProperties(String xxx) {
        this.xxx = xxx;
    }

    @Override
    public String toString() {
        return "NumberProperties{" +
                "xxx='" + xxx + '\'' +
                '}';
    }
}
