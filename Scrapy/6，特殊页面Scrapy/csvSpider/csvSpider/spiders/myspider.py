# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider


class MyspiderSpider(CSVFeedSpider):
    name = 'myspider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    headers = ['name', 'sex', 'addr','email'] # csv头部
    delimiter = ',' # 分割符

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = {}
        i['name'] = row['name']
        i['sex'] = row['sex']
        i['addr'] = row['addr']
        i['email'] = row['email']
        # print("name is"+i['name'])
        #i['url'] = row['url']
        #i['description'] = row['description']
        return i
