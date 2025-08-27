package com.c_java常用类用集合框架;

import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.List;

public class Test2 {

    @Test
    public void test1() throws IOException {

//        Path path1 = Paths.get("D", "test", "2.text");
//
//        System.out.println(path.getFileName());
//        System.out.println(path.getParent());
//        System.out.println(path.getRoot());
//        System.out.println(path.isAbsolute());
//        System.out.println(path.toAbsolutePath());

        // 创建文件（如果存在会抛异常）
            Path file = Paths.get("D:\\1.text");

            Files.createFile(file); // 创建文件 (只能创建文件，不能创建目录)

            Files.createDirectory(Paths.get("D:\\myDir")); // 创建目录

            Files.write(file, "hello world".getBytes()); // 写入文件

//            Files.delete(file); // 删除文件
    }

    @Test
    public void test2() throws IOException {
        Path src = Paths.get("D:\\1.text");
        Path dest = Paths.get("D:\\b.txt");

        // 复制
        Files.copy(src, dest, StandardCopyOption.REPLACE_EXISTING);

        // 移动（可用于重命名）
        Files.move(src, dest, StandardCopyOption.REPLACE_EXISTING);

    }

    @Test
    public void test3() throws IOException {
        // 写入（会覆盖）
        Files.write(Paths.get("D:\\b.txt"), "Hello Java".getBytes());

        // 读取（一次性读全部）
        byte[] bytes = Files.readAllBytes(Paths.get("D:\\b.txt"));
        System.out.println(new String(bytes));

        // 逐行读取
        List<String> lines = Files.readAllLines(Paths.get("D:\\b.txt"));
        lines.forEach(System.out::println);

    }

    @Test
    public void test4() throws IOException {
        Path p = Paths.get("D:\\b.txt");
        System.out.println(Files.exists(p));     // 文件是否存在
        System.out.println(Files.isDirectory(p)); // 是否是目录
        System.out.println(Files.size(p));       // 文件大小（字节）
        System.out.println(Files.getLastModifiedTime(p)); // 最后修改时间
    }
}
