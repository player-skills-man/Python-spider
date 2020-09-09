import requests
import re
import urllib.parse
# 构造搜索word新链接
def make_url(word):
    URL = 'http://tieba.baidu.com/f?'
    data = {
        "ie": "utf-8",
        "kw": word
    }
    com_url = URL+(urllib.parse.urlencode(data))
    return com_url

def main():
    html = requests.get(make_url("鞠婧祎")).text
    # print(html)
    reStr = '"  bpic="([\s\S]+?)" class="threadlist_pic j_m_pic "'
    regex = re.compile(reStr)
    links = regex.findall(html)
    print(len(links))
    for link in links:
        print(link)
if __name__ == '__main__':
    main()