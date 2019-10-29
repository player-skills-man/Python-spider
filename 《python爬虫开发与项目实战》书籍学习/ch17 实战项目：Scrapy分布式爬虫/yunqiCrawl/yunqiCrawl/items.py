# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YunqiBookListItem(scrapy.Item):
    # bookid
    novelId = scrapy.Field()
    # book名称
    novelName = scrapy.Field()
    # bookURL
    novelLink = scrapy.Field()
    # book作者
    novelAuthor = scrapy.Field()
    # book类型
    novelType = scrapy.Field()
    # book状态
    novelStatus = scrapy.Field()
    # book更新时间
    novelUpdateTime = scrapy.Field()
    # book字数
    novelWords = scrapy.Field()
    # book封面
    novelImageUrl = scrapy.Field()

class YunqiBookDetailItem(scrapy.Item):
    novelId = scrapy.Field()
    novelLabel  =scrapy.Field()
    novelAllClick = scrapy.Field()
    novelMonthClick = scrapy.Field()
    novelWeekClick = scrapy.Field()
    novelAllPopular = scrapy.Field()
    novelMonthPopular = scrapy.Field()
    novelWeekPopular = scrapy.Field()
    novelCommentNum = scrapy.Field()
    novelAllComm = scrapy.Field()
    novelMonthComm = scrapy.Field()
    novelWeekComm = scrapy.Field()

