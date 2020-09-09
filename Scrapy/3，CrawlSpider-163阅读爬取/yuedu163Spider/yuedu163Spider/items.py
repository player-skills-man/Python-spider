# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Yuedu163SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # bookid
    bookId = scrapy.Field()
    # book名称
    bookName = scrapy.Field()
    # bookURL
    bookLink = scrapy.Field()
    # book作者
    bookAuthor = scrapy.Field()
    # book类型
    bookType = scrapy.Field()
    # book状态
    bookStatus = scrapy.Field()
    # book更新时间
    bookUpdateTime = scrapy.Field()
    # book字数
    bookWords = scrapy.Field()
    # book封面
    bookImageUrl = scrapy.Field()
    # book点击量
    bookAllClick = scrapy.Field()
    # book评分人数
    bookCommentNum = scrapy.Field()
    # book评分
    bookCommentScore = scrapy.Field()