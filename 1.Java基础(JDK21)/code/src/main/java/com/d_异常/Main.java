package com.d_异常;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * @author lanxin
 * @version 1.0
 * @description: TODO
 * @date 2025/8/26 21:38
 */
public class Main {

    public static void main(String[] args) {
        copy("1.txt","2.txt");
    }


    public static void copy(String path1,String path2){
        Path path = Path.of(path1);
        // 使用try-with-resources语法, 可以自动释放资源
        try (
                FileOutputStream fileOutputStream = new FileOutputStream(path2)
        ){
            Files.copy(path, fileOutputStream);
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
