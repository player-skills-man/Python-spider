# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider,Request
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time



class TaobaospiderSpider(scrapy.Spider):
    name = 'taobaospider'
    allowed_domains = ['taobao.com']
    start_urls = ['https://login.taobao.com/member/login.jhtml']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.browser = webdriver.Chrome("./tools/chromedriver.exe")
        self.browser.set_page_load_timeout(30)

    def if_spider_closed(self):
        print("爬虫关闭")
        self.browser.close()# 关闭浏览器

    def parse(self, response):
        with open("data/res.html","wb") as f:
            f.write(response.body)

