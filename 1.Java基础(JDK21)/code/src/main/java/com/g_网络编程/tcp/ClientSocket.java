package com.g_网络编程.tcp;

import java.io.*;
import java.net.*;


/**
 * @author lanxin
 * @version 1.0
 * @description: TODO
 * @date 2025/8/27 21:10
 */
public class ClientSocket {
    /**
     *  socket客户端
     */
    public static void main(String[] args) {
        try (
                Socket socket = new Socket("127.0.0.1",9090);
                PrintWriter writer = new PrintWriter(socket.getOutputStream(),true);
                BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));

        ){
            // 发送数据
            writer.println("你好, 服务器!");

            // 接收数据
            String s = reader.readLine();
            System.out.println("服务器: " + s);

        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
