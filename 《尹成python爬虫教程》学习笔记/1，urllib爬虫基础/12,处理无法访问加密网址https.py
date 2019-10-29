import urllib.request
import ssl

"""
# 两步解决
# 1. 导入Python SSL处理模块
import ssl
# 2. 表示忽略未经核实的SSL证书认证
ssl._create_default_https_context = ssl._create_unverified_context

"""

ssl._create_default_https_context = ssl._create_unverified_context
URL =  "https://www.python.org"
def download(url):
    response = urllib.request.urlopen(url)
    print("响应码：",response.code)

download(URL)

