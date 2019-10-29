import requests

# 返回本机ip的接口API有很多
# https://www.xxorg.com/tools/getip/
# http://ip.3322.org/
# http://icanhazip.com/
# http://whatismyip.akamai.com/
myip = requests.get("https://www.xxorg.com/tools/getip/").text
print("ip:{}".format(myip))


# 几个免费IP地址查询接口(API)
# http://ip.taobao.com/service/getIpInfo.php?ip= # 淘宝http://ip.taobao.com/service/getIpInfo2.php?ip=
# http://ip.ws.126.net/ipquery?ip= #126 IP API
# http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=js&ip= # 新浪
ipaddr = requests.get("http://ip.taobao.com/service/getIpInfo2.php?ip={}".format(myip)).text
print("IPaddr:{}".format(ipaddr))


# ip查询的接口
# http://ip-api.com/json/?lang=zh-CN
#
"""
http://ip-api.com/json/　　# 国际化英文显示
http://ip-api.com/json/?lang=zh-CN　　# 中文显示
http://ip-api.com/json/{myip}?lang=zh-CN　　# 查询某个ip的信息
"""