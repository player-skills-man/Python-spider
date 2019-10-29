# 程序taskWorker.py代码(win/linux版)
#coding:utf-8
import time
from multiprocessing.managers import BaseManager
# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass
# 实现第一步：使用QueueManager注册获取Queue的方法名称
QueueManager.register('get_task_queue') # 注册函数，调用服务器
QueueManager.register('get_result_queue')
# 实现第二步：连接到服务器:
server_addr = '192.168.10.103'
# 端口和验证口令注意保持与服务进程设置的完全一致:
manager = QueueManager(address=(server_addr, 8001), authkey=b'qiye')
# 连接服务器:
print(('Connect to server %s...' % server_addr))
manager.connect()
# 实现第三步：获取Queue的对象:
task = manager.get_task_queue() # 任务
result = manager.get_result_queue() # 结果
# 实现第四步：从task队列取任务,并把结果写入result队列:
while(not task.empty()):
        image_url = task.get(True,timeout=5)
        print(('run task download %s...' % image_url))
        time.sleep(2)
        result.put('%s--->success'%image_url)

# 处理结束:
print('worker exit.')