import time


start_time = time.perf_counter()

#程序
time.sleep(2)

print("运行时间：",time.perf_counter() - start_time)