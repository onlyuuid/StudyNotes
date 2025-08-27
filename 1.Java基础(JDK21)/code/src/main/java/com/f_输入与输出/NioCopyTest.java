package com.f_输入与输出;

import java.io.*;
import java.nio.channels.FileChannel;
import java.nio.file.*;
import java.util.concurrent.*;

public class NioCopyTest {
    public static void main(String[] args) throws Exception {
        Path srcDir = Paths.get("testdata");
        Path destDir = Paths.get("nio_output");
        Files.createDirectories(destDir);

        ExecutorService executor = Executors.newFixedThreadPool(4);
        long start = System.currentTimeMillis();

        for (File file : srcDir.toFile().listFiles()) {
            executor.submit(() -> {
                try (FileChannel inChannel = FileChannel.open(file.toPath(), StandardOpenOption.READ);
                     FileChannel outChannel = FileChannel.open(destDir.resolve(file.getName()),
                             StandardOpenOption.CREATE, StandardOpenOption.WRITE)) {
                    inChannel.transferTo(0, inChannel.size(), outChannel);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });
        }

        executor.shutdown();
        executor.awaitTermination(1, TimeUnit.HOURS);

        System.out.println("NIO 耗时: " + (System.currentTimeMillis() - start) + " ms");
    }
}

