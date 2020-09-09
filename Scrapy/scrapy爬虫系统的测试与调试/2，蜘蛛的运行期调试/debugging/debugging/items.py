# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class DebuggingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()  # 标题
    link = Field()  # 新闻详情链接
    desc = Field()  # 新闻综述
    pub_date = Field()  # 发布日期
