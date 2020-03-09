# -*- coding: utf-8 -*-
import scrapy
import re
import logging
import time


import logging.handlers
import time
import datetime

# logging初始化工作
logging.basicConfig()

# myapp的初始化工作
myLog = logging.getLogger('myLog')
myLog.setLevel(logging.INFO)

# 添加TimedRotatingFileHandler
# 定义一个1秒换一次log文件的handler
# 保留3个旧log文件
filehandler = logging.handlers.TimedRotatingFileHandler(filename="logs/myLog.log",when='M', interval=5, backupCount=4)
# 设置后缀名称，跟strftime的格式一样  when设置的是S这个结尾必须是S.log
filehandler.suffix = "%Y-%m-%d_%H-%M.log"
myLog.addHandler(filehandler)


class A163spiderSpider(scrapy.Spider):
    name = '163spider'
    allowed_domains = ['yuedu.163.com']
    start_urls = ['http://yuedu.163.com/']

    def parse(self, response):
        while True:
            myLog.error("YYL->hello world")
            time.sleep(60)
        book =response.xpath('//*[@id="identify"]//em/text()').extract()
        if len(book) > 0:
            item = {}
            item['bookName'] = book[0]
            # bookid
            item['bookId'] = re.findall("source/(.+)",response.url)[0]
            # bookURL
            item['bookLink'] = response.url
            # book作者
            item['bookAuthor'] = response.xpath('//*[@id="identify"]//em/following-sibling::span/a/text()').extract()[0]
            yield item
