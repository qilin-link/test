#!/usr/bin/env python
#_*_ coding:utf-8 _*_
#发邮件的库
import smtplib
#邮件文本
from email.mime.text import MIMEText 

#SMTP服务器
SMTPServer = 'smtp.163.com'
#发邮件的地址
sender = 'qi_lin18@163.com'
#发送者邮箱设置的授权密码
passwd = 'xxxxxxxx'

#设置发送的内容
message = 'This e-mail is a test mail.'
#转换成邮件文本
msg = MIMEText(message)
#标题
msg['Subject'] = '本机测试邮件'
#发送者
msg['From'] = sender

#创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer, 25)
#登录邮箱
mailServer.login(sender, passwd)
#发送邮件
mailServer.sendmail(sender, ['qi_lin18@163.com'], msg.as_string())
#退出邮箱
mailServer.quit()



