package com.b_面向对象编程.a_类与对象;

// 定义一个 Student 类
public class Student {

    private Integer id; // 学号

    private String name; // 姓名

    private Integer age; // 年龄

    protected String  address;

    // 无参构造方法
    public Student(){}

    // 有参构造方法
    public Student(Integer id, String name, Integer age) {
        this.id = id;
        this.name = name;
        this.age = age;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

//    @Override
//    public boolean equals(Object o) {
//        if (o == null || getClass() != o.getClass()) return false;
//        Student student = (Student) o;
//        return Objects.equals(id, student.id) && Objects.equals(name, student.name) && Objects.equals(age, student.age);
//    }

//    @Override
//    public int hashCode() {
//        return Objects.hash(id, name, age);
//    }


//    public void select(Integer id,String name){
//
//    }
//
//    // 重载select方法
//    public void select(String name,Integer id){
//
//    }

    public void select(Integer id){

    }

    // 重载select方法
    public void select(String name){

    }

    @Override
    public String toString() {
        return "Student{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", age=" + age +
                '}';
    }


}
