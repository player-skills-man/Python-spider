from scrapy import cmdline

cmdline.execute(["scrapy","crawl","shenji","-o","data/proxy.json","-s","FEED_EXPORT_ENCODING=utf-8"])