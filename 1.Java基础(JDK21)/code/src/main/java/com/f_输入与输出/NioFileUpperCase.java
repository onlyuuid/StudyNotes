package com.f_输入与输出;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.CharBuffer;
import java.nio.channels.FileChannel;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.time.Duration;
import java.time.Instant;

public class NioFileUpperCase {
    public static void main(String[] args) {
        Path inputPath = Path.of("input.txt");
        Path outputPath = Path.of("output.txt");
        Charset charset = StandardCharsets.UTF_8;
        Instant start = Instant.now();
        try (
                // 打开输入文件通道
                FileChannel inChannel = FileChannel.open(inputPath, StandardOpenOption.READ);
                // 打开输出文件通道（不存在则创建，存在则覆盖）
                FileChannel outChannel = FileChannel.open(outputPath,
                        StandardOpenOption.CREATE,
                        StandardOpenOption.TRUNCATE_EXISTING,
                        StandardOpenOption.WRITE)
        ) {
            ByteBuffer byteBuffer = ByteBuffer.allocate(1024); // 缓冲区
            while (inChannel.read(byteBuffer) != -1) {
                byteBuffer.flip(); // 切换到读模式

                // 解码为字符
                CharBuffer charBuffer = charset.decode(byteBuffer);
                // 转大写
                String upper = charBuffer.toString().toUpperCase();

                // 编码回字节
                ByteBuffer outputBuffer = charset.encode(upper);
                outChannel.write(outputBuffer);

                byteBuffer.clear(); // 清空缓冲区
            }
            Instant end = Instant.now();
            Duration between = Duration.between(start, end);
            System.out.println("NIO 文件处理完成！共耗时："+between.toMillis()+"毫秒");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
