import requests

# 实现一个完整的请求与响应模型:GET
r = requests.get('http://www.baidu.com')
# print(r.content)

# 带参数的GET请求
# payload = {'Keywords': 'blog:qiyeboy','pageindex':1}
payload = {'wd':"python教程"}
r = requests.get('http://www.baidu.com/s', params=payload)
print(r.url)

'''
# 实现一个完整的请求与响应模型:POST
postdata={'key':'value'}
r = requests.post('http://www.xxxxxx.com/login',params=postdata)
print(r.content)
'''


