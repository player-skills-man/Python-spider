from scrapy import cmdline
from os import system
def del_data():
    try:
        system("del data.json")
        print("data文件删除")
    except:
        print("文件删除失败")
# cmdline.execute(["scrapy","crawl","batspider"])
cmdline.execute(["scrapy","crawl","batspider","-o","data.json","-s","FEED_EXPORT_ENCODING=utf-8"])