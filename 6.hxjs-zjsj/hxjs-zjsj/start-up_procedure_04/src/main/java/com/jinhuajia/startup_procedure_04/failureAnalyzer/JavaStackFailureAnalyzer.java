package com.jinhuajia.startup_procedure_04.failureAnalyzer;

import com.jinhuajia.startup_procedure_04.exception.JavaStackException;
import org.springframework.boot.diagnostics.AbstractFailureAnalyzer;
import org.springframework.boot.diagnostics.FailureAnalysis;

/**
 * @author: WuPeng
 * @description:
 * @date: 2025/2/19 16:28
 */

public class JavaStackFailureAnalyzer extends AbstractFailureAnalyzer<JavaStackException> {
    @Override
    protected FailureAnalysis analyze(Throwable rootFailure, JavaStackException cause) {
        return new FailureAnalysis("发生了javastack 异常",
                "请检查一下",cause);
    }
}
