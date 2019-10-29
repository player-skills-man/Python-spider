# task_worker.py
# B机器负责处理任务和发送结果：
import sys, time, queue
from multiprocessing.managers import BaseManager

import os

class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('connect to server %s...' % server_addr)

m = QueueManager(address=(server_addr, 9833), authkey=b'abc')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        str = task.get(timeout=10)
        res = os.system(str)
        time.sleep(1)
        result.put(res)
    except queue.Empty:
        print('task queue is empty')

print('worker exit')