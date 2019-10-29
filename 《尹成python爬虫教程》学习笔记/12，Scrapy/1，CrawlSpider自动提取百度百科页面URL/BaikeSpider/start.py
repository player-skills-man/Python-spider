from scrapy import cmdline

# cmdline.execute(["scrapy","genspider","ManyPagesBKSpider","baike-mycrawler-redis.baidu.com"])
cmdline.execute(["scrapy","crawl","ManyPagesBKSpider","-o","data/MPres.jl","-s","FEED_EXPORT_ENCODING=utf-8"])
# cmdline.execute(["scrapy","crawl","BKSpider","-o","data/res.json","-s","FEED_EXPORT_ENCODING=utf-8"])