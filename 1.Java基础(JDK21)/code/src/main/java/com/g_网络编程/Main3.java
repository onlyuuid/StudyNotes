package com.g_网络编程;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;

/**
 * @author lanxin
 * @version 1.0
 * @description: TODO
 * @date 2025/8/27 0:15
 */
public class Main3 {
    public static void main(String[] args) throws MalformedURLException {
        URL url = new URL("https://www.baidu.com");
        URLConnection urlConnection = null;
//        HttpURLConnection httpURLConnection = null;
        File file = new File("3.html");
        InputStream inputStream;
        FileOutputStream fileOutputStream;
        try {
            urlConnection = url.openConnection();
            /**
             * 可以将URLConnection转为HttpURLConnection，以使用http特有功能
             */
//          httpURLConnection = (HttpURLConnection) url.openConnection();
            urlConnection.connect();
            inputStream = urlConnection.getInputStream();
            fileOutputStream = new FileOutputStream(file);
            byte[] bytes = new byte[1024];
            int len = 0;
            while((len = inputStream.read(bytes)) != -1){
                fileOutputStream.write(bytes,0,len);
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        try {
            fileOutputStream.close();
            inputStream.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
