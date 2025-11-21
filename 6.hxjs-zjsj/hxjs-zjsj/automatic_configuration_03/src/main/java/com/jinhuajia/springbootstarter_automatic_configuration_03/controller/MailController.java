package com.jinhuajia.springbootstarter_automatic_configuration_03.controller;

import com.jinhuajia.springbootstarter_automatic_configuration_03.config.MyMailProperties;
import jakarta.mail.MessagingException;
import jakarta.mail.internet.MimeMessage;
import lombok.RequiredArgsConstructor;

import org.springframework.core.io.ClassPathResource;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author: WuPeng
 * @description: 邮件发送
 * @date: 2025/2/15 14:18
 */
@RestController
@RequiredArgsConstructor
public class MailController {

    private final JavaMailSender javaMailSender;

    private final MyMailProperties mailProperties;

    /**
     * 邮件发送接口
     */
    @GetMapping("/sendEmail")
    public String sendEmail(@RequestParam("mail") String mail,
                           @RequestParam("text") String text){
        try {
//            sendSimpleMail(mail,text);
            MimeMessage mimeMessage = sendComplexMail(mail, text, "java.png");
            javaMailSender.send(mimeMessage);
        }catch(RuntimeException e){
            return "send mail fail";
        } catch (MessagingException e) {
            throw new RuntimeException(e);
        }
        return "send mail success";
    }

    /**
     * 创建简单邮件发送
     */
    public SimpleMailMessage sendSimpleMail(String mail, String text){
        SimpleMailMessage msg = new SimpleMailMessage();
        msg.setFrom(mailProperties.getFrom());  // 发件人
        msg.setSubject(mailProperties.getSubject()); // 邮件主题
        msg.setText(text);
        msg.setTo(mail);  // 收件人
        javaMailSender.send(msg);
        return msg;
    }

    /**
     * 创建复杂邮件发送
     */
    public MimeMessage sendComplexMail(String mail, String text,String attachmentClassPath) throws MessagingException {
        MimeMessage msg = javaMailSender.createMimeMessage();
        MimeMessageHelper mimeMessageHelper = new MimeMessageHelper(msg, true);
        mimeMessageHelper.setFrom(mailProperties.getFrom());
        mimeMessageHelper.setTo(mail);
        mimeMessageHelper.setSubject(mailProperties.getSubject());
        mimeMessageHelper.setText(text);
        mimeMessageHelper.addAttachment(attachmentClassPath, new ClassPathResource(attachmentClassPath));
        return msg;
    }
}
