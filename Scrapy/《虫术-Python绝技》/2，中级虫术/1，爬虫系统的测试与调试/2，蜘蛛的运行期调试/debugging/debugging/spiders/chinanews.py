# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from debugging.items import DebuggingItem
from scrapy import Request

from scrapy.utils.response import open_in_browser
class ChinanewsSpider(scrapy.Spider):
    name = 'chinanews'
    allowed_domains = ['chinanews.com']
    start_urls = ['http://www.chinanews.com/rss/rss_2.html', ]

    def parse(self, response):  # 深度1
        rss_page = BeautifulSoup(response.body, "html.parser")
        rss_links = set([item['href'] for item in rss_page.find_all('a')])  # 使用set去重
        # inspect_response(response, self) # 打开了命令行，作用---调试
        for link in rss_links:
            yield Request(url=link, callback=self.parse_feed)

    def parse_feed(self, response):  # 深度2
        # 如果url中含有字符串“world”，使用浏览器打开这个url
        if "world" in response.url:
            open_in_browser(response) # 虽然我是用notepad打开的？？？
        rss = BeautifulSoup(response.body, 'lxml')
        for item in rss.find_all('item'):
            feed_item = DebuggingItem()
            feed_item['title'] = item.title.text
            feed_item['link'] = item.link.text
            feed_item['desc'] = item.description.text
            feed_item['pub_date'] = item.pubdate.text
            yield feed_item
