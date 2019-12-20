# encoding=utf-8

import datetime
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from package.mk_ts_url import get_ts_urls


def download(ts_urls, download_path):
    for i in range(len(ts_urls)):
        ts_url = ts_urls[i]
        try:
            response = requests.get(ts_url, stream=True, verify=False)
        except Exception as e:
            print("异常请求：%s" % e.args)
            return

        ts_path = download_path + "/{0}.ts".format(i)
        with open(ts_path, "wb+") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)


if __name__ == '__main__':
    m3u8_url = 'https://jdvodrvfb210d.vod.126.net/mooc-video/nos/hls/2018/04/28/1009218006_cff89340b62041e396ec9a91a9974a81_sd.m3u8'
    ts_urls = get_ts_urls(m3u8_url)
    download_path = "ts_list"
    download(ts_urls, download_path)
