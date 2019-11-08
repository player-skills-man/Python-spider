#coding:utf-8
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import time

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 发送邮件函数
def send_email(from_addr,password,to_addr,txt_head,txt_msg):
    # 163网易邮箱服务器地址
    smtp_server = 'smtp.163.com'

    msg = MIMEText(txt_msg, 'html', 'utf-8')
    msg['Subject'] = Header(txt_head, 'utf-8').encode()
    msg['From'] = _format_addr(from_addr)
    msg['To'] = _format_addr(to_addr)

    #发送邮件
    server = smtplib.SMTP(smtp_server, 25)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    print(to_addr,":seng ok.")
    server.quit()

def send_msg(to_email='Ocean_yyl@163.com',txt_head = '公司邮箱容量异常',txt_msg = '异常'):
    # 发件人地址
    from_addr = 'to_Ocean_yyl@163.com'
    # 邮箱密码
    password = 'yyl123456789'
    # 收件人地址
    to_addr =to_email
    # 设置邮件信息
    txt_head = txt_head
    txt_msg = txt_msg
    send_email(from_addr, password, to_addr, txt_head, txt_msg)

def send_emails():
    # elist = ['2454453499@qq.com', ]
    with open("e-list",encoding="utf-8") as e_f:
        elist = e_f.readlines()
    txt_head = '邮箱管理员：邮箱帐号异常登录提醒'
    with open("./txt_msg/msg_html.html",encoding="utf-8") as f:
        txt_msg = f.read()
    

    for e_addr in elist:
        e_addr = e_addr.strip()
        txt_msg = txt_msg.replace("Ocean_yyl@163.com",e_addr)
        txt_msg = txt_msg.replace("2019-11-08 13:16", str(time.ctime()))

        send_msg(to_email=e_addr,txt_head=txt_head,txt_msg=txt_msg)


if __name__ == '__main__':
    send_emails()
