import threading
import os
import queue
import time

"""
发现的问题:
在线程递归调用函数中，只要使用多次调用thread，[多个递归]就会导致线程信号量失效。
运行时报错：RuntimeError: can't start new thread

分析错误原因:
首先信号量的工作机制如下：
互斥锁+容器  容器里同时最大可以存放五把钥匙，谁先拿到钥匙并释放后释放后，外面的才能继续抢钥匙十个线程，
五把钥匙，一开启肯定有五个线程能拿到钥匙，只有这五把钥匙谁先解锁了，之后的五个线程才能有抢钥匙的机会。
由于是递归调用，函数本身的运行就包含一个新的thread的创建和运行，由于有钥匙，这个不受限制。
而这个函数在运行的时候就已经获得了钥匙，所以新thread的创建不受影响，
这就导致钥匙————>每个“正常运行的thread”都有，而钥匙就失去了意义。
"打个比方就是：老子的钥匙给儿子们，儿子的钥匙又给孙子们。导致钥匙权力无限继承下去。"

解决思路:---》使用线程池统一管控。
保证钥匙的唯一性和不可重复使用。每次线程运行，都是到外部申请钥匙，而不是可以继承父函数的钥匙。

"""




def download_page(url):
    print("下载页面，",threading.current_thread().getName(),time.ctime())
    return "urls"


def get_page_datas(page_data):
    # print("获取数据",threading.current_thread().getName(),time.ctime())
    return [1,2,3]


def get_page_urls(page_data):
    # print("获取urls",threading.current_thread().getName(),time.ctime())
    return [1,2,3,4,5,6,7]


"""
线程延时调用：
timethread = threading.Timer(5,function=func,args=(n1,n2,...)) #5s以后开启一个线程，执行func函数
timetread.start()
"""


sim = threading.Semaphore(2)  # 最大线程并发数量
def BFS(url, data_queue):
    page_data = download_page(url)
    data_list = get_page_datas(page_data)
    if len(data_list) != 0:
        for data in data_list:
            data_queue.put(data)

    url_list = get_page_urls(page_data)
    if len(url_list) != 0:
            for myurl in  range(1): # 如果不循环，只一次，则不会报错
                # 递归调用，限定线程数量
                    try:
                        with sim:
                            threading.Thread(target=BFS,args=(myurl,data_queue)).start()
                    except RuntimeError as e:

                        """
                        RuntimeError: can't start new thread
                        
                        这个是由于每台计算机能进行的并行是有上限的，
                        经过测试本机的上限为1023个左右（win7 64位，i3 2核4线程），
                        可以进行设置提高上限，但我觉得此处没有必要，也不方便扩展，
                        所以想自行定义一个并行的上限数进行处理。
                        """
                        print(e)


def goBFS():
    q = queue.Queue()
    # with sim:
    threading.Thread(target=BFS,args=("1",q)).start()


goBFS()