# YYL->NUM->1
#!/usr/bin/env python

from twisted.scripts.twistd import run
from os.path import join, dirname
from sys import argv
import scrapyd

'''
这个main相当于命令行替代,然后调用了run()启动服务器。
只传递了一个自定义的参数txapp.py
接下来分析txapp.py文件
'''

def main():
    # argv[1:1] =这条语句的作用就是生成cmd命令行命令，供在run(runApp, ServerOptions)函数中调用
    # ./scrapyd_run.py -n -y ./txapp.py
    argv[1:1] = ['-n', '-y', join(dirname(scrapyd.__file__), 'txapp.py')]
    # print("YYL->scrapyd_run.py:argvtest.py->参数:argv= "+" ".join(argv))

    #run()是twisted启动服务器
    # print("YYL->scrapyd_run.py文件:argvtest.py->run(),启动服务器")
    run()
    # print("YYL->scrapyd_run.py:argvtest.py->run(),end run() func")

if __name__ == '__main__':
    main()
