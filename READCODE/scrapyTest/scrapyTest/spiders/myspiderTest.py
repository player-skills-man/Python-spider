# -*- coding: utf-8 -*-
import scrapy


class MyspidertestSpider(scrapy.Spider):
    name = 'myspiderTest'
    allowed_domains = ['runoob.com']
    start_urls = ['http://www.runoob.com/']

    def parse(self, response):
        datas = response.xpath('//*[@class="design"]/div//text()').extract()
        for data in datas:
            yield {"data"+str(datas.index(data)):data}
