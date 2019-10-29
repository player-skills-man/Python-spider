from scrapy import cmdline
url = 'http://www.chinanews.com/rss/rss_2.html'
url2 = 'http://www.chinanews.com/rss/scroll-news.xml'

#1 查看特定的parse->url爬取的item
# >>> STATUS DEPTH LEVEL 1 <<<...
# cmdline.execute(["scrapy","parse","--spider=chinanews","-c","parse_feed","-d","2",url2])

# >>> STATUS DEPTH LEVEL 2 <<<....
# cmdline.execute(["scrapy","parse","--spider=chinanews","-c","parse","-d","2",url])


#2 使用-v 查看各个层次的状态
cmdline.execute(["scrapy","parse","--spider=chinanews","-c","parse","-d","2","-v",url])
'''
输入如下：
>>> DEPTH LEVEL: 1 <<<
# Scraped Items  ------------------------------------------------------------
[]
# Requests  -----------------------------------------------------------------
[<GET http://www.chinanews.com/rss/sp.xml>,
 <GET http://www.chinanews.com/rss/zgqj.xml>,
 <GET http://www.chinanews.com/rss/world.xml>,
 <GET http://www.chinanews.com/rss/estate.xml>,
 <GET http://www.chinanews.com/rss/edu.xml>,
 <GET http://www.chinanews.com/rss/importnews.xml>,
 <GET http://www.chinanews.com/rss/lxsh.xml>,
 <GET http://www.chinanews.com/rss/ent.xml>,
 <GET http://www.chinanews.com/rss/it.xml>,
 <GET http://www.chinanews.com/rss/stock.xml>,
 <GET http://www.chinanews.com/rss/chinese.xml>,
 <GET http://www.chinanews.com/rss/mil.xml>,
 <GET http://www.chinanews.com/rss/qxcz.xml>,
 <GET http://www.chinanews.com/rss/china.xml>,
 <GET http://www.chinanews.com/rss/society.xml>,
 <GET http://www.chinanews.com/rss/wine.xml>,
 <GET http://www.chinanews.com/rss/hwjy.xml>,
 <GET http://www.chinanews.com/rss/energy.xml>,
 <GET http://www.chinanews.com/rss/sports.xml>,
 <GET http://www.chinanews.com/rss/auto.xml>,
 <GET http://www.chinanews.com/rss/health.xml>,
 <GET http://www.chinanews.com/rss/theory.xml>,
 <GET http://www.chinanews.com/rss/scroll-news.xml>,
 <GET http://www.chinanews.com/rss/fortune.xml>,
 <GET http://www.chinanews.com/rss/gangao.xml>,
 <GET http://www.chinanews.com/rss/taiwan.xml>,
 <GET http://www.chinanews.com/rss/life.xml>,
 <GET http://www.chinanews.com/rss/photo.xml>,
 <GET http://www.chinanews.com/rss/fz.xml>,
 <GET http://www.chinanews.com/rss/finance.xml>,
 <GET http://www.chinanews.com/rss/culture.xml>,
 <GET http://www.chinanews.com/rss/df.xml>]

>>> DEPTH LEVEL: 2 <<<
# Scraped Items  ------------------------------------------------------------
[{'desc': '\r\n'
          '\u3000\u3000'
          '新华社北京10月5日电(记者张泉)国家医保局日前发布的数据显示，全国跨省异地就医住院医疗费用直接结算工作稳步推进，截至2019年8月底，累计结算人次318万。',
  'link': '',
  'pub_date': '2019-10-05 14:58:24',
  'title': '中国跨省异地就医直接结算累计突破300万人次'},
 {'desc': '\r\n'
          '\u3000\u3000中新网苏州10月5日电 (记者 '
          '钟升)5日，苏州阳澄湖上秋风轻拂。蟹农杨忠明驾船来到湖中，从围网里捞出一只只青壳金毛、厚实饱满的大闸蟹。一旁，日本著名零售集团公司永旺的中国商品本部食品部经理钟俊彬露出满意的笑容。这已是永旺第三年在阳澄湖中“养蟹”。',
  'link': '',
  'pub_date': '2019-10-05 14:42:29',
  'title': '日资企业苏州“秋收”忙'},
 {'desc': '\r\n\u3000\u3000随着一系列重大开放举措，我国引资魅力不断增加。',
  'link': '',
  'pub_date': '2019-10-05 12:37:06',
  'title': '“六稳”如何稳 发力显现看这里——外资篇'},
'''
