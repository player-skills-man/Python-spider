import threading,time,random


def myThread(name):
    with sep:
        for i in range(10):
            time.sleep(random.randint(2,5))
            print(name,str(i),":",threading.current_thread().name)

sep = threading.Semaphore(3) # ！线程数量限制，信号量
td_list = []
for name in ['a','b','c','d','e']:
    td = threading.Thread(target=myThread,args=(name,))
    td.start()
    td_list.append(td)

for td in td_list:
    td.join()