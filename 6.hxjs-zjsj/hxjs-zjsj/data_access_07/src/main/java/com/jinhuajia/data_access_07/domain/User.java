//package com.jinhuajia.data_access_07.domain;
//
//import jakarta.persistence.*;
//import org.springframework.data.repository.Repository;
//
///**
// * @author: WuPeng
// * @description:
// * @date: 2025/2/25 16:06
// */
//@Entity(name = "user")
//public class User {
//
//    @Id
//    @GeneratedValue(strategy = GenerationType.IDENTITY)
//    private Long id;
//
//    @Column(nullable = false)
//    private String name;
//
//    public Long getId() {
//        return id;
//    }
//
//    public void setId(Long id) {
//        this.id = id;
//    }
//
//    public String getName() {
//        return name;
//    }
//
//    public void setName(String name) {
//        this.name = name;
//    }
//
//    @Override
//    public String toString() {
//        return "User{" +
//                "id=" + id +
//                ", name='" + name + '\'' +
//                '}';
//    }
//}
