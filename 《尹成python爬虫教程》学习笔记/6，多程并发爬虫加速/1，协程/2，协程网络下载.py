import gevent
import gevent.monkey
gevent.monkey.patch_all() # 自动切换

import requests

def down(url):
    txt = requests.get(url).text
    print("lenth of",url,len(txt))

if __name__ == '__main__':
    url_list = [
        'https://www.baidu.com',
        'https://www.qq.com',
        'https://www.163.com'
    ]

    #join
    # for url in url_list:
    #     gevent.spawn(down,url).join()



    #joinall1
    # gevent.joinall([gevent.spawn(down,url) for url in url_list])



    # #joinall1相当于：
    # gevent.joinall(
    #     [
    #         gevent.spawn(down, url_list[0]),
    #         gevent.spawn(down, url_list[1]),
    #         gevent.spawn(down, url_list[2])
    #     ]
    # )