# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider


class WeatherspiderSpider(CSVFeedSpider):
    name = 'weatherSpider'
    allowed_domains = ['sinaapp.com']
    start_urls = ['http://beijingair.sinaapp.com/data/beijing/all/20191004/csv']
    # headers的设置，必须要与原csv文件head_line完全一致，必须要全部！
    # 否则会解析错误。
    headers = ["date","hour","type","东四","天坛","官园",
               "万寿西宫","奥体中心","农展馆","万柳","北部新区","植物园",
               "丰台花园","云岗","古城","房山","大兴","亦庄","通州","顺义",
               "昌平","门头沟","平谷","怀柔","密云","延庆","定陵","八达岭",
               "密云水库","东高村","永乐店","榆垡","琉璃河","前门","永定门内",
               "西直门北","南三环","东四环"]
    delimiter = ','

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = {}
        #i['url'] = row['url']
        #i['name'] = row['name']
        #i['description'] = row['description']
        i['dat'] = row['date']
        i['hour'] = row['hour']
        i['type'] = row['type']
        i['西直门北'] = row['西直门北']
        return i
