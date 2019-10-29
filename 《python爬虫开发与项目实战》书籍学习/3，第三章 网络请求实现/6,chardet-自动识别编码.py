# chardet:自动识别编码
import requests
import chardet

r = requests.get('http://www.baidu.com')
coding = chardet.detect(r.content)  # 自动识别编码格式
print(coding)
r.encoding = coding['encoding'] # 设置编码格式
print(r.text)