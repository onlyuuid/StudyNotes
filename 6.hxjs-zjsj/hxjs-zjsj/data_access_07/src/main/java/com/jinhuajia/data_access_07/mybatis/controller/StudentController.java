package com.jinhuajia.data_access_07.mybatis.controller;

import com.jinhuajia.data_access_07.mybatis.domain.Student;
import com.jinhuajia.data_access_07.mybatis.service.StudentService;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author: WuPeng
 * @description:
 * @date: 2025/3/16 17:40
 */
@RestController
@RequestMapping("/student")
@RequiredArgsConstructor
public class StudentController {

    private final StudentService studentService;

    @GetMapping("/getById/{id}")
    public Student selectStudentById(@PathVariable("id") Integer id) {
        return studentService.getById(1);
    }
}
