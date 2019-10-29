import requests
from lxml import etree
import chardet
URL = 'http://www.neihan8.com/article'
URL2 = 'http://222.186.10.159:468/article/'

def getUrl(url):
    r = requests.get(url)
    ecode = chardet.detect(r.content) # 自动识别编码
    # print(ecode) # 打印字符编码信息
    r.encoding = ecode['encoding']
    return r.text

txt = getUrl(URL2)
html = etree.HTML(txt)

# 获取标题
title_list = html.xpath('//*[@class="text-column-item box box-790"]/h3/a/text()')
print(title_list)

# 获取描述
desc_list = html.xpath('//*[@class="text-column-item box box-790"]/div[@class="desc"]/text()')
print("\n".join(desc_list))