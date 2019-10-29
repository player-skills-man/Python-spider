# -*- coding: utf-8 -*-
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider


# 向url递进
from scrapy_redis.spiders import RedisMixin
from scrapy.spiders import CrawlSpider

class BaikespiderSpider(RedisCrawlSpider):
    name = 'baikespider'
    redis_key = 'baikecrawler:start_urls'

    rules = (
        # follow all links
        Rule(LinkExtractor(allow=r"/item/.*"), callback='parse_page', follow=True),
    )

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('baike.baidu.com', '') # 相当于allowed_domains = ['baike.baidu.com'，]
        self.allowed_domains = filter(None, domain.split(','))
        super(BaikespiderSpider, self).__init__(*args, **kwargs)

    ###重要！！！
    def set_crawler(self, crawler):
        CrawlSpider.set_crawler(self,crawler) # 设置默认爬取
        RedisMixin.setup_redis(self) # url由reids

    def parse_page(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }