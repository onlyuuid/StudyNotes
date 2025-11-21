package com.jinhuajia.data_access_07.mybatis.domain;

import com.baomidou.mybatisplus.annotation.*;
import lombok.Data;
import lombok.ToString;

import java.io.Serializable;

/**
 * @author: WuPeng
 * @description:
 * @date: 2025/3/16 17:40
 */
@TableName(value = "student")
@Data
@ToString
public class Student implements Serializable {

    @TableField
    private static final long serialVersionUID = 1L;

    @TableId(type = IdType.AUTO) // id自增
    private Integer id;

    @TableField(insertStrategy = FieldStrategy.NOT_NULL)
    private String name;

    @TableField(insertStrategy = FieldStrategy.NOT_NULL)
    private Integer age;

    @TableField(insertStrategy = FieldStrategy.NOT_NULL)
    private String sex;
}
