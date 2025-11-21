package com.jinhuajia.data_access_07;

import com.baomidou.mybatisplus.autoconfigure.MybatisPlusProperties;
//import com.jinhuajia.data_access_07.domain.User;
import com.jinhuajia.data_access_07.domain.Person;
import com.jinhuajia.data_access_07.mybatis.domain.Student;
import com.jinhuajia.data_access_07.mybatis.service.StudentService;
//import com.jinhuajia.data_access_07.service.UserRepository;
import com.jinhuajia.data_access_07.redis.RedisConfig;
import com.jinhuajia.data_access_07.redis.UseStringRedisTemplate;
import jakarta.annotation.Resource;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.mybatis.spring.annotation.MapperScan;
import org.mybatis.spring.mapper.ClassPathMapperScanner;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.support.FactoryBeanRegistrySupport;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.ValueOperations;
import org.springframework.jdbc.core.JdbcTemplate;



@SpringBootApplication
@MapperScan(basePackages = {"com.jinhuajia.data_access_07.mybatis.mapper"})
//@EnableAspectJAutoProxy(exposeProxy = true)
@Slf4j
@RequiredArgsConstructor
public class DataAccess07Application {

//    private final JdbcTemplate jdbcTemplate;

    private final StudentService studentService;

    private final UseStringRedisTemplate useStringRedisTemplate;

//    private final RedisTemplate redisTemplate;

      @Autowired
      private RedisTemplate<String,Object> redisTemplate;

//    @Resource(name = "stringRedisTemplate")
//    private ValueOperations valueOperations;



    public static void main(String[] args) {
//        FactoryBeanRegistrySupport
//        ClassPathMapperScanner
//        TransactionAutoConfiguration
//        DataSourceTransactionManagerAutoConfiguration
//        TransactionProperties
//        JdbcProperties
//        JpaRepositoriesAutoConfiguration
//        HibernateJpaAutoConfiguration
        SpringApplication.run(DataAccess07Application.class, args);

    }
//    @Bean
//    public CommandLineRunner commandLineRunner() {
//        return args -> {
////            String username = jdbcTemplate.queryForObject("select name from user where id= 1",String.class);
////            log.info("username:{}", username);
//
//            List<Map<String, Object>> list = jdbcTemplate.queryForList("select name from user");
//            log.info("total list:{}", list.size());
//        };
//    }

//    @Bean
//    public CommandLineRunner commandLineRunner() {
//        return args -> {
//            User user = userRepository.findById(1L).orElseGet(null);
//            log.info("user:{}", user);
//
//        };
//    }

//    @Bean
//    public CommandLineRunner commandLineRunner() {
//        return args -> {
//            Student student1 = studentService.getByStudentName("李四",0);
//            log.info("student1 = " + student1);
//
//            Student student2 = studentService.getByStudentName("王五",1);
//            log.info("student2 = " + student2);
//        };
//    }

    @Bean
    public CommandLineRunner commandLineRunner() {
        return args -> {
            ValueOperations set = useStringRedisTemplate.set("name", "张三");
            System.out.println("set = " + set.get("name"));
        };
    }

//    @Bean
//    public ValueOperations<String, Object> valueOperations() {
//        ValueOperations valueOperations = redisTemplate.opsForValue();
//        return valueOperations;
//    }


//    @Autowired
//    private ValueOperations<String, Object> valueOperations;

}
