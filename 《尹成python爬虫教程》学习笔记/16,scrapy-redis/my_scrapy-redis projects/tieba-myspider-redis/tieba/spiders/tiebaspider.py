# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

class TiebaspiderSpider(RedisSpider):
    name = 'tiebaspider'
    # allowed_domains = ['tieba.baidu.com']
    redis_key = 'tiebaspider:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(TiebaspiderSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }

