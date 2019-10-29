# task_master.py
# A机器负责发送任务和接受结果：
import random, time, queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass

def get_task():
    return task_queue
def get_result():
    return result_queue

if __name__ == '__main__':
    print("master start.")
    QueueManager.register('get_task_queue', callable=get_task)
    QueueManager.register('get_result_queue', callable=get_result)
    manager = QueueManager(address=('127.0.0.1', 9833), authkey=b'abc')
    manager.start()
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
       task.put("notepad") # 打开记事本
    print('try get results...')

    for i in range(10):
        r = result.get(timeout=100)
        print('Result:%s' % r)
    manager.shutdown()
    print('master exit.')