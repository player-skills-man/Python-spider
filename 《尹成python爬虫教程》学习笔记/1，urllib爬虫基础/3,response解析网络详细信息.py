import urllib.request

URL =  "http://wwww.baidu.com"

def download(url):
    response = urllib.request.urlopen(url,timeout=5) # 设置请求响应超时时间5s
    print(type(response))
    print("-----------------")
    print(response.info()) # info()包含了网络请求的详细信息

try:
    download(URL)
except :
    print("web error")