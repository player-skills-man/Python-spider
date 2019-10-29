# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider,Rule # 提取超链接的规则
from scrapy.linkextractors import LinkExtractor # 超链接提取器
from ItemLoaderTest.items import ItemloadertestItem

from scrapy.loader.processors import MapCompose

class CsdnlecturerspiderSpider(CrawlSpider):
    name = 'CSDNLecturerSpider'
    allowed_domains = ['edu.csdn.net']
    start_urls = ['https://edu.csdn.net/lecturer?page=1']

    page_categorys = LinkExtractor(allow=('lecturer\?page=\d+'), unique=True)  # 讲师列表页面
    r1 = Rule(page_categorys, follow=True)
    page_links = LinkExtractor(allow=(r'/lecturer/\d+'), unique=True)  # 讲师详情页面
    r2 = Rule(page_links, callback="parse_lector", follow=True)
    # 回调函数处理提取到的链接，follow=True表示一直循环下去
    rules = [r1, r2]
    # 注意:此处要想循环起来，必须修改原来的parse函数函数名,不然循环失败。

    def parse_lector(self, response):
        items = ItemLoader(item=ItemloadertestItem(), response=response)
        # 讲师姓名/昵称
        items.add_xpath('lecturer_name','//*[@class="lector1_name"]//text()')
        # 讲师url
        items.add_value("lecturer_url",response.url)
        # 课程数
        items.add_xpath('lectures_nums', '//*[@class="PubC_tabTit"]/a[1]//text()')
        # 学生数
        items.add_xpath('stus_nums', '//span[@class="fr"]/b/text()')
        # 讲师简介
        items.add_xpath('desc', '//*[@class="lector1_intro "]//text()')
        yield items.load_item()
