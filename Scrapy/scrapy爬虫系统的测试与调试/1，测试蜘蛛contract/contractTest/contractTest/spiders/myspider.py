# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy import Request
from contractTest.items import ContracttestItem

class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['chinanews.com']
    start_urls = ['http://www.chinanews.com/rss/rss_2.html', ]

    def parse(self, response):  # 深度1
        rss_page = BeautifulSoup(response.body, "html.parser")
        rss_links = set([item['href'] for item in rss_page.find_all('a')])  # 使用set去重
        # inspect_response(response, self) # 打开了命令行，作用---调试
        for link in rss_links:
            yield Request(url=link, callback=self.parse_feed)

    def parse_feed(self, response):  # 深度2
        '''
        @url http://www.chinanews.com/rss/scroll-news.xml
        @returns items 1 100
        @returns requests 0 0
        @scrapes title link desc pub_date
        :param response:
        :return:
        # 期待返回的items个数1-100
        # 期待返回的requests个数 0-0
        # 期待的scrapes字段，分别是title link desc pub_date
        '''
        rss = BeautifulSoup(response.body, 'lxml')
        for item in rss.find_all('item'):
            feed_item = ContracttestItem()
            feed_item['title'] = item.title.text
            feed_item['link'] = item.link.text
            feed_item['desc'] = item.description.text
            feed_item['pub_date'] = item.pubdate.text
            yield feed_item
