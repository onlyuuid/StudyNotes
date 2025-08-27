package com.c_java常用类用集合框架;

import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.io.InputStream;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.time.*;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.Date;
import java.util.Scanner;

public class DateTimeMain {

    @Test
    public  void test() {
        LocalDateTime now = LocalDateTime.now();// 获取当前时间
        LocalDateTime localDateTime = LocalDateTime.of(2020, 1, 1, 0, 0);// 获取指定时间
        LocalDateTime from = LocalDateTime.from(ZonedDateTime.now());// 获取最小时间
        LocalDateTime parse = LocalDateTime.parse("2020-01-01T00:00");// 将字符串转换成时间
        LocalDateTime localDateTime1 = LocalDateTime.now().plusDays(2);// 获取以当前时间为准,2天后的时间
        int year = LocalDateTime.now().getYear();   // 获取当前年份
        int month = LocalDateTime.now().getMonthValue(); // 获取当前月份
        int day = LocalDateTime.now().getDayOfMonth(); // 获取当前天
        int hour = LocalDateTime.now().getHour(); // 获取当前小时
        int minute = LocalDateTime.now().getMinute(); // 获取当前分钟
        int second = LocalDateTime.now().getSecond(); // 获取当前秒

        System.out.println(now);
        System.out.println(localDateTime);
        System.out.println(from);
        System.out.println(parse);
        System.out.println(localDateTime1);
        System.out.println(year);
        System.out.println(month);
        System.out.println(day);
        System.out.println(hour);
        System.out.println(minute);
        System.out.println(second);
    }

    @Test
    public void test1() {

//        LocalTime start = LocalTime.of(10, 0);
//        LocalTime end = LocalTime.of(23, 0);
//
//        // 获取两个时间之间的间隔
//        Duration between = Duration.between(start, end);
//        System.out.println(between); // PT13H
//        System.out.println(between.toHours()); // 13
//        System.out.println(between.toMinutes()); // 780
//
//        Duration duration = Duration.of(3, ChronoUnit.HOURS);
//        Duration duration1 = Duration.of(3, ChronoUnit.MINUTES);
//        System.out.println(duration.toHours()); // 3
//        System.out.println(duration1.toMillis()); // 180000


        System.out.println("=============================================");

        LocalDate start = LocalDate.of(2020, 1, 1);
        LocalDate end = LocalDate.of(2024, 3, 30);

        Period between = Period.between(start, end);

        System.out.println(between); // P4Y2M29D
        System.out.println(between.getYears()); // 4
        System.out.println(between.getMonths()); // 2
        System.out.println(between.getDays());  // 29

        Period period = Period.of(1, 2, 3);
        System.out.println(period.getYears()); // 1
        System.out.println(period.getMonths());  // 2
        System.out.println(period.getDays()); // 3

    }

    @Test
    public void test2() {
        // 获取当前世界时间
//        Instant now = Instant.now();
//        System.out.println(now);
//
//        Instant seconds = Instant.ofEpochSecond(1843535056L); // 根据秒数获取世界时间
//        Instant millis = Instant.ofEpochMilli(System.currentTimeMillis()); // 根据毫秒数获取世界时间
//        System.out.println(seconds);
//        System.out.println(millis);
//
//        Instant parse = Instant.parse("2024-01-02T12:32:45Z"); // 根据ISO-8601字符串
//        System.out.println(parse);

        // 将Instant转换成LocalDateTime, 需要时区
//        LocalDateTime localDateTime = LocalDateTime.ofInstant(Instant.now(), ZoneId.systemDefault());
//        System.out.println(localDateTime);
//
//        // 将LocalDateTime转换成Instant
//        Instant instant = localDateTime.atZone(ZoneId.systemDefault()).toInstant();
//        System.out.println(instant);
//        long epochMilli = instant.toEpochMilli();
//        System.out.println(epochMilli);
//        System.out.println(System.currentTimeMillis());

        Instant start = Instant.now();
        for (int i = 0; i < 10000; i++) {
            System.out.print(i);
        }
        System.out.println();
        Instant end = Instant.now();
        Duration between = Duration.between(start, end);
        System.out.println("任务耗时: "+between.toMillis()+"毫秒");
    }

    @Test
    public void test3() {
        ZoneId zoneId = ZoneId.of( "Asia/Shanghai");
        ZoneId zoneId1 = ZoneId.systemDefault();
        ZonedDateTime zonedDateTime = ZonedDateTime.of(2020, 1, 1, 0, 0, 0, 0, zoneId);

        System.out.println("zoneId = " + zoneId);
        System.out.println("zoneId1 = " + zoneId1);
        System.out.println("zonedDateTime = " + zonedDateTime);

        ZoneId zoneId2 = ZoneId.of( "Asia/Shanghai");
        LocalDateTime zonedDateTime1 = LocalDateTime.of(2025, 1, 1, 0, 0, 0, 0);
        ZoneOffset offset = zoneId2.getRules().getOffset(zonedDateTime1);
        System.out.println("offset = " + offset);

        ZoneOffset zoneOffset1 = ZoneOffset.of("+04:00");
        System.out.println("zoneOffset1 = " + zoneOffset1.getTotalSeconds());
    }

    @Test
    public void test4() throws ParseException {
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

        // 格式化
        String str = sdf.format(new Date());
        System.out.println(str); // 2025-08-10 14:35:00

        // 解析
        Date date = sdf.parse("2025-08-10 08:00:00");
        System.out.println(date);

        System.out.println("============================================");

        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

        // 格式化
        String str2 = LocalDateTime.now().format(dtf);
        System.out.println(str2); // 2025-08-10 16:05:52

        // 解析
        LocalDateTime dt = LocalDateTime.parse("2025-08-10 08:00:00", dtf);
        System.out.println(dt); // 2025-08-10T08:00
    }

    @Test
    public void test5() throws IOException {

//        long start = System.nanoTime();
//        long end = System.nanoTime();
//        long l = end - start;
//        System.out.println(l);
//
//        String str = "2025-08-10T08:00";
//        System.err.println(str);
//
//        System.out.println(System.getProperty("java.version"));
//        System.out.println(System.getProperty("os.name"));
//        System.out.println(System.getenv("PATH"));



    }
}
