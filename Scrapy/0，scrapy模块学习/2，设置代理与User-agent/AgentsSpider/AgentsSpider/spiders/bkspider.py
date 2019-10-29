# -*- coding: utf-8 -*-
import scrapy
from AgentsSpider.items import AgentsspiderItem

class BkspiderSpider(scrapy.Spider):
    name = 'bkspider'
    allowed_domains = ['baike-mycrawler-redis.baidu.com']
    start_urls = ['https://baike.baidu.com/item/Python']

    def gettitle(self, response):
        h1 = response.xpath('//dd[@class]/h1/text()').extract()
        h2 = response.xpath('//dd[@class]/h2/text()').extract()
        h1.extend(h2)
        return "".join(h1)

    def getcontent(self, response):
        text_list = response.xpath('//div[@class="lemma-summary"]//text()').extract()
        return "".join(text_list).split()

    def geturl(self, response):
        return response.url  # body代表数据，url表示当前链接

    def parse(self, response):
        item = AgentsspiderItem()
        item['kword'] = self.gettitle(response)
        item['url'] = self.geturl(response)
        item['content'] = self.getcontent(response)
        # for i in item:
        #     print(i, item[i])
        yield item
