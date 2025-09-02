package com.g_网络编程.多线程聊天室;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

/**
 * @author lanxin
 * @version 1.0
 * @description: TODO
 * @date 2025/9/2 22:34
 */
public class ChatSocket2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 定义客户端socket
        try (Socket socket = new Socket("127.0.0.1", 9999)){
            System.out.println("已连接到聊天室!");

            // 接收服务端消息
            new Thread(() -> {
                try (BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))){
                    String messageResp;
                    while ((messageResp = in.readLine()) != null){
                        System.out.println(messageResp);
                    }
                }catch (Exception e){
                    System.out.println("连接断开!");
                }
            }).start();

            PrintWriter out = new PrintWriter(socket.getOutputStream(),true);
            while (true){
                String message = scanner.nextLine();
                if(!"exit".equalsIgnoreCase(message)){
                    out.println(message);
                }else {
                    // 退出聊天室
                    break;
                }
            }
        } catch (IOException e) {
            System.out.println("连接断开!");
        }
        scanner.close();
    }
}
