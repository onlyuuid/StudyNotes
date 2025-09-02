package com.g_网络编程.多线程聊天室;

import java.io.*;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.CopyOnWriteArrayList;

/**
 * @author lanxin
 * @version 1.0
 * @description: TODO  多线程聊天室
 * @date 2025/9/2 21:52
 */
public class ChatServerSocket {
    // 使用线程安全的集合存储所有客户端输出流
    private static CopyOnWriteArrayList<PrintWriter> clients = new CopyOnWriteArrayList<>();
    public static void main(String[] args) {
        System.out.println("服务端已启动!");
        // 服务端socket
        int index = 1;
        try (ServerSocket serverSocket = new ServerSocket()){
            serverSocket.setReuseAddress(true); // 开启端口复用
            serverSocket.bind(new InetSocketAddress(9999));
            while (true){
                Socket socket = serverSocket.accept();
                System.out.println("有新的客户端连接!");

                Thread thread = new Thread(() -> {
                    PrintWriter out = null;
                    try (
                            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                    ){
                        out = new PrintWriter(socket.getOutputStream(), true);
                        clients.add(out);
                        out.println("欢迎加入聊天室! 当前人数: "+clients.size());

                        String message;
                        while ((message = in.readLine()) != null){
                            System.out.println("客户端(" +Thread.currentThread().getName()+"):" + message);
                            // 群发消息
                            for (PrintWriter client : clients) {
                                client.println("客户端(" +Thread.currentThread().getName()+"):" + message);
                            }
                        }
                    } catch (IOException e) {
                        System.out.println("连接断开!");
                    }finally {
                        if (out != null){
                            clients.remove(out);
                            out.close();
                            System.out.println("有客户端下线, 当前人数: "+clients.size());
                            for (PrintWriter client : clients) {
                                client.println("有客户端下线, 当前人数: "+clients.size());
                            }
                        }
                        try {
                            socket.close();
                        } catch (IOException e) {
                            throw new RuntimeException(e);
                        }
                    }
                }, "线程" + index);
                thread.start();
                index++;
            }
        } catch (IOException e) {
            System.out.println("服务端异常关闭");
        }
    }
}
