"""
https://blog.csdn.net/qq_39138295/article/details/81406991
"""
from urllib import request
from http import cookiejar
import ssl

# 设置忽略SSL验证
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == '__main__':
    """
        #声明一个CookieJar对象实例来保存cookie
        cookie = cookiejar.CookieJar()
        #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
        handler=request.HTTPCookieProcessor(cookie)
    """
    # 保存cookie信息
    filename = 'cookie.txt'
    # 设置cookie保存的文件
    cookie_obj = cookiejar.LWPCookieJar(filename=filename)
    # 创建一个支持cookie的对象，对象属于HTTPCookieProcessor
    cookie_handler = request.HTTPCookieProcessor(cookie_obj)
    # 通过CookieHandler创建opener
    opener = request.build_opener(cookie_handler)
    # 此处的open方法打开网页
    response = opener.open('http://www.baidu.com')

    # 保存cookie到指定的文件当中去
    # ignore_expires=True 即便目标cookie已经在文件中存在，仍然对其写入
    # ignore_discard=True   即便cookie将要/已经过期，仍然写入
    cookie_obj.save(ignore_expires=True, ignore_discard=True)

