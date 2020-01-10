# encoding=utf-8

import os
from io import StringIO
from io import open
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, process_pdf

# 获取文件列表
def getfiles(path):
    FileList = []
    for home,dirs,files in os.walk(path):
        for filename in files:
            # FileList.append(filename) #文件名列表，只包含文件名
            FileList.append(os.path.join(home, filename)) # 包含完整路径

    return FileList

# 找到字符串
def findStr(str,filelist):
    for file in filelist:
        with open(file,"r",encoding="utf-8",errors="ignore") as f:
            if str in f.read():
                print(file)



def read_pdf(path):
    # resource manager
    with open(path, "rb") as pdf:
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        laparams = LAParams()
        # device
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        process_pdf(rsrcmgr, device, pdf)
        device.close()
        content = retstr.getvalue()
        retstr.close()
        # 获取所有行
        lines = str(content).split("\n")
        return lines


if __name__ == '__main__':
    lines = read_pdf("2.pdf")
    print(lines)

