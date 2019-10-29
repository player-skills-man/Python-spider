import gevent
import gevent.pool
import gevent.monkey
gevent.monkey.patch_all()

import time
def run(name):
    time.sleep(1)
    print(name," is running...")
    return name

if __name__ == '__main__':
    mypool = gevent.pool.Pool(3) # 最大并发3个
    args = ["小米","小浩","小尼姑","小和尚"]
    res = mypool.map(run,args)
    print("------------------------")
    print(res)


