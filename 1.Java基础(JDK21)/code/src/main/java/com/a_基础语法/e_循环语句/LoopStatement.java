package com.a_基础语法.e_循环语句;

import java.awt.*;
import java.util.*;
import java.util.List;

/**
 * @author: WuPeng
 * @description: 循环语句
 * @date: 2025/3/19 15:33 
 */

public class LoopStatement {

    public static void main(String[] args) {
//        int[] arr = {2,4,5,46,7};
//        for (int i = 0; i < arr.length; i++) {
//            System.out.println(arr[i]);
//        }

//        int i = 1;
//        while (i < 10){
//            System.out.println("i = " + i);
//            i++;
//        }

//        int i = 1;
//        do{
//            System.out.println("i = " + i);
//        }while(i > 20);


        traverse();


    }

    public static void traverse(){
        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(2);
        list.add(3);
//
//        // 增强for循环
//        for (Integer i : list) {
//            System.out.println(i);
//        }

//        Iterator<Integer> iterator = list.iterator();
//        while (iterator.hasNext()){
//            Integer next = iterator.next();
//            System.out.println(next);
//        }

        list.stream().forEach(System.out::println);
    }
}
