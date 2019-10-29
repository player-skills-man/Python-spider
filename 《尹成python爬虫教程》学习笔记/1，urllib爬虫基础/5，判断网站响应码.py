import urllib.request


URL =  "http://wwww.baidu.com"
def download(url):
    response = urllib.request.urlopen(url)
    print("响应码：",response.code)

download(URL)




