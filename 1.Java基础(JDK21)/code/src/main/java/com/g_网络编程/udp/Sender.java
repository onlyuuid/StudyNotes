package com.g_网络编程.udp;

import java.io.IOException;
import java.net.*;

/**
 * @author lanxin
 * @version 1.0
 * @description: TODO
 * @date 2025/8/30 22:59
 */
public class Sender {


    public static void main(String[] args) {
        /**
         * 发送方
         */
        try (
                // 1.创建发送端socket, 系统会随机分配一个端口
                DatagramSocket socket = new DatagramSocket()
        ){
            socket.setBroadcast(true); // 开启广播
            String content = "局域网广播消息！"; // 发送的数据
            int port = 9999;          // 接收方端口

            //  2.封装报文信息
            DatagramPacket datagramPacket = new DatagramPacket(content.getBytes(),
                                                                    content.getBytes().length,
                                                                    InetAddress.getByName("255.255.255.255"),
                                                                    port);
            // 3. 发送报文信息
            socket.send(datagramPacket);
            System.out.println("消息已发送!");

        } catch (SocketException e) {
            throw new RuntimeException(e);
        } catch (UnknownHostException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
