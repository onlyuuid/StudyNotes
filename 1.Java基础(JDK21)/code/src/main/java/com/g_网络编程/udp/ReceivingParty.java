package com.g_网络编程.udp;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetSocketAddress;
import java.net.SocketException;
import java.nio.charset.StandardCharsets;

/**
 * @author lanxin
 * @version 1.0
 * @description: TODO
 * @date 2025/8/30 23:00
 */
public class ReceivingParty {
    public static void main(String[] args)  {

        /**
         * 接收方
         */
        try (   // 1. 创建接收端socket
                DatagramSocket socket = new DatagramSocket(null)
        ){
            socket.setReuseAddress(true); // 开启端口复用
            socket.bind(new InetSocketAddress(9999)); // 监听端口
            // 2. 创建数据报, 用于接收数据
            byte[] bytes = new byte[1024];
            DatagramPacket packet = new DatagramPacket(bytes, bytes.length);
            System.out.println("等待接收信息...");

            while(true){
                // 3.接收数据(阻塞等待)
                socket.receive(packet);

                // 4.解析数据
                String s = new String(packet.getData(), 0, packet.getLength(), StandardCharsets.UTF_8);
                System.out.println("收到信息: " + s);
                System.out.println("来自: " + packet.getAddress().getHostAddress()+":"+packet.getPort());
            }


        } catch (SocketException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

}
