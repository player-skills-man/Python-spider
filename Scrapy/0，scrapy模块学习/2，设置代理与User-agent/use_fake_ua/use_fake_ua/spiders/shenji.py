# -*- coding: utf-8 -*-
import scrapy
from use_fake_ua.items import UseFakeUaItem

class ShenjiSpider(scrapy.Spider):
    name = 'shenji'
    allowed_domains = ['shenjidaili.com']
    start_urls = ['http://www.shenjidaili.com/open/', ]

    def parse(self, response):
        print(response.request.headers['User-Agent'])
        item = UseFakeUaItem()
        item['country'] = 'China'  # 国家
        trs = response.xpath('//table//tr')[1:]# 切片，去掉thead

        for tr in trs:
            item['ip'] = tr.xpath('./td[1]/text()').get()  # ip地址
            item['port'] = tr.xpath('./td[2]/text()').get()  # 端口
            item['isAnonymous'] = tr.xpath('./td[3]/text()').get()  # 是否高匿
            item['protocol'] = tr.xpath('./td[4]/text()').get()  # 连接协议类型http,https
            item['addr'] = tr.xpath('./td[5]/text()').get()  # 服务器地址
            item['speed'] = tr.xpath('./td[6]/text()').get()  # 连接速度
            yield item

