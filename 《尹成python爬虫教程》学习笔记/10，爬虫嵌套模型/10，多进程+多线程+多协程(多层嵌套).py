from multiprocessing import Process
import threading
import gevent
import gevent.pool
import gevent.monkey
gevent.monkey.patch_all()
import os

# 3个进程，3*3个线程，3*3*3个协程

def do(name):
    print(os.getpid(),threading.current_thread().getName(),"do",name)

# 测试ok
def fun_event(list):
    mypool = gevent.pool.Pool(3)  # 最大并发3个
    for i in range(3):
        for name in list[i:len(list):3]:
            mypool.map(do,(name,))


sem = threading.Semaphore(3) # 并发数3
def fun_thread(list):
    threadslist = []
    for i in range(3):
        part_list = list[i:len(list):3]
        mytd = threading.Thread(target=fun_event, args=(part_list,))
        mytd.start()
        threadslist.append(mytd)

    for td in threadslist:
        td.join()

def fun_process(list):
    processlist = []
    for i in range(3):
        part_list = list[i:len(list):3]
        myprocess = Process(target=fun_event, args=(part_list,))
        myprocess.start()
        processlist.append(myprocess)

    for p in processlist:
        p.join()


if __name__ == '__main__':
    list = [i for i in range(100)]
    fun_process(list)
