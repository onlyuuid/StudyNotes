package com.b_面向对象编程.a_类与对象;

public class Main{

    public static void main(String[] args) {
        Person p = new Person();
        p.setName("person");
        p.setAge(23);
        System.out.println("p = " + p.getInfo());

        Tom tom = new Tom();
        tom.setName("tom");
        tom.setAge(23);
        System.out.println("tom = " + tom.getInfo());

//        Dog tom1 = new Dog(1, "tom", 23);
//        System.out.println("tom1 = " + tom1);
    }
}

