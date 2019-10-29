# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule # 提取超链接的规则
from scrapy.linkextractors import LinkExtractor # 超链接提取器
from yuedu163Spider.items import Yuedu163SpiderItem
import re

class MyspiderSpider(CrawlSpider):
    name = 'myspider'
    allowed_domains = ['yuedu.163.com']
    start_urls = ['http://yuedu.163.com/',
                  # 'http://guofeng.yuedu.163.com/rank',
                  ]
    """
        def parse_booklist_urls(self,response):
            booklist_urls = LinkExtractor(allow=(r'/category/.*'))
            rules = [Rule(booklist_urls, callback="parse_booklist_urls", follow=True)]
    """
    # 根据正则提取超链接,这里仅仅是对url的正则过滤
    # unique=True，连接去重
    page_categorys = LinkExtractor(allow=(r'/category/.*'),unique=True)# 图书列表页面
    r1 = Rule(page_categorys,follow=True)
    page_links = LinkExtractor(allow=(r'/source/.*'),unique=True) # 图书详情页面
    r2 = Rule(page_links, callback="parse_book", follow=True)
    # 回调函数处理提取到的链接，follow=True表示一直循环下去
    rules = [r1,r2]
    # 注意:此处要想循环起来，必须修改原来的parse函数函数名,不然循环失败。



    def parse_book(self, response):
        item = Yuedu163SpiderItem()
        # book名称
        book =response.xpath('//*[@id="identify"]//em/text()').extract()
        # 判断是否获取图书名称，可能图书已下架
        if len(book) > 0:
            item['bookName'] = book[0]
            # bookid
            item['bookId'] = re.findall("source/(.+)",response.url)[0]
            # bookURL
            item['bookLink'] = response.url
            # book作者
            item['bookAuthor'] = response.xpath('//*[@id="identify"]//em/following-sibling::span/a/text()').extract()[0]

            # 获取一块区域
            part_info = response.xpath('.//div[@class="m-bookstatus"]')
            # tbody的坑，导致xpath路径找不到！！！不知道原因，但是在xpath路径中不要出现tbody!
            # book状态
            item['bookStatus'] = part_info.xpath('.//table//tr[1]/td[2]//text()').extract()[0].strip()
            # book字数
            item['bookWords'] = part_info.xpath('.//table//tr[2]/td[2]//text()').extract()[0].strip()
            # book点击量
            item['bookAllClick'] = part_info.xpath('.//table//tr[3]/td[2]//text()').extract()[0].strip()
            # book类型
            item['bookType'] = part_info.xpath('.//table//tr[4]/td[2]//text()').extract()[0].strip()
            # book评分人数
            bookCommentNum = part_info.xpath('.//div[@class="starlevel"]/span[2]/text()').extract()[0]
            item['bookCommentNum'] = re.findall('(\d+)人评分',bookCommentNum)[0]
            # book评分
            item['bookCommentScore'] = part_info.xpath('.//div[@class="starlevel"]/span[1]/text()').extract()[0].strip()
            # book封面
            item['bookImageUrl'] =response.xpath('//*[@id="identify"]/a/img/@src').extract()[0]
            # book更新时间
            bookUpdateTime = response.xpath('.//*[@class="updatetime"]/text()').extract()
            if len(bookUpdateTime) > 0:
                item['bookUpdateTime'] = re.findall("更新时间：(.*)",bookUpdateTime[0])[0]

            yield item



