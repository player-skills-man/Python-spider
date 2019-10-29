# gevent的使用流程

from gevent import monkey
monkey.patch_all()
import gevent
from urllib.request import urlopen

def run_task(url):
    print ('Visit --> %s' % url)
    try:
        response = urlopen(url)
        data = response.read()
        print ('%d bytes received from %s.' % (len(data), url))
    except Exception as e:
        print (e)
if __name__=='__main__':
    urls = ['https://github.com/','https://www.python.org/','http://www.cnblogs.com/']
    greenlets = [gevent.spawn(run_task, url) for url in urls  ]
    gevent.joinall(greenlets)