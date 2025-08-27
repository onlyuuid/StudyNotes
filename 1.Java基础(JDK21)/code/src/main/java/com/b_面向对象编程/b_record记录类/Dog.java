package com.b_面向对象编程.b_record记录类;

public record Dog(String name, Integer age) {

    // 自定义带参数校验的构造方法
    public Dog(String name, Integer age) {
       if (age < 0 || age > 100) {
           throw new RuntimeException("");
       }else{
           this.name = name;
           this.age = age;
       }
    }

    // 其他自定义方法
    public String getInfo() {
        return name+age;
    }
}
