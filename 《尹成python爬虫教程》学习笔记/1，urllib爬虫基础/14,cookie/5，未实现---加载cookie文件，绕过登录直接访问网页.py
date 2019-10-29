#  requests 与 http.cookiejar相结合使用

import requests
import http.cookiejar as HC

session = requests.session()
session.cookies = HC.LWPCookieJar(filename='cookie.txt')
#  如果存在cookies文件，则加载，如果不存在则提示
try:
    session.cookies.load(ignore_discard=True)
except:
    print('未找到cookies文件')

URL = 'http://www.renren.com/242245656/profile'
html = requests.get(URL, verify=False)
print(html.content.decode("utf-8"))

session.cookies.save()
