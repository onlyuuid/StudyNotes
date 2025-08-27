package com.g_网络编程.tcp;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * @author lanxin
 * @version 1.0
 * @description: TODO
 * @date 2025/8/27 21:09
 */
public class MyServerSocket {

    public static void main(String[] args) {
        /**
         * 服务端socket
         */
        System.out.println("服务端已启动...");
        try (
                ServerSocket serverSocket = new ServerSocket(9090);
        ){

           while(true){
               Socket socket = serverSocket.accept();
               // 读取客服端发送来的数据
               BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
               String s = bufferedReader.readLine();
               System.out.println("客户端: " +s);

               // 向客户端响应连接结果信息
               PrintWriter writer = new PrintWriter(socket.getOutputStream(),true); // 自动flush, 确保消息不会卡在jvm中
               writer.println("连接成功!");

               socket.close();

           }

        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
