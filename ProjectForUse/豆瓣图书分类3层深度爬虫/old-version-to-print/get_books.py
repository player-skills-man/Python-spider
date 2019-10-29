"""
获取豆瓣图书每一本书的url链接
"""

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

"""
#subject_list > ul > li:nth-child(1) > div.info > h2 > a
#subject_list > ul > li:nth-child(2) > div.info > h2 > a
"""

def get_books(href):
    start_num = 0 # href 位置定位页面，每页20本book
    url = href + '?start={}'.format(start_num) # 初始url

    books_page = urllib.request.urlopen(url).read()
    books_page = bytes.decode(books_page, encoding="utf-8")
    soup = BeautifulSoup(books_page, 'lxml')  # 创建CSS选择器

    while True: # 浏览每一页
        print('startnum = ',start_num)
        for id in range(20): # 获取一个page的<=20本书
            book_element = soup.select_one('#subject_list > ul > li:nth-child({}) > div.info > h2 > a'.format(id+1))
            if book_element is not None:
                print(book_element.get('href'))
            else:
                break

        # 如果新的链接没有book，结束while
        start_num += 20
        url = href + '?start={}'.format(start_num)
        books_page = urllib.request.urlopen(url).read()
        books_page = bytes.decode(books_page, encoding="utf-8")
        soup = BeautifulSoup(books_page, 'lxml')  # 创建CSS选择器
        book_element_plus = soup.select_one('#subject_list > ul > li:nth-child(1) > div.info > h2 > a')
        if book_element_plus is None:
            break


if __name__ == '__main__':
    url="https://book.douban.com" + urllib.parse.quote('/tag/神经网络')
    get_books(url)