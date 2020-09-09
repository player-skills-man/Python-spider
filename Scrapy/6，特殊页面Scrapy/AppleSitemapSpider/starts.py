from scrapy import cmdline

cmdline.execute(["scrapy","crawl","applespider","-o","data/res.xml"])