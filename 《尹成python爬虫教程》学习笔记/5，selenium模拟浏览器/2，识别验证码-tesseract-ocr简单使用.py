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
#参数：tesseract路径，图片路径，输出路径
p = subprocess.Popen([r"D:\softwares\tesseract-OCR\tesseract.exe","./verify_code/1.jpg","res"],
                     stdout=subprocess.PIPE,stderr=subprocess.PIPE)

p.wait()
with open("res.txt") as f:
    print(f.read())
