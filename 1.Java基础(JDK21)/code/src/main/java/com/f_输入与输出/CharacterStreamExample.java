package com.f_输入与输出;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.time.Instant;

public class CharacterStreamExample {
    public static void main(String[] args) throws IOException {
        String inputFile = "input.txt";
        String outputFile = "output.txt";
        Instant start = Instant.now();
        // 推荐方式：使用 InputStreamReader/OutputStreamWriter 显式指定编码
//        File file = new File(outputFile);
//        if(!file.exists()){
//            file.createNewFile();
//        }
        try (
                FileInputStream fis = new FileInputStream(inputFile);
                FileOutputStream fos = new FileOutputStream(outputFile);

                // 字节流转字符流, 使用 UTF-8 编码读取和写入
                InputStreamReader isr = new InputStreamReader(fis, StandardCharsets.UTF_8);
                OutputStreamWriter osw = new OutputStreamWriter(fos, StandardCharsets.UTF_8);

                // 添加缓冲
                BufferedReader br = new BufferedReader(isr);
                BufferedWriter bw = new BufferedWriter(osw)
        ) {
            String line;
            // 逐行读取
            while ((line = br.readLine()) != null) {
                // 处理每一行（例如，转换为大写）
                String processedLine = line.toUpperCase();
                // 写入处理后的行
                bw.write(processedLine);
                bw.newLine(); // 写入平台相关的行分隔符
            }
            Instant end = Instant.now();
            Duration between = Duration.between(start, end);
            System.out.println("文本文件处理完成！共耗时："+between.toMillis()+"毫秒");

        } catch (UnsupportedEncodingException e) {
            System.err.println("不支持的编码: " + e.getMessage());
        } catch (FileNotFoundException e) {
            System.err.println("文件未找到: " + e.getMessage());
        } catch (IOException e) {
            System.err.println("I/O 错误: " + e.getMessage());
        }
    }
}
