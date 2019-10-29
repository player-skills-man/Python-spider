import requests
import re
import os
import time
with open("testip.log","a") as f:
    try:
        for i in range(2):
            time.sleep(2)
            response = requests.get(
                "http://httpbin.org/get",
                proxies={
                    "http": "http://5d8e4bd61e574bb2adc696def7f65012:@proxy.crawlera.com:8010/",
                },
            )
            # print(response.text)

            ip = re.findall("((?:\d{1,3}\\.){3}\d{1,3})",response.text)[1]
            ipaddr = requests.get("http://ip-api.com/json/{}?lang=zh-CN".format(ip)).text
            f.write("{ip} : {ipaddr}\n".format(ip=ip,ipaddr=ipaddr))
            print(ip)
    except:
        f.write("erro  ---\n"+time.ctime())

