package com.f_输入与输出;

import java.io.*;
import java.nio.file.*;
import java.util.concurrent.*;

public class BioCopyTest {
    public static void main(String[] args) throws Exception {
        Path srcDir = Paths.get("testdata");
        Path destDir = Paths.get("bio_output");
        Files.createDirectories(destDir);

        ExecutorService executor = Executors.newFixedThreadPool(4);
        long start = System.currentTimeMillis();

        for (File file : srcDir.toFile().listFiles()) {
            executor.submit(() -> {
                try (InputStream in = new FileInputStream(file);
                     OutputStream out = new FileOutputStream(destDir.resolve(file.getName()).toFile())) {
                    byte[] buf = new byte[8192];
                    int len;
                    while ((len = in.read(buf)) != -1) {
                        out.write(buf, 0, len);
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });
        }

        executor.shutdown();
        executor.awaitTermination(1, TimeUnit.HOURS);

        System.out.println("BIO 耗时: " + (System.currentTimeMillis() - start) + " ms");
    }
}

