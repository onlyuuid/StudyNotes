package com.jinhuajia.data_access_07.redis;

import lombok.RequiredArgsConstructor;
import org.springframework.data.redis.core.SetOperations;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.data.redis.core.ValueOperations;
import org.springframework.stereotype.Service;

/**
 * @author: WuPeng
 * @description:
 * @date: 2025/4/20 11:41
 */
@Service
@RequiredArgsConstructor
public class UseStringRedisTemplate {

    private final StringRedisTemplate stringRedisTemplate;

    public ValueOperations set(String key, String value) {
        ValueOperations<String, String> valueOperations = stringRedisTemplate.opsForValue();
        valueOperations.set(key, value);
        return valueOperations;
    }
}
