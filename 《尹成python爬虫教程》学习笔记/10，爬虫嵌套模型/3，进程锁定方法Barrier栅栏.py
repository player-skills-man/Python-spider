import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time,sleep
from datetime import datetime

def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("process %s ----> %s" %(name, datetime.fromtimestamp(now)))

def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s" %(name, datetime.fromtimestamp(now)))



if __name__ == "__main__":
    # create a barrier and lock.
    synchronizer = Barrier(3)# 设置barrier最大wait数
    serializer = Lock()
    # create four processes
    Process(name='p1.1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p2 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p3 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p5 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p1.2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p6 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p7 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p8 - test_without_barrier', target=test_without_barrier).start()
    sleep(10)
    print("waiting barrier 达到3") # wait数达到3后，会统一执行.
    Process(name='p1.3 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()

    sleep(5)

    Process(name='p1.1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p2 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p3 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p5 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p1.2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p6 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p7 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p8 - test_without_barrier', target=test_without_barrier).start()
    sleep(10)
    print("waiting barrier 达到6")  # wait数达到3后，会统一执行
    Process(name='p1.3 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
