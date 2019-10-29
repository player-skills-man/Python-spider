"""
获取豆瓣图书各个分类标签列表的url链接
url=https://book.douban.com/tag/?view=type&icn=index-sorttags-all
"""

"""
    selector：查找规律
    
    #文学 #content > div > div.article > div:nth-child(2) > div:nth-child(1) > a > h2
    #流行 #content > div > div.article > div:nth-child(2) > div:nth-child(2) > a > h2
    

    #文学-小说-外国文学-文学
    #文学-中国文学
    # #content > div > div.article > div:nth-child(2) > div:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(1) > a
    # #content > div > div.article > div:nth-child(2) > div:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(2) > a
    # #content > div > div.article > div:nth-child(2) > div:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(3) > a
    
    # #content > div > div.article > div:nth-child(2) > div:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(1) > a
    # ------------
    #流行-漫画
    # #content > div > div.article > div:nth-child(2) > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(1) > a
    #--------------
    #文化-历史
    # #content > div > div.article > div:nth-child(2) > div:nth-child(3) > table > tbody > tr:nth-child(1) > td:nth-child(1) > a
"""


from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

def get_tags(url):
    tags_html = urllib.request.urlopen(url).read()
    tags_html = bytes.decode(tags_html, encoding="utf-8")
    soup = BeautifulSoup(tags_html, 'lxml')  # 创建CSS选择器
    count_kind=0 # 标签类别初始化
    count_x=0 # 标签x位置初始化
    count_y=0 # 标签y位置初始化
    tag1='' # 标签类别初始化
    tag2='' # 标签初始化
    while True: # 爬去标签类别-》tag1
        count_kind += 1 # 类别 + 1
        e1=soup.select_one("#content > div > div.article > div:nth-child(2) > div:nth-child({}) > a > h2".format(count_kind))
        if e1 is not None: # 种类tag1
            tag1=e1.get_text()
            print(tag1)

            count_y += 1  # y + 1
            while True: # 爬去标签-》tag2
                count_x += 1 # x位置 + 1
                e2= soup.select_one('#content > div > div.article > div:nth-child(2) > div:nth-child({}) > table > tbody > tr:nth-child({}) > td:nth-child({}) > a'.format(count_kind,count_y,count_x))  # css选择器匹配符合条件
                if e2 is not None:
                    # print(e2.get('href')) # info.get['href']也可以
                    tag2=e2.get_text()
                    print(tag2)
                    tag_url='https://book.douban.com'+ urllib.parse.quote(e2.get('href'))
                    # get_books.get_books(tag_url,tag1,tag2)

                else: # x 到 4（or 最大）
                    e2_plus = soup.select_one(
                        '#content > div > div.article > div:nth-child(2) > div:nth-child({}) > table > tbody > tr:nth-child({}) > td:nth-child({}) > a'.format(
                            count_kind, count_y+1, 1))  # css选择器匹配符合条件
                    if e2_plus is not None:  # 下一行有数据，回归 x,y+1
                        count_y += 1  # y+1
                        count_x = 0  # x 回归
                    else:# 下一行没有数据，结束y循环
                        count_y = 0 # y 回归
                        break
        else:
            break




if __name__ == '__main__':
    url='https://book.douban.com/tag/?view=type&icn=index-sorttags-all'
    get_tags(url)
