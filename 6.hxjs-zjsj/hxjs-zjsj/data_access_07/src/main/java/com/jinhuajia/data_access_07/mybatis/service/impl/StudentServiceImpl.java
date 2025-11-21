package com.jinhuajia.data_access_07.mybatis.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.jinhuajia.data_access_07.mybatis.domain.Student;
import com.jinhuajia.data_access_07.mybatis.mapper.StudentMapper;
import com.jinhuajia.data_access_07.mybatis.service.StudentService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * @author: WuPeng
 * @description:
 * @date: 2025/3/16 17:42
 */
@Service
@Slf4j
@RequiredArgsConstructor
public class StudentServiceImpl
        extends ServiceImpl<StudentMapper,Student>
        implements StudentService {
    private final StudentMapper studentMapper;

//    @Autowired
//    private StudentMapper studentMapper;
//
//    @Override
//    public Student selectStudentById(Integer id) {
//        return studentMapper.selectStudentById(id);
//    }
    public Student getByStudentName(String studentName,int type) {
        if(type == 0){
            // xml
            log.info("query from xml");
            return studentMapper.getByStudentName(studentName);
        }else {
            // QueryWrapper
            log.info("query from wrapper");
            QueryWrapper<Student> studentQueryWrapper = new QueryWrapper<>();
            studentQueryWrapper.eq("name",studentName);
            return studentMapper.selectOne(studentQueryWrapper);
        }
    }
}
