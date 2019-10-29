from scrapy import cmdline

cmdline.execute(["scrapy","crawl","xici","-o","data/xici.json","-s","FEED_EXPORT_ENCODING=utf-8"])