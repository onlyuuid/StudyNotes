package com.jinhuajia.data_access_07.service;

import org.springframework.aop.framework.AopContext;
import org.springframework.context.annotation.EnableAspectJAutoProxy;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Propagation;
import org.springframework.transaction.annotation.Transactional;

/**
 * @author: WuPeng
 * @description:
 * @date: 2025/2/24 17:18
 */
@Service
public class UserService {


//    public int update(Long id ){
//        update2(id);
//        // 1.查询操作
//
//        // 2.更新操作
//
////        throw new RuntimeException("操作执行失败");
//        return 1;
//    }

//    public void update1(Long id ){
//        update2(id);
//    }
//
//    @Transactional
//    public void update2(Long id ){
//        // update1
//    }

//    @Transactional
//    public void update1(Long id ) throws Exception {
//        ((UserService)AopContext.currentProxy()).update2(id);
//    }
//
//    @Transactional(rollbackFor = Exception.class)
//    public void update2(Long id ) throws Exception {
//        try{
//            // update data
//        } catch (Exception e) {
//           throw new Exception("操作失败");
//        }
//    }
}
