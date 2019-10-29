from PIL import Image
import pytesseract.pytesseract
import subprocess
"""
相比于命令行，使用pytesseract模块的好处：
    1，只需要只当pytesseract.exe,不需要输入命令行参数
    2，需要的特定的参数（训练数据集），由函数封装。
    3，不必输出到文件
"""

# 设置tesseract.exe路径
pytesseract.pytesseract.tesseract_cmd = r"D:\softwares\tesseract-OCR\tesseract.exe"

# 英文识别
#打开图片
imge = Image.open("en.jpg")
# 输出识别结果
print(pytesseract.pytesseract.image_to_string(imge))

print("-----------------------------------------------")

# 中文识别
imge2 = Image.open("1.jpg")
#lang= 设置训练好的数据集
print(pytesseract.pytesseract.image_to_string(imge2,lang="chi_sim"))