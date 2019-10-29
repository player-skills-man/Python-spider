# -*- coding: utf-8 -*-
import scrapy
from ImageSpider.items import ImagespiderItem

class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/qiyeboy/p',]

    def parse(self, response):
        papers = response.xpath('//div[@class="postTitl2"]/a')
        for p in papers:
            title = p.xpath('./text()').extract()[0]
            url = p.xpath('./@href').extract()[0]
            item = ImagespiderItem()
            item['title'] = title
            item['url'] = url

            request = scrapy.Request(url=url,callback=self.parse_body) # 使用Request回调另一个解析函数
            request.meta["item"] = item # 将item暂存
            yield request

        # 实现翻页
        next_pages = response.xpath("") # 抽取新页面链接
        if next_pages:
            for next_page in next_pages:
                yield scrapy.Request(url=next_page,callback=self.parse)


    def parse_body(self,response):
        item = response.meta["item"]
        body = response.xpath('.//*[@class="postBody"]')
        item["img_urls"] = body.xpath('.//img/@src').extract() # 提取图片链接
        yield item


