from scrapy import cmdline

cmdline.execute(["scrapy","crawl","myspider","-o","data/res.xml"])