import requests

def getCookie(url):
    Hostreferer = {
        #'Host':'***',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }
    #urllib或requests在打开https站点是会验证证书。 简单的处理办法是在get方法中加入verify参数，并设为False
    html = requests.get(url, headers=Hostreferer,verify=False)
    #获取cookie:DZSW_WSYYT_SESSIONID
    if html.status_code == 200:
        print(html.cookies)
        for cookie in html.cookies:
            print(cookie)

if __name__ == '__main__':
    URL = "https://baidu.com/"
    getCookie(URL)