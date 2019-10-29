import requests
from lxml import etree
import chardet

def getUrl(url):
    r = requests.get(url)
    ecode = chardet.detect(r.content) # 自动识别编码
    # print(ecode) # 打印字符编码信息
    r.encoding = ecode['encoding']
    return r.text

def getPageTitle(url):
    txt = getUrl(url)
    html = etree.HTML(txt)
    # 获取标题
    title_list = html.xpath('//*[@class="artlist clearfix"]/dl/dt/a/text()')
    return title_list

if __name__ == '__main__':
    URL = 'https://www.jb51.net/list/list_72_1.htm'
    'https://www.jb51.net/list/list_72_2.htm'
    'https://www.jb51.net/list/list_72_3.htm'
    title_list = getPageTitle(URL)
    print(title_list)