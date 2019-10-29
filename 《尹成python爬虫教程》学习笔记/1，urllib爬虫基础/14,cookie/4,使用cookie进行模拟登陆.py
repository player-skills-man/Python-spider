"""
https://blog.csdn.net/qq_39138295/article/details/81406991
"""
from http.cookiejar import CookieJar,LWPCookieJar
from urllib.request import Request,urlopen,HTTPCookieProcessor,build_opener
from urllib.parse import urlencode
import ssl

cookie = LWPCookieJar(filename='cookie.txt')# 创建一个对象存储cookie。如果需要保存cookie文件
# cookie = LWPCookieJar() # 创建一个对象存储cookie。如果不需要保存cookie文件
cookie_handler = HTTPCookieProcessor(cookie) # 创建一个对象使用cookie
opener = build_opener(cookie_handler) # 使用cookie打开
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}
post_url = 'http://www.renren.com/PLogin.do'
# urlencode对url当中的参数进行编码;
# urlencode()编码的对象为字典类型
post_data = urlencode({
    'email':'yincheng5201314@163.com',   #自己的登陆账号
    'password':'tsinghua'   #自己的登陆密码
})
# 请求url 并传参，设置编码方式
request = Request(post_url,bytes(post_data,encoding='utf-8')) # 请求登录，抓取cookie
# request = Request(post_url,post_data) # 错误，type错误
# 解决ssl证书问题
ssl._create_default_https_context = ssl._create_unverified_context
response = opener.open(request) # 载入cookie,登录
print(response.read().decode("utf-8"))
cookie.save(ignore_discard=True,ignore_expires=True) # 保存cookie