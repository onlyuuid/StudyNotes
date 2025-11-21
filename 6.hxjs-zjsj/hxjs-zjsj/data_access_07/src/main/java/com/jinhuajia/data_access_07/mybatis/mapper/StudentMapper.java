package com.jinhuajia.data_access_07.mybatis.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.jinhuajia.data_access_07.mybatis.domain.Student;
import org.apache.ibatis.annotations.Mapper;

/**
 * @author: WuPeng
 * @description:
 * @date: 2025/3/16 17:42
 */
@Mapper
public interface StudentMapper extends BaseMapper<Student> {

//    /**
//     * 根据id查询
//     * @param id
//     * @return
//     */
//    public Student selectStudentById(Integer id);

    public Student getByStudentName(String studentName);
}
