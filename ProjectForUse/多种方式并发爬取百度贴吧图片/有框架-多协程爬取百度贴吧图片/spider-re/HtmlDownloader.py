# html下载器
import requests
from tools.GET_headers import getheaders

# html下载器
class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None

        r = requests.get(url,headers=getheaders())
        if r.status_code==200:
            r.encoding='utf-8'
            return r.text


    def down_img(self, url):
        if url is None:
            return None
        r = requests.get(url,headers=getheaders())
        if r.status_code==200:
            return (r.content)
        else:
            print("图片下载失败，url=",url)

