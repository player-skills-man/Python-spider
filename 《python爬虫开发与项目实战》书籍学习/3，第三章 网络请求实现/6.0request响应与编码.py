# 响应与编码

import requests
r = requests.get('http://www.baidu.com')
print('content-->',r.content) # 打印bytes
print('text-->',r.text) # 打印文本
print('encoding-->',r.encoding) # 打印文本采用的编码格式
r.encoding='utf-8' # 设置新的编码格式'utf-8'
print('new text-->',r.text) # 打印文本