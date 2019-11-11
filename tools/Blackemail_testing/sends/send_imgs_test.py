#!/usr/bin/env python3
# coding: utf-8
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
from email.utils import parseaddr, formataddr
import os


def get_img_files():
    return ["../txt_msg/imgs/apple.png",]

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def sendmail(filelist):
    sender = 'to_Ocean_yyl@163.com'
    receiver = '2454453499@qq.com'
    password = "yyl123456789"
    smtpserver = 'smtp.163.com'
    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = Header("test imgs sending", 'utf-8').encode()
    msgRoot['From'] = _format_addr(u'管理员<%s>' % sender)  # 设置发送人姓名
    msgRoot['To'] = _format_addr(receiver)
    '''
    图片id加入所在位置 
    '''
    content = '<b>Some <i>HTML</i> text</b> and an image.<br>'
    for index in range(len(filelist)):
        if index % 2 == 0:
            content += '<img src="cid:' + str(index) + '"><br>'
        else:
            content += '<img src="cid:' + str(index) + '">'

    msgText = MIMEText(content, 'html', 'utf-8')
    msgRoot.attach(msgText)

    '''
    将图片和id位置对应起来
    '''
    index = 0
    for file in filelist:
        fp = open(file, 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        msgImage.add_header('Content-ID', '<' + str(index) + '>')
        index += 1
        msgRoot.attach(msgImage)

        # 发送邮件
        server = smtplib.SMTP(smtpserver, 25)
        server.login(sender, password)
        server.sendmail(sender, [receiver], msgRoot.as_string())
        print(receiver, ":seng ok.")
        server.quit()


if __name__ == '__main__':
    sendmail(get_img_files())