package com.基础语法_01.运算符与表达式;

/**
 * @author: WuPeng
 * @description: 赋值运算符
 * @date: 2025/3/19 15:12 
 */

public class AssigningOperator {

    public static void main(String[] args) {
        int a = 10;
        int b = 14;
        int c = 20;
        int d = 4;

        System.out.println(a >>= 2); // 2
        System.out.println(b <<= 2); // 56
        System.out.println(c &= 2);  // 0
        System.out.println(d |= 3);  // 7
    }
}
