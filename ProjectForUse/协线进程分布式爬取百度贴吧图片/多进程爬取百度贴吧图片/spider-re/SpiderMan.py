# 爬虫调度器
from URLManager import UrlManager
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from DataOutput import DataOutput
import urllib.parse
import time

from multiprocessing import Pool

# 爬虫调度器
class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()
    def call_steps(self):
        try:
            # 从URL管理器获取新的url
            new_url = self.manager.get_new_url()
            # HTML下载器下载网页
            html = self.downloader.download(new_url)
            # print("debug->len-html=",len(html))
            # HTML解析器抽取网页数据,data 是url-img
            new_urls, data_img_urls = self.parser.parse(new_url, html)
            # 将抽取到url添加到URL管理器中
            self.manager.add_new_urls(new_urls)
            # 数据存储器储存文件,data 是url-img
            for img_url in data_img_urls:
                datas = self.downloader.down_img(img_url)
                self.output.store_img_data_to_jpg(datas)
            print("已经抓取%s个页面" % self.manager.old_url_size())
        except Exception as e:
            print("crawl failed")

    def crawl(self,root_url):
        #添加入口URL
        self.manager.add_new_url(root_url)
        #判断url管理器中是否有新的url，同时判断抓取了多少个url
        while(self.manager.has_new_url() and self.manager.old_url_size()<20):
            pool = Pool(4)
            for i in range(6):
                pool.apply_async(func=self.call_steps)
            pool.close()  # 关闭进程池，不再接受新的进程
            pool.join()  # 主进程阻塞等待子进程的退出


# 构造搜索word新链接
def make_url(word):
    URL = 'http://tieba.baidu.com/f?'
    data = {
        "ie": "utf-8",
        "kw": word
    }
    com_url = URL+(urllib.parse.urlencode(data))
    return com_url

if __name__=="__main__":
    start_time = time.perf_counter()

    spider_man = SpiderMan()
    spider_man.crawl(make_url("鞠婧祎"))

    print("爬虫运行结束，运行时间：",time.perf_counter()-start_time)