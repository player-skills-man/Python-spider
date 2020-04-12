# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Ocean-yyl
# datetime:2020-04-12 17:43
# software: PyCharm
import requests
from baidu.client import BaiduClient

from my_api import get_attr


def get_access_token():
	APP_ID, API_KEY, SECRET_KEY = get_attr()
	client = BaiduClient(app_id=APP_ID, api_key=API_KEY, secret_key=SECRET_KEY)
	client.fetch_access_token()
	return client.access_token


def get_scores(sentence):
	access_token = get_access_token()
	# 默认gbk编码，若是要utf-8,需要加上说明:url?charset=UTF-8&access_token=
	url = "https://aip.baidubce.com/rpc/2.0/nlp/v2/dnnlm_cn?access_token={}".format(access_token)
	body = {
		"text": sentence
	}
	res = requests.post(url, json=body)
	if res.status_code == 200:
		try:
			return res.json()['ppl']
		except Exception as e:
			print(e)
			return False
	else:
		return False

if __name__ == '__main__':
	print(get_scores("我在北京工作")) # ppl 句子通顺的值：数值越低，句子越通顺
