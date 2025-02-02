package com.基础语法_01.数据类型与变量;

/**
 * @author: WuPeng
 * @description: 数据类型与变量
 * @date: 2024/11/26 10:57
 */

public class Main {
    public static void main(String[] args) {
        /**
         * 基本数据类型：
         */
        // 整数类型
        byte a = 10;
        short b = 20;
        int c = 30;
        long d = 40L;

        // 浮点数类型
        float e = 5.5F;
        double f = 6.6;

        // 布尔类型
        boolean g = true;
        boolean h = false;

        // 字符类型
        char i = 'a';
        char j = '\u4e00';

        // 输出所有结果
        System.out.println("整数类型：" + a + ", " + b + ", " + c + ", " + d);
        System.out.println("浮点数类型：" + e + ", " + f);
        System.out.println("布尔类型：" + g + ", " + h);
        System.out.println("字符类型：" + i + ", " + j);
    }
}
