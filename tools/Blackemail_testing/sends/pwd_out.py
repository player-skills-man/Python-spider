#coding:utf-8
from sends.base0 import send_emails

if __name__ == '__main__':
	send_emails(e_file="../e-list",txt_head = '邮箱管理员：密码已过期',htm_file="../txt_msg/pwd_out.html",
				baseurl="http://39.96.166.6/changepwd/")
