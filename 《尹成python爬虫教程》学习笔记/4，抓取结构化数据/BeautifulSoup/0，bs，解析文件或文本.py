import bs4
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
# 通过字符串str---创建bs对象,默认会被转换成unicode编码。
soup = bs(html_str,'lxml')
# print(soup.prettify()) # 打印对象

# 通过读取文件创建bs对象，默认会被转换成unicode编码。
soup2 = bs(open("index.html"),'lxml')
# print(soup2.prettify())# 打印对象

#***********************使用BeautifulSoup结构化解析***********************************

########################对象种类#####################################
'''
#tag对象

# 打印tag对象
print(soup.name)
print(soup.title.name)

# 修改tag对象
soup.title.name = 'mytitle'
print(soup.title)
print(soup.mytitle)

# 获取tag对象的属性
print(soup.p['class']) # 获取tag属性的方法1
print(soup.p.get('class')) # 获取tag属性的方法2
print(soup.p.attrs['class']) # 获取tag属性的方法3
print(soup.p.attrs) # 获取tag全部属性

# 修改tag对象的属性
soup.p['class']="myClass"
print(soup.p)
'''

'''
#NavigableString对象
# 获取tag内部的文字
print(soup.p.string)
print(type(soup.p.string)) #<class 'bs4.element.NavigableString'>

#python用NavigableString来包装tag中的字符串，编码unicode，通过str()方法可直接将其转换为字符串(py3默认为unicode)
unicode_str = str(soup.p.string)
print(type(unicode_str))
print(unicode_str)
'''

'''
# BeautifulSoup对象是一个文档的全部内容。可以把它当作一个特殊的tag对象，但name和attrs仅仅是为了实现统一接口，没有意义。
print(type(soup.name))
# print(soup.name) # 仅仅是统一接口，无意义
# print(soup.attrs)# 仅仅是统一接口，无意义
'''

'''
#Comment对象
#  <a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
print(soup.a.string) # 原本是一个注释，但是打印的时候把注释符号去掉了。
print(type(soup.a.string)) # <class 'bs4.element.Comment'> 这是一个注释

# if type(soup.a.string)==bs4.element.Comment:
#     print(soup.a.string)
'''



########################遍历文档树#####################################
'''
# 子节点
print(soup.head.contents)
print(len(soup.head.contents))
print(soup.head.contents[0].string)
# 直接子节点
print("---children---")
for child in soup.head.children:
    print(child)
print("---descendants---")
# 所有的子孙节点递归循环
for child in soup.head.descendants:
    print(child)

"""
.string这个属性很有特点：
如果一个标记里面没有标记了，那么.string就会返回标记里 面的内容。
如果标记里面只有唯一的一个标记了，那么.string也会返回最里面的内容。
如果tag包含了多个子节点，tag就无法确定string方法应该调用哪个子节点的内容，.string 的输出结果是None。
"""
print(soup.head.string)
print(soup.title.string)
print(soup.html.string)
'''



'''
for string in soup.strings:
    print((repr(string)))

for string in soup.stripped_strings:
    print((repr(string)))

print(soup.title)
print(soup.title.parent)

print(soup.a)
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    0,else:
        print((parent.name))

print(soup.p.next_sibling)
print(soup.p.prev_sibling)
print(soup.p.next_sibling.next_sibling)

for sibling in soup.a.next_siblings:
    print((repr(sibling)))

print(soup.head)
print(soup.head.next_element)

for element in soup.a.next_elements:
    print((repr(element)))

print(soup.find_all('b'))

import re
for tag in soup.find_all(re.compile("^b")):
    print((tag.name))

print(soup.find_all(["a", "b"]))

for tag in soup.find_all(True):
    print((tag.name))
def hasClass_Id(tag):
    return tag.has_attr('class') and tag.has_attr('id')
print(soup.find_all(hasClass_Id))

print(soup.find_all(id='link2'))

print(soup.find_all(href=re.compile("elsie")))

print(soup.find_all(id=True))
print(soup.find_all("a", class_="sister"))

print(soup.find_all(href=re.compile("elsie"), id='link1'))

data_soup = bs('<div data-foo="value">foo!</div>')
data_soup.find_all(attrs={"data-foo": "value"})


print(soup.find_all(text="Elsie"))
print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))
print(soup.find_all(text=re.compile("Dormouse")))

print(soup.find_all("a", text="Elsie"))

print(soup.find_all("a", limit=2))

print(soup.find_all("title"))
print(soup.find_all("title", recursive=False))


#***********CSS选择器****************
#直接查找title标签
print(soup.select("title"))
#逐层查找title标签
print(soup.select("html head title"))
#查找直接子节点
#查找head下的title标签
print(soup.select("head > title"))
#查找p下的id="link1"的标签
print(soup.select("p > #link1"))
#查找兄弟节点
#查找id="link1"之后class=sisiter的所有兄弟标签
print(soup.select("#link1 ~ .sister"))
#查找紧跟着id="link1"之后class=sisiter的子标签
print(soup.select("#link1 + .sister"))

print(soup.select(".sister"))
print(soup.select("[class~=sister]"))

print(soup.select("#link1"))
print(soup.select("a#link2"))

print(soup.select('a[href]'))

print(soup.select('a[href="http://example.com/elsie"]'))
print(soup.select('a[href^="http://example.com/"]'))
print(soup.select('a[href$="tillie"]'))
print(soup.select('a[href*=".com/el"]'))
'''
