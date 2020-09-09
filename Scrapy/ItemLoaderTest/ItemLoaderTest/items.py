# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItemloadertestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field
    # 讲师姓名/昵称
    lecturer_name = scrapy.Field()
    # 讲师url
    lecturer_url = scrapy.Field()
    #课程数
    lectures_nums = scrapy.Field()
    #学生数
    stus_nums = scrapy.Field()
    #讲师简介
    desc = scrapy.Field()
    # 爬取时间
    time = scrapy.Field
