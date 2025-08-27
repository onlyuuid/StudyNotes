package com.c_java常用类用集合框架;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Test {
    public static void main(String[] args) throws IOException {
//        System.out.println("请输入一个字符");
//        int read = System.in.read();
//        System.out.println("你输入的是："+(char)read);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("请输入字符串");
        String line = br.readLine();
        System.out.println("你输入的字符串是："+line);
    }


}
