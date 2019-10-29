"""
https://blog.csdn.net/qq_39138295/article/details/81406991
"""

from http.cookiejar import CookieJar,LWPCookieJar
from urllib.request import Request,urlopen,HTTPCookieProcessor,build_opener

cookie = LWPCookieJar()
# 从文件中读取cookie到变量
cookie.load('cookie.txt')

request = Request('http://www.baidu.com')
# 创建一个支持cookie的对象，对象属于HTTPCookieProcessor
cookie_handler = HTTPCookieProcessor(cookie)
# 创建一个opener
opener = build_opener(cookie_handler)
# 请求网页
response = opener.open(request)

print(response.status)