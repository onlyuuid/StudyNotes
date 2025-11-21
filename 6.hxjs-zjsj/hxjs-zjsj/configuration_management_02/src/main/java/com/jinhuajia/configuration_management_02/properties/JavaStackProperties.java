package com.jinhuajia.configuration_management_02.properties;

import jakarta.validation.constraints.NotNull;
import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.validation.annotation.Validated;

/**
 * @author: WuPeng
 * @description:
 * @date: 2025/2/6 14:58
 */
@Data
@ConfigurationProperties(prefix = "javastack")
@Validated
public class JavaStackProperties {

    private boolean enable;

    @NotNull
    private String name;
}
