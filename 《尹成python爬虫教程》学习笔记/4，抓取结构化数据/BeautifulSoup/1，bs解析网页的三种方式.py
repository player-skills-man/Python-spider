from bs4 import BeautifulSoup as bs

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

soup1 = bs(html_str,'html.parser') # 常规网页解析.比较慢，不推荐
# xml文件解析更快
soup2 = bs(html_str,'lxml')  # lxml解析方式。
# html5文件解析更快
soup3 = bs(html_str,'html5lib',from_encoding='utf-8') # HTML5解析。 # 需要安装html5lib模块
