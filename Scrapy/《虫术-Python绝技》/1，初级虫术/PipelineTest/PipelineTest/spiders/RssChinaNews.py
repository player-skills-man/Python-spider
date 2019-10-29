# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from PipelineTest.items import PipelinetestItem
from bs4 import BeautifulSoup
from scrapy.shell import inspect_response

class RsschinanewsSpider(scrapy.Spider):
    name = 'RssChinaNews'
    allowed_domains = ['chinanews.com']
    start_urls = ['http://www.chinanews.com/rss/rss_2.html',]

    def parse(self, response): # 深度1
        rss_page = BeautifulSoup(response.body, "html.parser")
        rss_links = set([item['href'] for item in rss_page.find_all('a')]) # 使用set去重
        # inspect_response(response, self) # 打开了命令行，作用---调试
        for link in rss_links:
            yield Request(url=link, callback=self.parse_feed)

    def parse_feed(self, response):# 深度2
        rss = BeautifulSoup(response.body, 'lxml')
        for item in rss.find_all('item'):
            feed_item = PipelinetestItem()
            feed_item['title'] = item.title.text
            feed_item['link'] = item.link.text
            feed_item['desc'] = item.description.text
            feed_item['pub_date'] = item.pubdate.text
            yield feed_item
