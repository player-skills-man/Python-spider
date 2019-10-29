from bs4 import UnicodeDammit
import requests

dammint = UnicodeDammit(requests.get("http://www.baidu.com").content)
print(dammint.unicode_markup)
