# -*- coding: utf-8 -*-
import scrapy

class ApplespiderSpider(scrapy.spiders.SitemapSpider):
    name = 'applespider'
    allowed_domains = ['apple.com']
    sitemap_urls = ['https://www.apple.com/sitemap.xml',]
    sitemap_rules = [
        ("/mac/","parse_mac"),
        ("/iphone","parse_iphone"),
        ("","parse"),
    ] # 一个包含(regex,callback)元组的列表
    '''
    sitemap_follow = [
        
    ]# 一个用于匹配要跟进的sitemap正则表达式列表，其仅仅被应用在使用sitemap index file来指向其他sitemap文件的站点。
    
    sitemap_alternate_links = True  # 指定当一个Url有可选的链接时是否跟进，默认情况下都会跟进。
    '''
    # 不同类型的网址，交给不同的parse处理
    def parse_mac(self, response):
        print("mac处理:",response.url)

    def parse_iphone(self, response):
        print("iphone处理:",response.url)

    def parse(self, response):
        yield {
            "title":response.css("title::text").extract_first(), # 链接页面的title
            "url":response.url # 链接页面的url
        }
