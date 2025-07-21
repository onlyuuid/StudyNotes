package com.基础语法_01.运算符与表达式;

/**
 * @author: WuPeng
 * @description: 位运算
 * @date: 2025/3/19 14:59 
 */

public class BitOperation {
    public static void main(String[] args) {
        int a = 2; // 二进制 10
        int b = 3; // 二进制 11
        int c = 5; // 二进制 101

        System.out.println(a & b);  // 2
        System.out.println(a | b);  // 3
        System.out.println(a ^ b);  // 1
        System.out.println(~a);     // -3
        System.out.println(c >> 2); // 1
    }
}
