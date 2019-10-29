from urllib import request

URL =  "https://wwww.baidu.com"

def download(url):
    return request.urlopen(url).read() # 读取全部网页

def download2(url):
    return request.urlopen(url).readlines() # 读取每一行的网页数据，压入到列表

def download3(url):
    response = request.urlopen(url) # 网页抽象为文件
    while True:
        line = response.readline() # 读取一行
        if not line:
            break
        print(line)


# print(download(URL))
# print(download2(URL))
download3(URL)

