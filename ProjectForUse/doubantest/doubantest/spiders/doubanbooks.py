# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from doubantest.items import DoubantestItem

class DoubanbooksSpider(CrawlSpider):
    name = 'doubanbooks'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/?view=type&icn=index-sorttags-all',]
    page_categorys = LinkExtractor(allow=(r'/tag/.*'), unique=True)  # 图书类别列表页面
    r1 = Rule(page_categorys, follow=True)
    page_links = LinkExtractor(allow=(r'/book.douban.com/subject/\d+/'), unique=True)  # 图书详情页面
    r2 = Rule(page_links, callback="parse_book", follow=True)
    rules = (r1,r2)

    def parse_book(self, response):
        item = DoubantestItem()
        item['book_name'] = response.xpath('//h1/span/text()').get()  # 书名
        info_list = response.xpath('//div[@id="info"]//text()')  # book info
        info = ""
        for infoline in info_list:
            info += infoline.get().strip()
            info += " "
        item['info'] = info
        yield item
