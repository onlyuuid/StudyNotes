package com.b_面向对象编程.a_类与对象;

public class Tom extends Person{

    public String getInfo(){
        return super.getName()+" "+super.getAge();
    }
}
