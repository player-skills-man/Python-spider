# -*- coding: utf-8 -*-
import scrapy

# scrapy 提供的正统的模拟登录方法-->只有在密码加密方法在客户端的时候有效。
class RrloginspiderSpider(scrapy.Spider):
    name = 'rrloginspider'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/SysHome.do'] # 登录的url


    def parse(self, response):
        # scrapy 自动模拟js加密
        formdata = {"email": "yincheng5201314@163.com", "password": "tsinghua"}
        yield scrapy.FormRequest.from_response(response,
                                               formdata=formdata,
                                               callback = self.parse_page)

    def parse_page(self,response):
        url = "http://www.renren.com/242245656/profile"
        yield scrapy.Request(url,callback=self.parse_new_page)

    def parse_new_page(self,response):# 写入文件
        with open("yinicheng.html","wb") as f:
            f.write(response.body)