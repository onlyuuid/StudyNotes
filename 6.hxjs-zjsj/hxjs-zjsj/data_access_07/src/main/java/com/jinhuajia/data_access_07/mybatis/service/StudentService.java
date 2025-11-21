package com.jinhuajia.data_access_07.mybatis.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.jinhuajia.data_access_07.mybatis.domain.Student;

/**
 * @author: WuPeng
 * @description:
 * @date: 2025/3/16 17:36
 */

public interface StudentService extends IService<Student> {

//    /**
//     * 根据id查询
//     * @param id
//     * @return
//     */
//    public Student selectStudentById(Integer id);

    public Student getByStudentName(String studentName,int type);
}
