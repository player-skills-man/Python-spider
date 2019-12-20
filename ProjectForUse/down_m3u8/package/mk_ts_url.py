# encoding=utf-8
"""
＃m3u8文件下载url地址
https://jdvodrvfb210d.vod.126.net/mooc-video/nos/hls/2018/04/28/1009218006_cff89340b62041e396ec9a91a9974a81_sd.m3u8

#ts地址
https://jdvodrvfb210d.vod.126.net/mooc-video/nos/hls/2018/04/28/1009218006_cff89340b62041e396ec9a91a9974a81_sd0.ts

＃
"""
import requests


def get_ts_urls(m3u8_url):
    urls = []
    file_name = m3u8_url.split("/")[-1]
    base_url = m3u8_url.strip(file_name)
    r = requests.get(m3u8_url)
    lines = r.text.split('\n')
    for line in lines:
        if line.endswith(".ts"):
            urls.append(base_url + line.strip("\n"))
    return urls


if __name__ == '__main__':
    m3u8_url = 'https://jdvodrvfb210d.vod.126.net/mooc-video/nos/hls/2018/04/28/1009218006_cff89340b62041e396ec9a91a9974a81_sd.m3u8'
    ts_url_list = get_ts_urls(m3u8_url)
    print("\n".join(ts_url_list))
