# -*- coding: utf-8 -*-
import scrapy
import re
import logging

class A163spiderSpider(scrapy.Spider):
    name = '163spider'
    allowed_domains = ['yuedu.163.com']
    start_urls = ['http://yuedu.163.com/']

    def parse(self, response):
        logging.error("YYL->hello world")
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
