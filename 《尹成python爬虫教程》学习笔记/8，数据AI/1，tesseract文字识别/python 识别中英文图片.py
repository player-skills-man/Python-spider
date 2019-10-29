"""
识别验证码：2种方法
1,调用AI平台(百度AI等)API
2,使用工具tesseract-OCR
    下载tesseract-OCR。tesseract-OCR下载地址:https://digi.bib.uni-mannheim.de/tesseract/
    配置tesseract环境变量，
    使用cmd命令：tesseract 图片源位置 输出文本位置

验证码图片获取：http://reg.mail.163.com/unireg/call.do?cmd=register.entrance
"""

import subprocess

# 模拟命令行
# 参数：tesseract路径，图片路径，输出路径

# 英文识别
p = subprocess.Popen([r"D:\softwares\tesseract-OCR\tesseract.exe", "en.jpg", "res"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)

p.wait()  # 等待命令执行成功
with open("res.txt") as f:
    print(f.read())

# 中文识别，需要下载tessdata数据(注意版本问题！！！)：
# https://github.com/tesseract-ocr/tessdata
# https://github.com/tesseract-ocr/tessdata_best
# https://github.com/tesseract-ocr/tessdata_fast
# -l datatrained_name 识别非英语
p = subprocess.Popen([r"D:\softwares\tesseract-OCR\tesseract.exe", "1.jpg", "res2", "-l", "chi_sim"],
                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)

p.wait()  # 等待命令执行成功
with open("res2.txt", encoding="utf-8") as f:
    print(f.read())
