package com.f_输入与输出;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.AsynchronousFileChannel;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.time.Duration;
import java.time.Instant;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

public class AioFileUpperCase {
    public static void main(String[] args) {
        Path inputPath = Path.of("input.txt");
        Path outputPath = Path.of("output.txt");
        Charset charset = StandardCharsets.UTF_8;
        Instant start = Instant.now();
        try (
                // 异步打开文件
                AsynchronousFileChannel inChannel = AsynchronousFileChannel.open(inputPath, StandardOpenOption.READ);
                AsynchronousFileChannel outChannel = AsynchronousFileChannel.open(outputPath,
                        StandardOpenOption.WRITE,
                        StandardOpenOption.CREATE,
                        StandardOpenOption.TRUNCATE_EXISTING)
        ) {
            ByteBuffer buffer = ByteBuffer.allocate(1024);

            // 发起异步读取
            Future<Integer> readFuture = inChannel.read(buffer, 0);
            int bytesRead = readFuture.get(); // 等待读取完成（阻塞等待，但可以用回调替代）

            if (bytesRead != -1) {
                buffer.flip();
                // 解码成字符串
                String content = charset.decode(buffer).toString();
                // 转大写
                String upper = content.toUpperCase();
                // 编码回字节
                ByteBuffer outputBuffer = charset.encode(upper);

                // 异步写入
                Future<Integer> writeFuture = outChannel.write(outputBuffer, 0);
                writeFuture.get(); // 等待写入完成
            }
            Instant end = Instant.now();
            Duration between = Duration.between(start, end);
            System.out.println("AIO 文件处理完成！共耗时："+between.toMillis()+"毫秒");

        } catch (IOException | InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }
}
