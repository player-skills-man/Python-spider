from lxml import etree
import re

# 通过读取文件
html = etree.parse('blibli.html',etree.HTMLParser())
result = etree.tostring(html, pretty_print=True)# 修复HTML代码，补全其他选项。返回result是bytes类型
txt = str(result)

def get_cid(txt):
    # 提取cid
    regStr = '"cid":(.+?),"page":'
    regex = re.compile(regStr,re.IGNORECASE)
    cid_list = regex.findall(txt)
    print(len(cid_list))

def get_part_name(txt):
    # 提取视频part名称
    regStr2 = '"part":"(.+?)",'
    regex2 = re.compile(regStr2,re.IGNORECASE)
    part_list = regex2.findall(txt)
    print(len(part_list))

get_cid(txt)
get_part_name(txt)