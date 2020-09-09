# -*- coding: utf-8 -*-
import scrapy


class RrcookiespiderSpider(scrapy.Spider):
    name = 'rrcookiespider'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/242245656/profile']  # 登录的url

    """
    人人网与登录有关的一个cookie是：
    "t":"a78bef053dd62a7124a5e71fbcfbc96a6",
    """
    # 注意cookie的时效性！！！cookie是会过期的！
    cookies = {
        "t":"a78bef053dd62a7124a5e71fbcfbc96a6",
    }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.FormRequest(url,cookies=self.cookies,callback=self.parse_new_page)

    def parse_new_page(self,response):# 写入文件
        with open("yinicheng.html","wb") as f:
            f.write(response.body)