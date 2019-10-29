# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class FreeproxyscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    country = Field() # 国家
    ip = Field()  # ip地址
    port = Field()  # 端口
    addr = Field() # 服务器地址
    isAnonymous = Field()  # 是否高匿
    protocol = Field()  # 连接协议类型http,https
    speed = Field()  # 连接速度
    connection_time = Field()  # 连接时间
    lifeCircle = Field()  # 存活时间
    validate_time = Field()  # 验证时间
    validated = Field()  # 是否有效（标志位）