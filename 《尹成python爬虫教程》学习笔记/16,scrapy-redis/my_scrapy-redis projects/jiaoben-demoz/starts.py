from scrapy import cmdline
from os import system

import redis
r = redis.Redis("127.0.0.1",port=6379,password="yyl1") #连接数据库
print(r.delete("batspider:items"))
print(r.delete("batspider:dupefilter"))

def del_data():
    try:
        system("del data.json")
        print("data文件删除")
    except:
        print("文件删除失败")
# cmdline.execute(["scrapy","crawl","batspider"])
cmdline.execute(["scrapy","crawl","batspider","-o","data.json","-s","FEED_EXPORT_ENCODING=utf-8"])