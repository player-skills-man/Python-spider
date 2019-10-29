import threading
import time

def run(name):
    with sem:
        for i in range(10):
            time.sleep(1)
            print(name,str(i),threading.current_thread().getName())

sem = threading.Semaphore(2)
"""
注意信号量的位置！！！
此代码:with sem设置在下面mytd上则不起作用，设置在run函数中则会起作用。
"""

threadslist = []
for name in "abcde":
    mytd = threading.Thread(target=run,args=(name,))
    mytd.start()
    threadslist.append(mytd)

for td in threadslist:
    td.join()