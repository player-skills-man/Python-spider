# -*- coding: utf-8 -*-
import scrapy


class DatawashuseitemloaderSpider(scrapy.Spider):
    name = 'DataWashUseItemLoader'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://cnblogs.com/']

    def parse(self, response):
        pass
