# 非阻塞
import random
import gevent
import time

import gevent.monkey
gevent.monkey.patch_all()
# 自动切换 若没有这行代码，若sleep则会顺序执行：小明1-3，小红1-3，小刚1-3实现协程
# 需要等待时，自动切换。使得sleep程序运行方式相当于gevent.sleep(random.randint(1,5))。

def show_wait(name, num):
    for i in range(num):
        waiting = random.randint(1,5)
        print(i,"->",name, "wait for",waiting, "seconds")
        gevent.sleep(waiting)  # 不需要等待就顺序执行，需要等待，自动切换
        # time.sleep(waiting) # time.sleep就相当于顺序执行（这是程序sleep，不是协程等待）。
        print(i,"->",name,"over")



if __name__ == '__main__':
    g1 = gevent.spawn(show_wait, "小明", 3)
    g2 = gevent.spawn(show_wait, "小红", 3)
    g3 = gevent.spawn(show_wait, "小刚", 3)
    g1.join()
    g2.join()
    g3.join()