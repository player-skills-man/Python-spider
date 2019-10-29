import os
PATH = r"C:\Users\admin\Desktop\yyl-docs\pycharm\Python-spider\READCODE\scrapyd"
STR_YOU_WANT = "schedule.json"
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

if __name__ == '__main__':
    filelist = getfiles(PATH)
    findStr(STR_YOU_WANT,filelist)