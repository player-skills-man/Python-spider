"""
author:尹业立
time:2019-07-05

按照url='https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
豆瓣所有图书标签列表爬去豆瓣图书数据库

依赖：使用数据库mysql
    host='localhost',
    port=3306,
    user='test',
    passwd='123456',
    db='books',
    charset='utf8'
    插入数据表：book_info
    数据表字段：isbn,title,author,publish,publish_year,score,price,description,img,kind,tag

"""

from get_tags import getTags

def start_spider(href):
    getTags(href)


if __name__ == '__main__':
    url='https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    start_spider(url)