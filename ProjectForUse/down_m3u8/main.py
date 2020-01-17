# encoding=utf-8
import os
import shutil  # 文件树操作需要
import datetime
from package.combine_ts import combine
from package.down_ts import download, get_ts_urls

# m3u8_url文件地址
# m3u8_url = 'https://jdvodrvfb210d.vod.126.net/mooc-video/nos/hls/2018/04/28/1009218006_cff89340b62041e396ec9a91a9974a81_sd.m3u8'
m3u8_url = 'blob:https://hywm1.com/6145f824-3723-45a3-ad6d-fb1297b45824'
# 要保存的文件名
video_name = "result/h2.ts"


def down_m3u8(m3u8_url,video_name):
    ts_urls = get_ts_urls(m3u8_url)
    m3u8_file_name = m3u8_url.split("/")[-1]
    temp_download_path = m3u8_file_name+"ts_list_temp"
    # 创建目录ts_list_temp
    if not os.path.exists(temp_download_path):
        os.mkdir(temp_download_path)

    print("开始下载 %s" % m3u8_file_name, end="\t")
    start = datetime.datetime.now().replace(microsecond=0)
    download(ts_urls, temp_download_path)
    combine(temp_download_path, video_name)
    shutil.rmtree(temp_download_path)  # 删除临时文件夹和文件
    end = datetime.datetime.now().replace(microsecond=0)
    print("耗时：%s" % (end - start))


if __name__ == '__main__':
    down_m3u8(m3u8_url,video_name)
