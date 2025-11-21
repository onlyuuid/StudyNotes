package com.jinhuajia.startup_procedure_04.failureAnalyzer;

import org.springframework.boot.diagnostics.AbstractFailureAnalyzer;
import org.springframework.boot.diagnostics.FailureAnalysis;
import org.springframework.boot.web.server.PortInUseException;

/**
 * @author: WuPeng
 * @description:
 * @date: 2025/2/19 16:11
 */

public class PortInUseFailureAnalyzer extends AbstractFailureAnalyzer<PortInUseException> {

    @Override
    protected FailureAnalysis analyze(Throwable rootFailure, PortInUseException cause) {
        return new FailureAnalysis("端口"+cause.getPort()+"被占用",
                                        "请检查"+cause.getPort()+"端口",
                                        cause);
    }
}
