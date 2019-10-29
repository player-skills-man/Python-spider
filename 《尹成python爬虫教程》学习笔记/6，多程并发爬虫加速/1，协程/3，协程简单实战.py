import gevent
import gevent.monkey
gevent.monkey.patch_all() # 自动切换

import requests
import time
import random
import lxml
from lxml import etree


def get_page_title(url,title_list):
    txt = requests.get(url).text
    time.sleep(random.randint(1,5))
    html = etree.HTML(txt)
    title_list.extend(html.xpath('//*[@id="wrapper"]/h1/span/text()'))
    print(title_list)

# ['从一到无穷大', '沉睡者', '破碎海岸', '猎人']
# ['沉睡者', '猎人', '破碎海岸', '从一到无穷大']

if __name__ == '__main__':
    title_list = []
    url_list = [
        'https://book.douban.com/subject/33658595/',
        'https://book.douban.com/subject/34782541/',
        'https://book.douban.com/subject/30464121/',
        'https://book.douban.com/subject/33455193/'
    ]
    # gevent.joinall([gevent.spawn(get_page_title, url,title_list) for url in url_list])
    for url in url_list:
        gevent.spawn(get_page_title(url,title_list))
    # print(title_list)