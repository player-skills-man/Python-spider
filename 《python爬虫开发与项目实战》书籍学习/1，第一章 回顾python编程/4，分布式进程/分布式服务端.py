# taskManager.py for windows
import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
#任务个数
task_number = 10
#第一步：定义收发队列
task_queue = queue.Queue(task_number)
result_queue = queue.Queue(task_number)

#windows下绑定调用接口不能使用lambda，所以只能先定义函数再绑定
def get_task():
    return task_queue
def get_result():
     return result_queue

# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass
def win_run():
    # 第二步：把创建的两个队列注册在网络上，利用register方法。#windows下绑定调用接口不能使用lambda，所以只能先定义函数再绑定
    # 将Queue对象在网络中暴露
    QueueManager.register('get_task_queue',callable = get_task)
    QueueManager.register('get_result_queue',callable = get_result)
    ##第三步：绑定端口8001，设置验证口令‘qiye’。这个相当于对象的初始化。绑定端口并设置验证口令，windows下需要填写ip地址，linux下不填默认为本地
    manager = QueueManager(address=('127.0.0.1',8001),authkey = b'qiye')
    #第四步：启动管理，监听信息通道
    manager.start()

    try:
        #第五步：通过管理实例的方法获得通过网络访问的Queue对象。通过网络获取任务队列和结果队列
        task = manager.get_task_queue()
        result = manager.get_result_queue()

        #第六步：添加任务
        for url in ["ImageUrl_"+str(i) for i in range(10)]:
            print('put task %s ...' %url)
            task.put(url)

        # 获取返回结果
        print('try get result...')
        for i in range(10):
            print('result is %s' %result.get(timeout=10))
    except:
        print('Manager error')
    finally:
        #关闭管理。一定要关闭，否则会爆管道未关闭的错误
        manager.shutdown()

if __name__ == '__main__':
    #windows下多进程可能会有问题，添加这句可以缓解
    freeze_support()
    win_run()