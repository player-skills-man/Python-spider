# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 过滤性管道
# 加工性管道
# 存储性管道
from scrapy.exceptions import DropItem
import json
from bs4 import BeautifulSoup



# 过滤性管道---丢弃数据,只要关于“国庆”的news
class BlockGamePipeline:
    def process_item(self, item, spider):
        key = "国庆"
        if key not in item['title']:
            raise DropItem()
        return item

# 过滤性管道---去重
class DuplicatesPipeline:
    def __init__(self):
        self.fingerprints = set()

    def process_item(self, item, spider):
        if  item['title'] not in self.fingerprints:
            self.fingerprints.add(item["title"])
        else:
            raise DropItem()
        return item

# 加工性管道
class CleanHTMLPipeline:
    def add_my_words(self, txt):
        html = BeautifulSoup(txt,"html.parser")
        return html.get_text()+"has been changed by CleanHTMLPipeline"

    def strip_str(self,txt):
        return txt.replace("\n","").replace("\r","").strip()

    def process_item(self, item, spider):
        item['title'] = self.add_my_words(item["title"])
        item['desc'] = self.strip_str(item["desc"])

        return item

# 存储性管道
import codecs
class JsonFeedPipeline:
    def __init__(self):
        self.json_file = codecs.open('data/feed.json', 'w',encoding="utf-8")
        self.json_file.write("[")
    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + ",\n"
        self.json_file.write(line)
        return item


    def close_spider(self, spider):
        self.json_file.write("]\n")
        self.json_file.close()




class PipelinetestPipeline(object):
    def process_item(self, item, spider):
        return item