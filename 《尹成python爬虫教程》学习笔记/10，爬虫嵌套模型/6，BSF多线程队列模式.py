import threading
import os
import queue
import time







def download_page(url):
    time.sleep(3)
    print("下载页面，",threading.current_thread().getName())
    return "urls"


def get_page_datas(page_data):
    print("获取数据",threading.current_thread().getName())
    return [1,2,3]


def get_page_urls(page_data):
    print("获取urls",threading.current_thread().getName())
    return [1,2,3,4,5,6,7]


"""
线程延时调用：
timethread = threading.Timer(5,function=func,args=(n1,n2,...)) #5s以后开启一个线程，执行func函数
timetread.start()
"""


sim = threading.Semaphore(10)  # 最大线程并发数量
def BFS(url, data_queue,url_queue):
    url_queue.put(url)
    page_data = download_page(url_queue.get())
    data_list = get_page_datas(page_data)
    if len(data_list) != 0:
        for data in data_list:
            data_queue.put(data)

    url_list = get_page_urls(page_data)
    if len(url_list) != 0:
        for myurl in  url_list:
            print(myurl)
            url_queue.put(myurl)

def startBFS(url,data_queue,url_queue):
    url_queue.put(url)
    while True:
        while not url_queue.empty():
            with sim:
                threading.Thread(target=BFS,args=(data_queue,url_queue))


if __name__ == '__main__':
    data_queue = queue.Queue()
    url_queue = queue.Queue()
    startBFS("",data_queue=data_queue,url_queue=url_queue)