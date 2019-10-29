import requests
from lxml import etree
import chardet
URL = 'http://quote.stockstar.com/'

def getUrl(url):
    r = requests.get(url)
    ecode = chardet.detect(r.content)
    # print(ecode) # 打印字符编码信息
    r.encoding = ecode['encoding']
    return r.text

txt = getUrl(URL)
html = etree.HTML(txt)

# 一行数据，但是含有三种xpath格式
# //*[@id="datalist"]/tr[1]/td[1]/a
# //*[@id="datalist"]/tr[1]/td[3]/span
# //*[@id="datalist"]/tr[1]/td[7]

# //*[@id="datalist"]/tr/td/a/text() 错误1
# //*[@id="datalist"]/tr/td/span/text() 错误2
# //*[@id="datalist"]/tr/td/text() 错误3
# // 在xpath中代表选取此节点的所有子节点
datalist = html.xpath('//*[@id="datalist"]/tr/td//text()')
print(datalist)