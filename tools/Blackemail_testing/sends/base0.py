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
	msg['From'] = _format_addr(u'管理员<%s>'%from_addr) # 设置发送人姓名
	msg['To'] = _format_addr(to_addr)

	#发送邮件
	server = smtplib.SMTP(smtp_server, 25)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	print(to_addr,":seng ok.")
	server.quit()

def send_msg(to_email='',txt_head = '',txt_msg = ''):
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


def send_emails(e_file,txt_head="",htm_file="",url="http://39.96.166.6/login/"):
	with open(e_file,encoding="utf-8") as e_f:
		elist = e_f.readlines()
	txt_head = txt_head
	with open(htm_file,encoding="utf-8") as f:
		txt_msg = f.read()

	for e_addr in elist:
		url = url+e_addr
		e_addr = e_addr.strip()
		txt_msg_new = txt_msg.replace("Ocean_yyl@163.com",e_addr) # 更换邮箱
		txt_msg_new = txt_msg_new.replace("http://www.baidu.com",url) # 更换url地址
		txt_msg_new = txt_msg_new.replace("2019-11-08 13:16", str(time.ctime())) # other_login

		send_msg(to_email=e_addr,txt_head=txt_head,txt_msg=txt_msg_new)