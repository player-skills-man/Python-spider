"""
读取豆瓣图书详情链接文件，爬去图书详细信息\

"""

from bs4 import BeautifulSoup
import urllib.request
import pymysql
import re

# 连接数据库
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
    db='books',
    # 编码格式
    charset='utf8'
)
print("连接数据库成功！")
# 2. 创建一个游标cursor, 是用来操作表。
cursor = connect.cursor()


# 使用xpath获取一个图书页面的图书信息
def getBookInfo(href):
    # print(href)
    html = urllib.request.urlopen(href).read()
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
    print(str_re)
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
    save_to_db(isbn,title,author,publish,publish_year,score,price,description,img) # 存储信息到数据库

#存储book信息到数据库
def save_to_db(isbn,title,author,publish,publish_year,score,price,description,img):
    print("插入图书【%s】数据..."%(title))
    insert_sql = "INSERT INTO book_info(isbn,title,author,publish,publish_year,score,price,description,img) " \
                 "VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s')" % (isbn,title,author,publish,publish_year,score,price,description,img)
    cursor.execute(insert_sql)
    print('图书【{}】信息存储完成！'.format(title))  # 打印提示
    # 4. 提交操作
    connect.commit()


if __name__ == '__main__':
    with open('./urls.txt','r',encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            newline = re.findall('"(.+)"',line)
            # print(newline[0])
            getBookInfo(newline[0])

    # 关闭数据库连接
    cursor.close()
    connect.close()


    # driver.get(starturl) # 返回初始页面