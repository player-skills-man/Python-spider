# -*- coding: utf-8 -*-
import scrapy
from ScrapydataToFile.items import ScrapydatatofileItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/Eeyhan/',]

    def parse(self, response):
        papers = response.xpath('//*[@class="forFlow"]/div[@class="day"]')
        for paper in papers:
            url = paper.xpath(".//*[@class='dayTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0]
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postCon']/div/text()").extract()[0]
            # self.log(message=(url+title+time+content))
            # print(url,title,time,content)

            item = ScrapydatatofileItem()
            item['url'] = url
            item['title'] = title
            item['time'] = time
            item['content'] = content
            yield item


            # request = scrapy.Request(url=url, callback=self.parse_body)
            # request.meta['item'] = item  # 将item暂存
            # yield request
        # next_page = Selector(response).re(u'<a href="(\S*)">下一页</a>')
        # if next_page:
        #     yield scrapy.Request(url=next_page[0], callback=self.parse)

