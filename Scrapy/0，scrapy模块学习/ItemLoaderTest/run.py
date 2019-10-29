from scrapy import cmdline

cmdline.execute(["scrapy","crawl","CSDNLecturerSpider","-o","data/res.xml"])