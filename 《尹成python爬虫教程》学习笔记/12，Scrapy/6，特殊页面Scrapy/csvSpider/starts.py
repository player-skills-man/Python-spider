from scrapy import cmdline

# cmdline.execute(["scrapy","crawl","myspider","-o","data/res.csv"])
cmdline.execute(["scrapy","crawl","weatherSpider","-o","data/weather.csv"])