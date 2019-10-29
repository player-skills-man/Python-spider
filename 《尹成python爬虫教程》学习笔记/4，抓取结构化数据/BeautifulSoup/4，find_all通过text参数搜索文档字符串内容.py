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


print(soup.find_all(text='The Dormouse\'s story')) # 精确等于

print(soup.find_all(text=['The Dormouse\'s story','hello','Elsie'])) # 列表，其中一个等于

print(soup.find_all(text=re.compile("^T"))) # 正则