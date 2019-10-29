import urllib.request

URL =  "https://www.sina.com.cn/"
httpHandler = urllib.request.HTTPHandler(debuglevel=1) # 设置调试级别。访问网络，输出调试信息
httpsHandler = urllib.request.HTTPSHandler(debuglevel=1) # 设置调试级别。访问网络，输出调试信息

opener = urllib.request.build_opener(httpHandler,httpsHandler) # 可以处理http和https
urllib.request.install_opener(opener) # 全局生效

response = urllib.request.urlopen(URL)