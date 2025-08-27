package com.a_基础语法.c_运算符与表达式;

/**
 * @author: WuPeng
 * @description: 三元运算符
 * @date: 2025/3/19 15:21 
 */

public class TernaryOperator {

    public static void main(String[] args) {
        int a = 10;
        int b = 20;

        int max = (a > b)?a:b;
        System.out.println(max); // 20
    }
}
