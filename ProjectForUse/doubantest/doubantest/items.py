# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubantestItem(scrapy.Item):
    book_name = scrapy.Field()  # 书名
    info = scrapy.Field() # info
