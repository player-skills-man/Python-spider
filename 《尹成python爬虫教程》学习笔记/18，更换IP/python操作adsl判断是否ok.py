import os
adslname = "宽带连接"
username = "account"
password = "123456"

def conn():
    # os.popen（）可以返回命令执行的结果
    pipe = os.popen("rasdial %s %s %s"%(adslname,username,password))
    text = pipe.read()
    # print(text)
    if text.find("正在连接")!= -1 and text.find("命令已完成") != -1:
        print("连接成功！")

    elif text.find("您已连接") != -1 and text.find("命令已完成") != -1:
        print("---已经连接。")
        pass
    else:
        print("连接失败...")


if __name__ == '__main__':
    conn()