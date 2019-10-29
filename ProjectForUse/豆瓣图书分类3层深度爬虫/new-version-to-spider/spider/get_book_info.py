"""
读取豆瓣图书详情链接文件，爬去图书详细信息\
"""

from bs4 import BeautifulSoup
import urllib.request
import pymysql
import re
import sqlite3
import random

conn = sqlite3.connect('D:\swProject\pyCharm\webDjango\db.sqlite3')

NUM = 1
database_name = 'webapp_bookinfo'
# 连接数据库mysql
"""
connect = pymysql.connect(
    # localhost连接的是本地数据库
    host='localhost',
    # mysql数据库的端口号
    port=3306,
    # 数据库的用户名
    user='test',
    # 本地数据库密码
    passwd='123456',
    # 表名
    db='bookstore',
    # 编码格式
    charset='utf8'
)
print("连接数据库成功！")
# 2. 创建一个游标cursor, 是用来操作表。
cursor = connect.cursor()
"""

#href 标签链接 tag1 种类 tag2 标签
def getBookInfo(href,tag1,tag2):

    # print(href)
    try:
        html = urllib.request.urlopen(href,timeout=5).read()
        html = bytes.decode(html,encoding="utf-8")
        # print(html)
        soup = BeautifulSoup(html, 'lxml')  # 创建CSS选择器
        info = soup.select_one('#info')  # css选择器匹配符合条件
        str_info = ''
        for child in info.children:
            if (child.string != None):
                str_info += str(child.string.strip())+";"
        info_list = str_info.split(';')
        for i in range(info_list.count('')): # 获取列表中的''项
            info_list.remove('') # 删除列表中的''项

        str_re = str(info_list)
        # print(str_re)
        # htmlfile.close()# 关闭本地文件

        author = re.findall(r"作者:', '(.+?)'", str_re)  # 获取信息---作者
        if (len(author)>0):
            author = author[0]
        # print(author)
        publish = re.findall(r"出版社:', '(.+?)'", str_re) # 获取信息---出版社
        if (len(publish)>0):
            publish = publish[0]
        publish_year = re.findall(r"出版年:', '(.+?)'", str_re)  # 获取信息---出版年
        if (len(publish_year)>0):
            publish_year = publish_year[0]
        price = re.findall(r"定价:', '(.+?)'", str_re)  # 获取信息---定价
        if (len(price)>0):
            price = price[0]
        isbn = re.findall(r"ISBN:', '(.+?)'", str_re)  # 获取信息---ISBN
        if (len(isbn)>0):
            isbn = isbn[0]

        title = soup.select_one('#wrapper > h1 > span')
        if title is not  None:
            title = title.get_text()  # 获取信息---评分
        # print(title)
        score = soup.select_one('#interest_sectl > div > div.rating_self.clearfix > strong')
        if score is not  None:
            score = score.get_text()  # 获取信息---评分
        # print(score.get_text())
        description = soup.select_one('#link-report > div:nth-child(1) > div > p:nth-child(1)')
        if description is not None:
            description = description.get_text()  # 获取信息---简介
        # print(description.get_text())
        img = soup.select_one('#mainpic > a > img')
        img = img['src']
        # print(img)
        # print(isbn,title,author,publish,publish_year,score,price,description,img)
        save_to_db(isbn,title,author,publish,publish_year,score,price,description,img,tag1,tag2) # 存储信息到数据库
    except Exception as e:
        print(href,"出错了，继续....")

#存储book信息到数据库
def save_to_db(isbn,title,author,publish,publish_year,score,price,description,img,tag1,tag2):
    print("插入图书【%s】数据..."%(title))
    insert_sql = "INSERT INTO "+database_name+"(isbn,title,author,publish,publish_year,score,price,description,img,kind,tag) " \
                 "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s','%s)" % \
                 (isbn,title,author,publish,publish_year,score,price,description,img,tag1,tag2,str(random.randint(1,100)))
    conn.execute(insert_sql) # sqllite
    conn.commit()# sqllite
    # cursor.execute(insert_sql) # mysql
    # connect.commit() # mysql


if __name__ == '__main__':
    getBookInfo('https://book.douban.com/subject/26340138/',"tage1","tag2")

    # 关闭数据库连接
    conn.close() # sqllite
    # cursor.close() # mysql
    # connect.close() # mysql


    # driver.get(starturl) # 返回初始页面