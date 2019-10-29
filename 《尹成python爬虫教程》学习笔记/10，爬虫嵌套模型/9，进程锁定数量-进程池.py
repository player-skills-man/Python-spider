import multiprocessing
import multiprocessing.pool
import os

import time
def run(name):
    time.sleep(1)
    print(name," is running...",os.getpid())
    return "-"+str(name)+"-"

if __name__ == '__main__':
    mylist = [i for i in range(100)]
    pool = multiprocessing.pool.Pool(4)
    pool_outputs = pool.map(run,mylist)

    pool.close()
    pool.join()
    print(pool_outputs)
