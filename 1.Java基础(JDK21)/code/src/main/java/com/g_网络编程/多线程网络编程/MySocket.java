package com.g_网络编程.多线程网络编程;

import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;

/**
 * @author lanxin
 * @version 1.0
 * @description: TODO
 * @date 2025/9/1 22:55
 */
public class MySocket {
    @Test
    public void client1(){
      try(    // 创建客户端socket
              Socket socket = new Socket("127.0.0.1", 9999)
      ){
          // 定义发送消息
          String message = "你好";
          PrintWriter writer = new PrintWriter(new OutputStreamWriter(socket.getOutputStream()),true);
          writer.println(message);
      } catch (UnknownHostException e) {
          throw new RuntimeException(e);
      } catch (IOException e) {
          throw new RuntimeException(e);
      }
    }

    @Test
    public void client2(){
        try(    // 创建客户端socket
                Socket socket = new Socket("127.0.0.1", 9999)
        ){
            // 定义发送消息
            String message = "你好,北京";
            PrintWriter writer = new PrintWriter(new OutputStreamWriter(socket.getOutputStream()),true);
            writer.println(message);

        } catch (UnknownHostException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    @Test
    public void client3(){
        try(    // 创建客户端socket
                Socket socket = new Socket("127.0.0.1", 9999)
        ){
            // 定义发送消息
            String message = "你好,世界";
            PrintWriter writer = new PrintWriter(new OutputStreamWriter(socket.getOutputStream()),true);
            writer.println(message);

        } catch (UnknownHostException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
