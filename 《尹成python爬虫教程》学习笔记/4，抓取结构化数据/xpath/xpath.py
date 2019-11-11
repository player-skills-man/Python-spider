from lxml import etree

# 通过字符串
'''
html_str = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
text = etree.HTML(html_str)
result = etree.tostring(text)# 修复HTML代码，补全其他选项
print(result)
print(type(result))
'''




# 通过读取文件
html = etree.parse('chpwd.html',etree.HTMLParser())
result = etree.tostring(html, pretty_print=True)# 修复HTML代码，补全其他选项。返回result是bytes类型
# print(result)
# print(type(result))

# xpath简单应用,抽取url
urls = html.xpath(".//*[@class='sister']/@href")
print(urls)
