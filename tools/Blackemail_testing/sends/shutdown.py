#coding:utf-8
from sends.base0 import send_emails

if __name__ == '__main__':
	send_emails(e_file="../e-list",txt_head = 'Shutdown Request!',htm_file="../txt_msg/shutdown.html")
