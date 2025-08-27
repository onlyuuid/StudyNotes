package com.g_网络编程;

import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

/**
 * @author lanxin
 * @version 1.0
 * @description: TODO
 * @date 2025/8/26 23:42
 */
public class Main2 {
    public static void main(String[] args) throws IOException {
        // 创建URL对象
        URL url = new URL("https://www.baidu.com:9090?name=李四");

        String protocol = url.getProtocol();  // 获取协议
        String host = url.getHost();          // 获取主机
        int port = url.getPort();             // 获取端口
        String path = url.getPath();          // 获取资源路径
        String query = url.getQuery();        // 获取查询字符串
        String string = url.toString();       // 获取完整URL


        System.out.println("protocol = " + protocol); // https
        System.out.println("host = " + host);         // www.baidu.com
        System.out.println("port = " + port);         // 9090
        System.out.println("path = " + path);         //
        System.out.println("query = " + query);       // name=李四
        System.out.println("string = " + string);     // https://www.baidu.com?name=李四
    }
}
