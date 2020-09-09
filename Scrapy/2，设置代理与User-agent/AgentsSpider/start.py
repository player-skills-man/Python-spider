from scrapy import cmdline

# cmdline.execute(["scrapy","genspider","bkspider","baike-mycrawler-redis.baidu.com"])
cmdline.execute(["scrapy","crawl","bkspider","-o","data/res.xml"])
