# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider


class MyspiderSpider(XMLFeedSpider):
    name = 'myspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/rss/liuyuhaoxy.xml',]
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        item = {}
        #item['url'] = selector.select('url').get()
        #item['name'] = selector.select('name').get()
        #item['description'] = selector.select('description').get()

        item['title'] = selector.select('/rss/channel/item/title/text()').extract()
        item['link'] = selector.select('/rss/channel/item/link/text()').extract()
        # item['description'] = selector.select('/rss/channel/item/description/text()').get()
        item['author'] = selector.select('/rss/channel/item/author/text()').extract()

        # for i in range(len(item['title'])):
        #     print(item['title'][i])
        #     print(item['link'][i])
        #     print(item['author'][i])

        return item
