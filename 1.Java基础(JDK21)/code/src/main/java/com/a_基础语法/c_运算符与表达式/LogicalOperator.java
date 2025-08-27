package com.a_基础语法.c_运算符与表达式;

/**
 * @author: WuPeng
 * @description: 逻辑运算符
 * @date: 2025/3/19 14:43
 */

public class LogicalOperator {

    public static void main(String[] args) {
       boolean a = true;
       boolean b = false;

       boolean c = a && b;
       boolean d = a && !b;
       System.out.println("a && b = " + c); // a && b = false
       System.out.println("a && !b = " + d); // a && !b = true
    }
}
