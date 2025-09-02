package com.g_网络编程.多线程网络编程;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * @author lanxin
 * @version 1.0
 * @description: TODO
 * @date 2025/9/1 22:18
 */
public class MyServerSocket {
    public static void main(String[] args) {
        System.out.println("服务端已启动!");
        int index = 1;
        // 创建服务端socket
        try (ServerSocket serverSocket = new ServerSocket(9999)){
            while (true){
                Socket socket = serverSocket.accept();
                int finalIndex = index;
                // 使用多线程接收连接
                Thread thread = new Thread(() -> {
                    try (
                            // 将字节流转换为字符流
                            BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()))
                    ){
                        String s = br.readLine();
                        System.out.println("服务端"+"("+Thread.currentThread().getName()+")收到消息: "+ s);
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                },"线程"+finalIndex);
                thread.start();
                index++;
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
