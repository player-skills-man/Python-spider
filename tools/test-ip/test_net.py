# encoding=utf-8
from em2me import send_1
from datetime import datetime
import time
import requests
import logging
logging.basicConfig(level= logging.ERROR,#控制台打印的日志级别
                    filename='./logs/error_net.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format='%(asctime)s - %(levelname)s: %(message)s'
                    #日志格式
                    )

# 每n秒执行一次
def timer(n):
    while True:
        time.sleep(n)
        try:
            code1 = requests.get("https://www.facebook.com",timeout=3).status_code
            code2 = requests.get("https://www.google.com",timeout=3).status_code
            code3 = requests.get("https://www.youtube.com",timeout=3).status_code
            if 200 == code1 and 200 == code2 and 200 == code3:
                logging.info("ok!")
            else:
                send_1()
                logging.error(code1+","+code2+","+code3)
        except Exception as e:
            send_1()
            logging.error(e)

if __name__ == '__main__':
    # 5s
    timer(5)
