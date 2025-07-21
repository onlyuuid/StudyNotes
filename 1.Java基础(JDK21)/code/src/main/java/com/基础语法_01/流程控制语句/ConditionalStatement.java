package com.基础语法_01.流程控制语句;

/**
 * @author: WuPeng
 * @description: 条件语句
 * @date: 2025/3/19 15:25 
 */

public class ConditionalStatement {
    public static void main(String[] args) {
//        int a = 10;
//        int b = 20;
//        int c = 15;
//        if(a > b){
//            System.out.println(a);
//        }else if (a < c) {
//            System.out.println("c = " + c);
//        }else{
//            System.out.println("a = " + a);
//        }

//        int a = 3;
//
//        switch(a){
//            case 1:
//                System.out.println(1);
//                break;
//            case 2:
//                System.out.println(2);
//                break;
//            case 3:
//                System.out.println(3);
//                break;
//            default:
//                System.out.println(4);
//        }
        String s = "hello";

        switch(s){
            case "hello" -> System.out.println("hello");
            case "world" -> System.out.println("world");
            default -> System.out.println("default");
        }

    }
}
