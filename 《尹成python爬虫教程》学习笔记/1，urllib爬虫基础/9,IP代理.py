import urllib.request


URL =  "https://www.sina.com.cn/"


def download(url):
    # httpProxy = urllib.request.ProxyHandler({"http":"192.168.113.1:808"}) # 代理服务器，无需账号
    httpProxy = urllib.request.ProxyHandler({"http": "yyl:123456@127.0.0.1:8080"})# 代理服务器，需账号
    opener = urllib.request.build_opener(httpProxy) # 创建一个打开器，打开代理
    req = urllib.request.Request(url)
    response = opener.open(req) # 打开网页，内置代理服务器
    print(response.read())

download(URL)