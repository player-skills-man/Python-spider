import requests
import urllib.request
import urllib.parse
import random
import re


# get获取网页源码
def getResponseWithurl(url):
    request = urllib.request.Request(url, headers=getheaders())
    response = urllib.request.urlopen(request)
    return response


# 返回一个随机的请求头 headers
def getheaders():
    # 各种PC端
    user_agent_list_2 = [
        # Opera
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
        "Opera/8.0 (Windows NT 5.1; U; en)",
        "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
        # Firefox
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        # Safari
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
        # chrome
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        # 360
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        # 淘宝浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        # 猎豹浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        # QQ浏览器
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        # sogou浏览器
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
        # maxthon浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
        # UC浏览器
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
    ]
    # 各种移动端
    user_agent_list_3 = [
        # IPhone
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # IPod
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # IPAD
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        # Android
        "Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        # QQ浏览器 Android版本
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        # Android Opera Mobile
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        # Android Pad Moto Xoom
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        # BlackBerry
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        # WebOS HP Touchpad
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        # Nokia N97
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        # Windows Phone Mango
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        # UC浏览器
        "UCWEB7.0.2.37/28/999",
        "NOKIA5700/ UCWEB7.0.2.37/28/999",
        # UCOpenwave
        "Openwave/ UCWEB7.0.2.37/28/999",
        # UC Opera
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999"
    ]
    # 一部分 PC端的
    user_agent_list_1 = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    user_agent_list = user_agent_list_1 + user_agent_list_2 + user_agent_list_3
    UserAgent = random.choice(user_agent_list)
    headers = {'User-Agent': UserAgent}
    return headers


# 返回网页TeXT
def getTextByUrl(url):
    return requests.get(url, headers=getheaders()).text


# 搜索word，返回网页源码
def getTextByWord(word):
    '贴吧链接格式:'
    'http://tieba.baidu.com/f?kw=python3&ie=utf-8&pn=0'
    'http://tieba.baidu.com/f?kw=python3&ie=utf-8&pn=50'
    'http://tieba.baidu.com/f?kw=python3&ie=utf-8&pn=100'

    payload = {'kw': word, 'ie': 'utf-8', 'pn': 0}
    return requests.get('http://tieba.baidu.com/f', params=payload, headers=getheaders()).text


# 关注人数
def getPeopleNum(txt):
    regStr = '<span class="card_menNum">([\s\S]+?)</span>'
    regex = re.compile(regStr, re.IGNORECASE)
    num = regex.findall(txt)
    if len(num) > 0:
        return int(str(num[0]).replace(',', ''))
    else:
        print("getPeopleNum失败")
        return None


# 发帖数量
def getTieNum(txt):
    regStr = '<span class="card_infoNum">([\s\S]+?)</span>'
    regex = re.compile(regStr, re.IGNORECASE)
    num = regex.findall(txt)
    if len(num) > 0:
        return int(str(num[0]).replace(',', ''))
    else:
        print("getTieNum失败")
        return None


# 拼接所有页面连接
def getWordTie_urllist(word):
    tieList = []  # 存储所有页面连接
    tieNum = getTieNum(txt=getTextByWord(word))  # 发帖数量
    # print(tieNum)
    # 处理连接获取失败的情况
    if (None == tieNum):
        return ["null", ]

    dict = {"kw": word}  # 编辑url连接参数字典
    encode_word = urllib.parse.urlencode(dict)  # url编码

    '贴吧链接格式:'
    'http://tieba.baidu.com/f?kw=python3&ie=utf-8&pn=0'
    'http://tieba.baidu.com/f?kw=python3&ie=utf-8&pn=50'
    'http://tieba.baidu.com/f?kw=python3&ie=utf-8&pn=100'
    if (tieNum % 50 == 0):
        # 整除
        for i in range(tieNum // 50):
            tieList.append('http://tieba.baidu.com/f?' + encode_word + '&ie=utf-8&pn=' + str(i * 50))
    else:
        # 不整除
        for i in range(tieNum // 50 + 1):
            tieList.append('http://tieba.baidu.com/f?' + encode_word + '&ie=utf-8&pn=' + str(i * 50))

    # 返回url列表
    return tieList


# 提取页面帖子子链接
def getTitleTieUrl(url):
    tie_urls = []  # 存储结果
    txt = getTextByUrl(url)
    regStr = '<ul id="thread_list" class="threadlist_bright j_threadlist_bright">([\s\S]*?)<div class="thread_list_bottom clearfix">'
    regex = re.compile(regStr, re.IGNORECASE)
    ul_html = regex.findall(txt)[0]  # 第1次正则过滤，抓取ul表格

    regStr2 = 'href="/p/(\d+)" title='
    regex2 = re.compile(regStr2, re.IGNORECASE)
    url_title_list = regex2.findall(ul_html)  # 第2次正则过滤，抓取ul中每个href
    # print(url_title_list)
    # 主题帖连接：http://tieba.baidu.com/p/6247696440
    for str in url_title_list:
        tie_urls.append('http://tieba.baidu.com/p/' + str)

    return tie_urls


# 获取url页面QQ
def getQQ(url):
    qq_list = []
    response = getResponseWithurl(url)
    regStr = '[1-9][0-9]{4,14}'
    regex = re.compile(regStr, re.IGNORECASE)
    while True:
        line = response.readline().decode("utf-8")
        # print(line)
        if not line:
            break
        if (line.find("qq") != -1 or line.find("Qq") != -1 or line.find("qQ") != -1 or line.find("QQ") != -1):
            temp_qqlist = regex.findall(line)
            qq_list.extend(temp_qqlist)
    # print(ul_html)

    return qq_list


if __name__ == '__main__':
    # print(getTitleTieUrl('http://tieba.baidu.com/f?kw=python3&ie=utf-8&pn=0')) # 函数运行错误，测试

    WORD = "python3"  # 搜索词
    QQLIST = []  # QQ号码
    title_urls = []  # 主题帖子页面链接
    word_tie_url_list = []  # 贴吧页面链接

    # 提取贴吧页面链接
    word_tie_url_list = getWordTie_urllist(WORD)
    # print(word_tie_url_list[0])
    # print(word_tie_url_list[len(word_tie_url_list) - 1])
    # 返回正确
    if (word_tie_url_list[0] != "null"):
        # 提取主题帖子页面链接
        # for url in word_tie_url_list[0:2]:测试用
        for url in word_tie_url_list:
            # print(url)
            try:
                title_urls_temp = getTitleTieUrl(url)
                print(title_urls_temp)
                title_urls.extend(title_urls_temp)
            except:
                print(url,"，访问错误")
        # 过滤QQ号码
        for title_url in title_urls:
            try:
                QQLISTTemp = getQQ(title_url)
                print(QQLISTTemp)
                QQLIST.extend(QQLISTTemp)
            except:
                print(title_url,",访问错误")
