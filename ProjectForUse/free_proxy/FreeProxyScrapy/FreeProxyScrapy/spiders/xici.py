# -*- coding: utf-8 -*-
import scrapy
from FreeProxyScrapy.items import FreeproxyscrapyItem
from scrapy.shell import inspect_response
class XiciSpider(scrapy.Spider):
    name = 'xici'
    allowed_domains = ['xicidaili.com']
    start_urls = [
        'https://www.xicidaili.com/nn/', # 高匿名
        'https://www.xicidaili.com/nt/', # 普通
        'https://www.xicidaili.com/wn/', # HTTPS
        'https://www.xicidaili.com/wt/' # http
        ]
    # start_urls = ["https://www.xicidaili.com/nn/"+ str(i+1) for i in range(1)]


    def parse(self, response):
        item = FreeproxyscrapyItem()

        # item['country'] = response.xpath('your_xpath').extract()[0]  # 国家
        item['country'] = 'China'
        lines = response.xpath('//table//tr') # a line
        # inspect_response(response, self)  # 打开了命令行，作用---调试
        lines  = lines[1:] # 去掉theader一行
        for line in lines:
            # print(line)
            item['ip'] = line.xpath('./td[2]/text()').get()  # ip地址
            item['port'] = line.xpath('./td[3]/text()').get()  # 端口
            item['addr'] = line.xpath('./td[4]/a/text()').get()  # 服务器地址
            item['isAnonymous'] = line.xpath('./td[5]/text()').get()  # 是否高匿
            item['protocol'] = line.xpath('./td[6]/text()').get()  # 连接协议类型http,https
            item['speed'] = line.xpath('./td[7]/div/@title').get()  # 连接速度
            item['connection_time'] = line.xpath('./td[8]/div/@title').get()  # 连接时间
            item['lifeCircle'] = line.xpath('./td[9]/text()').get()  # 存活时间
            item['validate_time'] = line.xpath('./td[10]/text()').get()  # 验证时间
            # item['validated'] = line.xpath('your_xpath').extract()[0]  # 是否有效（标志位）
            # 验证是否有效到pipline中去验证
            yield item


