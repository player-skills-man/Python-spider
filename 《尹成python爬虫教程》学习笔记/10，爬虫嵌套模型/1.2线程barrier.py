# Barrier类是设置了一个线程数量障碍，当等待的线程到达了这个数量就会唤醒所有的等待线程。

"""

__init__(self, parties, action=None, timeout=None) parties障碍要求的线程数量 action设置了的话会在突破障碍的时候被某一个被唤醒的线程调用 timeout给之后的wait()设置了个默认的等待时间


wait(self, timeout=None) 当前线程进入阻塞状态


abort(self) 强行突破阻碍，所有正在等待的线程和要调用wait()方法的线程收到一个BrokenBarrierError异常

reset(self) 重置当前对象，所有正在等待的线程收到一个BrokenBarrierError异常
————————————————
版权声明：本文为CSDN博主「去海里喂鱼」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/u013346751/article/details/78520188

"""

import threading
import time


def display():
    print("放了你们")


barrier = threading.Barrier(3, display)


class Chick(threading.Thread):
    def run(self):
        while True:
            print(self.getName(), ": 你抓不到我")
            time.sleep(1)
            print(self.getName(), ": 好吧，你抓到我了")
            try:
                barrier.wait()
            except threading.BrokenBarrierError:
                print("BrokenBarrierError")


if __name__ == "__main__":
    c1 = Chick(name="A")
    c2 = Chick(name="B")
    c3 = Chick(name="C")
    c1.start()
    c2.start()
    c3.start()
    time.sleep(2)
    # barrier.reset()
    print("main")
