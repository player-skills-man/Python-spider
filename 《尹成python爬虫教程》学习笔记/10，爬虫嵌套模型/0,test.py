import time
import threading

sem = threading.Semaphore(3)


def callback():
    with sem:
        time.sleep(3)
        print(time.ctime(),threading.current_thread().getName())
        for i in range(2):
            threading.Thread(target=callback).start()

def start():
    callback()

start()

"""
发现的问题:
在线程递归调用函数中，只要使用多次调用thread，[多个递归]就会导致线程信号量失效。
运行时报错：RuntimeError: can't start new thread

解决办法：
sleep几秒，time.sleep(3)。使得OS及时回收线程。
"""