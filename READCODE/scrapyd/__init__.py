# YYL->READCODE->3
# 引入了两个外部元素load_project Config

# pkgutil 扩展包工具,为特定的包添加模块搜索路径，并使用包中包含的资源。
import pkgutil

# 读取版本文件，设置version_info
__version__ = pkgutil.get_data(__package__, 'VERSION').decode('ascii').strip()
version_info = tuple(__version__.split('.')[:3])


'''
# 导入外部包scrapy,引用函数load_object
# 导入配置文件，引用配置文件的类Config
# 实现了config和appfunc的可自定义
# 这个代码就是下面代码的精简版
import scrapyd.app
from scrapyd.config import Config
def get_application(config=None):
    if config is None:
        config =Config()
    return scrapyd.app.application(config)
'''
from scrapy.utils.misc import load_object
from scrapyd.config import Config

def get_application(config=None):
    """自定义：这里可以自定义Config类"""
    if config is None:
        config = Config()

    """
    自定义：这里可以自定义apppath，自定义替代scrapyd.app.application
    # 定义了返回app的函数为scrapyd.app.application
    # 使用,传入函数路径scrapyd.app.application，返回一个对象
    
    scrapy的load_object 的源码如下：
    Load an object given its absolute object path, and return it.
    object can be a class, function, variable or an instance.
    path ie: 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware'
    
    核心代码：
    module, name = path[:dot], path[dot+1:]
    mod = import_module(module)
    obj = getattr(mod, name)
    return obj
    """
    apppath = config.get('application', 'scrapyd.app.application')
    appfunc = load_object(apppath)
    # print("YYL->apppath=",apppath,type(apppath))
    # print("YYL->appfunc=",appfunc,type(appfunc))
    # apppath= scrapyd.app.application <class 'str'>
    #appfunc= <function application at 0x00000215348A74C8> <class 'function'>
    # 此处的appfunc就是scrapyd.app.application，并且可调用
    return appfunc(config)

