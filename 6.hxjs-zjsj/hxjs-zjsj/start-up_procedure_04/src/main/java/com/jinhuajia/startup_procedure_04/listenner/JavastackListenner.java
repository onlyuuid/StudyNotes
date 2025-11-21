package com.jinhuajia.startup_procedure_04.listenner;

import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.availability.AvailabilityChangeEvent;
import org.springframework.boot.availability.ReadinessState;
import org.springframework.context.ApplicationListener;
import org.springframework.stereotype.Component;

/**
 * @author: WuPeng
 * @description:
 * @date: 2025/2/19 17:58
 */
@Slf4j
//@Component
public class JavastackListenner implements ApplicationListener<AvailabilityChangeEvent> {
    @Override
    public void onApplicationEvent(AvailabilityChangeEvent event) {
        log.info("监听到了事件："+event);
        if(ReadinessState.ACCEPTING_TRAFFIC == event.getState()){
            log.info("应用启动完成，可以接收请求了...");
        }
    }
}
