import scrapy
import scrapy.selector
from cnblogSpider.items import CnblogspiderItem
from scrapy import Selector


class CnblogSpider(scrapy.Spider):
    name = "cnblog_spider" # 爬虫的名称
    allowed_domains = ["cnblogs.com"] # 域名范围
    start_urls = [
        "http://www.cnblogs.com/qiyeboy/default.html?page=1",
    ]

    def parse(self, response):
        # 实现网页解析
        papers = response.xpath(".//*[@class='day']") # 抽取所有文章栏目

        # 从每个文章栏目中抽取数据
        for paper in papers:
            url = paper.xpath(".//*[@class='postTitle']/a/@href").extract()[0]
            title = paper.xpath(".//*[@class='postTitle']/a/text()").extract()[0].split()
            time = paper.xpath(".//*[@class='dayTitle']/a/text()").extract()[0]
            content = paper.xpath(".//*[@class='postCon']/div/text()").extract()[0].split()
            item = CnblogspiderItem(url=url,title=title,time=time,content=content)
            yield item

        # 获取下一页链接，翻页
        next_page = Selector(response).re('<a href="(\S*)">\s*下一页\s*</a>')
        if next_page:
            yield scrapy.Request(url=next_page[0], callback=self.parse)