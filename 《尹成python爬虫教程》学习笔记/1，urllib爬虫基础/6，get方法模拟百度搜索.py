import urllib.request
from urllib.parse import urlencode,unquote

"""
注意：url连接，编码！英文不编码也可以实现，但为了统一规范，统一编码。
"""

WORD = {"wd":"Python教程"} # 编辑url连接参数字典
print(urlencode(WORD)) # url编码
print(unquote(urlencode(WORD))) # url解码

URL =  "http://wwww.baidu.com"
URL = URL + "/s?"+urlencode(WORD) # 拼接新url

def download(url):
    print("访问url：",url)
    response = urllib.request.urlopen(url)
    print(response.read().decode('utf-8'))


download(URL)