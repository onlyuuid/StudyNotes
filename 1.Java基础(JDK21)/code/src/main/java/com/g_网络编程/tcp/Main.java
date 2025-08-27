package com.g_网络编程.tcp;

import java.io.IOException;
import java.net.ServerSocket;

/**
 * @author lanxin
 * @version 1.0
 * @description: TODO
 * @date 2025/8/27 22:31
 */
public class Main {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(9090);
        serverSocket.close();
    }
}
