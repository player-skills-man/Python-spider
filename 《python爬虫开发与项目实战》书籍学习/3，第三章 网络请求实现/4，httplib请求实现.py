# httplib/urllib实现:GET请求

import http.client
conn =None
try:
    conn = http.client.HTTPConnection("www.zhihu.com")
    conn.request("GET", "/")
    response = conn.getresponse()
    print((response.status, response.reason))
    print(('-' * 40))
    headers = response.getheaders()
    for h in headers:
        print(h)
    print(('-' * 40))
    print((response.msg))
except Exception as e:
    print(e)
finally:
    if conn:
        conn.close()



# httplib/urllib实现:POST请求
import http.client, urllib.request, urllib.parse, urllib.error
conn = None
try:
    params = urllib.parse.urlencode({'name': 'qiye', 'age': 22})
    headers = {"Content-type": "application/x-www-form-urlencoded"
    , "Accept": "text/plain"}
    conn = http.client.HTTPConnection("www.zhihu.com", 80, timeout=3)
    conn.request("POST", "/login", params, headers)
    response = conn.getresponse()
    print(response.getheaders()) #获取头信息
    print(response.status)
    print(response.read())
except Exception as e:
    print(e)
finally:
    if conn:
        conn.close()
