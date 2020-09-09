# -*- coding: utf-8 -*-
import scrapy
from BaikeSpider.items import BaikespiderItem

from scrapy.spiders import CrawlSpider,Rule # 提取超链接的规则
from scrapy.linkextractors import LinkExtractor # 超链接提取器

class ManypagesbkspiderSpider(CrawlSpider):
    name = 'ManyPagesBKSpider'
    allowed_domains = ['baike-mycrawler-redis.baidu.com']
    start_urls = ['https://baike.baidu.com/item/Python']

    # 根据正则提取超链接,这里仅仅是对url的正则过滤
    page_links = LinkExtractor(allow=(r'/item/.*'),unique=True)
    r = Rule(page_links, callback="parse_item", follow=True)
    # 回调函数处理提取到的链接，follow=True表示一直循环下去
    rules = [r,]
    # 注意:此处要想循环起来，必须修改原来的parse函数函数名,不然循环失败。

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

    def parse_item(self, response):
        item = BaikespiderItem()
        item['kword'] = self.gettitle(response)
        item['url'] = self.geturl(response)
        item['content'] = self.getcontent(response)
        # for i in item:
        #     print(i, item[i])
        yield item