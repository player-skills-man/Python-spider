# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class JiaobenItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field() # 名称
    kind = scrapy.Field() # 类别
    size = scrapy.Field() # 大小
    update_time = scrapy.Field() #更新时间
    desc = scrapy.Field() # 描述