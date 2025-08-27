package com.f_输入与输出;

import java.io.File;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousFileChannel;
import java.nio.channels.CompletionHandler;
import java.nio.file.*;
import java.util.Collections;
import java.util.EnumSet;
import java.util.Objects;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class AioCopyTest {
    public static void main(String[] args) throws Exception {
        Path srcDir = Paths.get("testdata");
        Path destDir = Paths.get("aio_output");
        Files.createDirectories(destDir);

        ExecutorService pool = Executors.newFixedThreadPool(4);
        CountDownLatch latch = new CountDownLatch(Objects.requireNonNull(srcDir.toFile().listFiles()).length);

        long start = System.currentTimeMillis();

        for (File file : Objects.requireNonNull(srcDir.toFile().listFiles())) {
            // 不用try-with-resources，通道不能提前关闭
            AsynchronousFileChannel inChannel = AsynchronousFileChannel.open(file.toPath(), Collections.singleton(StandardOpenOption.READ), pool);

            EnumSet<StandardOpenOption> writeOptions = EnumSet.of(StandardOpenOption.WRITE, StandardOpenOption.CREATE, StandardOpenOption.TRUNCATE_EXISTING);
            AsynchronousFileChannel outChannel = AsynchronousFileChannel.open(destDir.resolve(file.getName()), writeOptions, pool);

            readAndWrite(inChannel, outChannel, 0, latch);
        }

        latch.await();
        pool.shutdown();

        System.out.println("AIO 耗时: " + (System.currentTimeMillis() - start) + " ms");
    }

    private static void readAndWrite(AsynchronousFileChannel inChannel,
                                     AsynchronousFileChannel outChannel,
                                     long position,
                                     CountDownLatch latch) {
        ByteBuffer buffer = ByteBuffer.allocate(8192);

        inChannel.read(buffer, position, null, new CompletionHandler<Integer, Object>() {
            @Override
            public void completed(Integer bytesRead, Object attachment) {
                if (bytesRead == -1) {
                    try {
                        inChannel.close();
                        outChannel.close();
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                    latch.countDown();
                    return;
                }

                buffer.flip();
                outChannel.write(buffer, position, null, new CompletionHandler<Integer, Object>() {
                    @Override
                    public void completed(Integer bytesWritten, Object attachment) {
                        // 下一段读取
                        readAndWrite(inChannel, outChannel, position + bytesRead, latch);
                    }

                    @Override
                    public void failed(Throwable exc, Object attachment) {
                        exc.printStackTrace();
                        try {
                            inChannel.close();
                            outChannel.close();
                        } catch (IOException e) {
                            e.printStackTrace();
                        }
                        latch.countDown();
                    }
                });
            }

            @Override
            public void failed(Throwable exc, Object attachment) {
                exc.printStackTrace();
                try {
                    inChannel.close();
                    outChannel.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
                latch.countDown();
            }
        });
    }

}


