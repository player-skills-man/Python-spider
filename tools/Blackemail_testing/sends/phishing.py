import random
from emails.base0 import send_email
from emails.apple_order import send_emails
import logging
logging.basicConfig(level= logging.DEBUG,#控制台打印的日志级别
                    filename='./logs/send_email.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format='%(asctime)s - %(levelname)s: %(message)s'
                    #日志格式
                    )
"""
随机获取1/3的邮箱
"""
def get_emails(e_file):
    e_list_1_3 = []  # 存储1/3的邮箱
    with open(e_file, encoding="utf-8") as f:
        e_list = f.readlines()

    len_e_list_1_3 = len(e_list) // 3 + 1
    for i in range(len_e_list_1_3):
        e_list_1_3.append(e_list.pop(random.randint(0, len(e_list)-1-i)))

    return e_list_1_3

"""
随机选取钓鱼邮件发送
"""
def sends_random(from_addr,password,email_list):

    for item in email_list:
        randint = random.randint(0,3)
        if 0 == randint:
            send_emails(from_addr,
                        password,
                        txt_head='Apple 确认订单',
                        htm_file="./txt_msg/apple_order.html",
                        e_addr=item.strip())
        elif 1==randint:
            send_email(from_addr,
                       password,
                       txt_head='邮箱管理员：邮箱帐号异常登录提醒',
                       htm_file="./txt_msg/other_login.html",
                       e_addr=item.strip()
                       )
        elif 2 == randint:
            send_email( from_addr,
                        password,
                        txt_head='Shutdown Request!',
                        htm_file="./txt_msg/shutdown.html",
                        e_addr=item.strip()
                        )
        elif 3==randint:
            send_email(from_addr,
                        password,
                        txt_head='邮箱管理员：密码已过期',
                       htm_file="./txt_msg/pwd_out.html",
                       baseurl="http://39.96.166.6/changepwd/",
                       e_addr=item.strip())
        else:
            logging.info("randint > 3")

def get_smtp_account(setting_file_name):
    with open(setting_file_name,encoding="utf-8") as f:
        lines = f.readlines()
    if len(lines) > 1:
        return lines
    else:
        print('account文件配置错误,请尝试如下配置:')
        print('example@163.com\npassword_for_smtp_client')
        return None

# 设置"e-list文件"
if __name__ == '__main__':
    # 读取文件获取smtp账号
    account = get_smtp_account("account")
    from_addr = account[0].strip()
    password = account[1].strip()


    # sends_random(from_addr,password,get_emails("./e-list")) # 发送随机邮件
    # 判断命令函是否有输入邮件列表,默认为e-list,发送邮件
    import sys
    if len(sys.argv) < 2:
        sends_random(from_addr,password,get_emails("./e-list"))
    else:
        try:
            sends_random(from_addr,password,get_emails(sys.argv[1]))
        except Exception as e:
            print('ERROE:',e)
            print('run example: python phishing e-list')
            print('e-list is a file of emails list')