import urllib.request
import urllib.parse
import json
# post 方法，传递json数据

URL =  "http://wwww.baidu.com"
def download(url):
    data = {'number': '123456'}
    data = json.dumps(data)
    # POST data should be bytes or an iterable of bytes. It cannot be of type str.
    data = bytes(data, 'utf8')
    print(data)
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request,data=data)
    html = response.read()
    print(html.decode('utf-8'))


download(URL)