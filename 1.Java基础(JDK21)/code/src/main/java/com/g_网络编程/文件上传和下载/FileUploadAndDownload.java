package com.g_网络编程.文件上传和下载;

import jakarta.servlet.ServletOutputStream;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.io.*;
import java.nio.ByteBuffer;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;

/**
 * @author lanxin
 * @version 1.0
 * @description: TODO
 * @date 2025/8/29 23:20
 */
@RestController
public class FileUploadAndDownload {

    /**
     * 上传文件
     */
    @CrossOrigin
    @PostMapping("/upload")
    public String upload(@RequestParam("file") MultipartFile file) throws IOException {
        if(file == null || file.isEmpty()){
            return "文件为空";
        }
        String name =  file.getOriginalFilename();
        System.out.println("文件名为: "+name);
        File file1 = Files.createFile(Path.of("D:/1.mp3")).toFile();
        try (
                BufferedInputStream bi = new BufferedInputStream(file.getInputStream());
                BufferedOutputStream bo = new BufferedOutputStream(new FileOutputStream(file1));
        ){
            byte[] bytes = new byte[1024];
            int len;
            while ((len = bi.read(bytes)) != -1){
                System.out.println("bytes = " + Arrays.toString(bytes));
                bo.write(bytes,0,len);
                bo.flush();
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        return "上传成功";
    }

    /**
     * 下载文件
     */
    @CrossOrigin
    @GetMapping("/download")
    public void download(HttpServletResponse response)  {
        // 通过二进制数据下载
        File file = new File("D:/1.mp3");
        response.setContentLengthLong(file.length());
        response.setHeader("Content-Disposition", "attachment;filename=output.mp3");
        response.setContentType("application/octet-stream");
       try (
               FileInputStream fileInputStream = new FileInputStream(file);
               ServletOutputStream outputStream = response.getOutputStream()
            ){
           byte[] bytes = new byte[1024];
           int len = 0;
           while ((len = fileInputStream.read(bytes)) != -1){
               outputStream.write(bytes,0,len);
           }
           outputStream.flush();
           System.out.println("下载完成!");
       }catch (Exception e){
           throw new RuntimeException(e);
       }
    }
}
