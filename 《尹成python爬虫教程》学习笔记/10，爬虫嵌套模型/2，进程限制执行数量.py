import multiprocessing
import os,time


def get(data):
    print(os.getpid(),":start")
    time.sleep(1)
    print(os.getpid(),":end")
    return data*data

if __name__ == '__main__':
    my_list = [x for x in range(20)]
    pool = multiprocessing.Pool(processes=2) # ！进程数量限制，进程池
    pool_outs = pool.map(get,my_list)
    pool.close()
    pool.join()
    print(pool_outs)