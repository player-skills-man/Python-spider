# 检测是否发生了重定向动作

import urllib.request
response = urllib.request.urlopen('http://www.zhihu.cn')
isRedirected = response.geturl() == 'http://www.zhihu.cn'
print(not isRedirected)

'''
urllib默认情况下会针对HTTP 3XX返回码自动进行重定向动作。
如果不想自动重定向，可以自定义HTTPRedirectHandler 类，如下：

import urllib2
class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        result = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        result.status = code
        result.newurl = result.geturl()
        return result
opener = urllib2.build_opener(RedirectHandler)
opener.open('http://www.zhihu.cn')
'''