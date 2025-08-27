package com.b_面向对象编程.a_类与对象;

import java.io.Serializable;
import java.util.Objects;

public record Dog(Integer id, String name, int age) {
}

//public final class Dog implements Serializable {
//
//    private final Integer id;
//    private final String name;
//    private final Integer age;
//
//    public Dog(Integer id, String name, Integer age) {
//        this.id = id;
//        this.name = name;
//        this.age = age;
//    }
//
//    public Integer id() {
//        return id;
//    }
//
//    public String name() {
//        return name;
//    }
//
//    public Integer age() {
//        return age;
//    }
//
//    @Override
//    public boolean equals(Object o) {
//        if (o == null || getClass() != o.getClass()) return false;
//        Dog dog = (Dog) o;
//        return Objects.equals(id, dog.id) && Objects.equals(name, dog.name) && Objects.equals(age, dog.age);
//    }
//
//    @Override
//    public int hashCode() {
//        return Objects.hash(id, name, age);
//    }
//
//    @Override
//    public String toString() {
//        return "Dog[" +
//                "id=" + id +
//                ", name=" + name +
//                ", age=" + age +
//                ']';
//    }
//}
