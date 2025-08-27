package com.g_网络编程;

import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Arrays;

/**
 * @author lanxin
 * @version 1.0
 * @description: TODO
 * @date 2025/8/26 23:18
 */
public class Main {
    public static void main(String[] args) throws UnknownHostException {
//        // 1. 获取本机IP地址
//        InetAddress localHost = InetAddress.getLocalHost();
//        // 2. 获取本机回环地址
//        InetAddress loopbackAddress = InetAddress.getLoopbackAddress();
        // 3. 根据域名获取网络地址
        InetAddress[] baidu = InetAddress.getAllByName("www.baidu.com");
        // 4. 根据域名获取网络地址
        InetAddress gztrc = InetAddress.getByName("www.gztrc.edu.cn");

//        System.out.println("localHost = " + localHost);
//        System.out.println("loopbackAddress = " + loopbackAddress);
        Arrays.stream(baidu).forEach(System.out::println);
        System.out.println("gztrc = " + gztrc);
    }
}
