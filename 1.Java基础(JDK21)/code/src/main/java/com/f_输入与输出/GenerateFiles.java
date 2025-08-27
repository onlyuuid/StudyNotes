package com.f_输入与输出;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Random;

public class GenerateFiles {
    public static void main(String[] args) throws IOException {
        int fileCount = 10; // 文件数量
        int fileSizeMB = 50; // 文件大小 MB
        byte[] buffer = new byte[1024 * 1024]; // 1MB 缓冲区
        Random random = new Random();

        for (int i = 1; i <= fileCount; i++) {
            try (FileOutputStream fos = new FileOutputStream("testdata/file" + i + ".bin")) {
                for (int j = 0; j < fileSizeMB; j++) {
                    random.nextBytes(buffer);
                    fos.write(buffer);
                }
            }
            System.out.println("生成 file" + i + ".bin 完成");
        }
    }
}

