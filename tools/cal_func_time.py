import time


# 计算函数运行时间的装饰器
def func_time(func):
    def call_fun(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('函数%s耗时：%s秒' % (func.__name__, int(end_time - start_time)))

    return call_fun


@func_time
def test():
    for i in range(10):
        print(i)
        time.sleep(0.5)


if __name__ == '__main__':
    test()
