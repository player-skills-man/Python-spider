#coding:utf-8
from sends.base0 import send_emails

if __name__ == '__main__':
    send_emails(e_file="../e-list",txt_head = '邮箱管理员：邮箱帐号异常登录提醒',htm_file="../txt_msg/other_login.html")
