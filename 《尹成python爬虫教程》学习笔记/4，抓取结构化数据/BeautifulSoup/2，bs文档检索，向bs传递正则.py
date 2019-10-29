from bs4 import BeautifulSoup as bs
import re
html_str = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><!-- Lacie --></a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = bs(html_str,'lxml')  # lxml解析方式。

regex = re.compile("t") # 匹配含有t字符的str

# 查找含有t字符的tag对象
for tag in soup.find_all(regex):
    print(tag.name)
