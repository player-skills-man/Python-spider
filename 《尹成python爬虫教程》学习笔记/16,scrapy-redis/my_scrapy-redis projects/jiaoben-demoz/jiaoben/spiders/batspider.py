# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from jiaoben.items import JiaobenItem

class BatspiderSpider(CrawlSpider):
    name = 'batspider'
    allowed_domains = ['jb51.net']
    start_urls = ['https://www.jb51.net/bat/']

    rules = [
        Rule(LinkExtractor(
           restrict_xpaths=('//div[@class="plist"]//a[5]')
        ), callback='parse_directory', follow=True),
    ]

    def parse_directory(self, all_response):
        response_lis = all_response.xpath('.//ul[@id="list_ul_more"]/li')
        for response in response_lis:
            item = JiaobenItem()
            item['name'] = response.xpath('./div[1]/p//text()').get()  # 名称
            item['kind'] = response.xpath('.//div[@class="rinfo"]//span[@class="intro"]/a/text()').get() # gb2312->utf-8  # 类别
            item['size'] = response.xpath('.//div[@class="rinfo"]//span[2]/text()').get()  # 大小
            item['update_time'] = response.xpath('.//div[@class="rinfo"]//span[3]/text()').get()  # 更新时间
            item['desc'] = response.xpath('.//div[@class="rinfo"]/p[@class="desc"]//text()').get()  # 描述
            yield item