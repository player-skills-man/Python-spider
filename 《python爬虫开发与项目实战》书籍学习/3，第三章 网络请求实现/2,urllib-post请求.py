# POST请求
import urllib.request
import urllib.parse
url = 'http://www.xxxxxx.com/login'
postdata = {'username' : 'qiye',
           'password' : 'qiye_pass'}
#postdata 需要被编码为urllib能理解的格式
data = urllib.parse.urlencode(postdata)
req = urllib.request.Request(url, data) # 请求，加入data
response = urllib.request.urlopen(req)  # 响应
html = response.read()