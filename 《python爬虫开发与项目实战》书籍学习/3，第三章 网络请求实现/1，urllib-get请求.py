# urllib.request = urllib2(py2使用)

# 最简单的形式
import urllib.request

response=urllib.request.urlopen('http://www.zhihu.com')

html=response.read()
print(html)

'''
上面对http://www.zhihu.com的请求响应分为两步，一步是请求，一步是响应

import urllib.request

#请求
request=urllib.request.Request('http://www.zhihu.com')
#响应
response = urllib.request.urlopen(request)

html=response.read()
print html

'''