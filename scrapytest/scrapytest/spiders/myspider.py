# -*- coding: utf-8 -*-
import scrapy

class forkHeart():
    def test(self):
        yield scrapy.Request("http://www.douban.com")


class MyspiderSpider():
    name = 'myspider'
    allowed_domains = ['douban.com']
    start_urls = ['http://www.douban.com/']

    def start_requests(self):
        yield scrapy.Request("http://www.douban.com",callback=self.parse)


    def parse(self, response):
        print(response.text)
        yield {"code:":response.status}
