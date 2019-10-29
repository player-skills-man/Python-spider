import requests

try:
    # requests.get('http://wenshu.court.gov.cn/', proxies={"http":"http://192.168.113.1:808"}) # 无需账号密码的代理
    requests.get('http://wenshu.court.gov.cn/', proxies={"http":"http://yyl:123456@192.168.113.1:808"}) # 需账号密码的代理
except:
    print ('connect failed')
else:
    print ('success')