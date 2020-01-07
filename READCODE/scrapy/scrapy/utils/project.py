import os
import pickle
import warnings

from importlib import import_module
from os.path import join, dirname, abspath, isabs, exists

from scrapy.utils.conf import closest_scrapy_cfg, get_config, init_env
from scrapy.settings import Settings
from scrapy.exceptions import NotConfigured, ScrapyDeprecationWarning


ENVVAR = 'SCRAPY_SETTINGS_MODULE'
DATADIR_CFG_SECTION = 'datadir'


def inside_project():
    # 检查此环境变量是否存在(上面已设置)
    scrapy_module = os.environ.get('SCRAPY_SETTINGS_MODULE')
    if scrapy_module is not None:
        try:
            import_module(scrapy_module)
        except ImportError as exc:
            warnings.warn("Cannot import scrapy settings module %s: %s" % (scrapy_module, exc))
        else:
            return True

    # 如果环境变量没有，就近查找scrapy.cfg，找得到就认为是在项目环境中
    """
    scrapy命令有的是依赖项目运行的，有的命令则是全局的，不依赖项目的。
    这里主要通过就近查找scrapy.cfg文件来确定是否在项目环境中。
    """
    return bool(closest_scrapy_cfg())


def project_data_dir(project='default'):
    """Return the current project data dir, creating it if it doesn't exist"""
    if not inside_project():
        raise NotConfigured("Not inside a project")
    cfg = get_config()
    if cfg.has_option(DATADIR_CFG_SECTION, project):
        d = cfg.get(DATADIR_CFG_SECTION, project)
    else:
        scrapy_cfg = closest_scrapy_cfg()
        if not scrapy_cfg:
            raise NotConfigured("Unable to find scrapy.cfg file to infer project data dir")
        d = abspath(join(dirname(scrapy_cfg), '.scrapy'))
    if not exists(d):
        os.makedirs(d)
    return d


def data_path(path, createdir=False):
    """
    Return the given path joined with the .scrapy data directory.
    If given an absolute path, return it unmodified.
    """
    if not isabs(path):
        if inside_project():
            path = join(project_data_dir(), path)
        else:
            path = join('.scrapy', path)
    if createdir and not exists(path):
        os.makedirs(path)
    return path


def get_project_settings():
    # 环境变量中是否有SCRAPY_SETTINGS_MODULE配置
    # print(os.environ)
    # print("SCRAPY_SETTINGS_MODULE in the environ? ",os.environ.get(ENVVAR))
    if ENVVAR not in os.environ:
        project = os.environ.get('SCRAPY_PROJECT', 'default') # os.environ 返回有关系统的各种信息
        # 系统没有SCRAPY_PROJECT键值,project = default.
        # print(project) # default

        # 初始化环境,找到用户配置文件settings.py,设置到环境变量SCRAPY_SETTINGS_MODULE中
        init_env(project) # 环境path中加入用户自己编写的爬虫项目project-dir，以便scrapy命令可以找到这个模块
        # print(project) # default
        """
        init_env:
        Initialize environment to use command-line tool from inside a project
            dir. This sets the Scrapy settings module and modifies the Python path to
            be able to locate the project module.
        """
        # print(os.environ)

    # 加载默认配置文件default_settings.py，生成settings实例
    """
    默认配置文件default_settings.py是非常重要的，个人认为还是有必要看一下里面的内容，
    这里包含了所有默认的配置，例如调度器类、爬虫中间件类、下载器中间件类、下载处理器类等等.
    
    在这里就能隐约发现，scrapy的架构是非常低耦合的，所有组件都是可替换的，什么是可替换呢？
    例如，你觉得默认的调度器功能不够用，那么你就可以按照它定义的接口标准，自己实现一个调度器，
    然后在自己的配置文件中，注册自己写的调度器模块，那么scrapy的运行时就会用上你新写的调度器模块了！
    ---只要在默认配置文件中配置的模块，都是可替换的---
    """
    settings = Settings()
    # 取得用户配置文件
    settings_module_path = os.environ.get(ENVVAR)
    # 更新配置，用户配置覆盖默认配置
    if settings_module_path:
        settings.setmodule(settings_module_path, priority='project')
        # 如果环境变量中有其他scrapy相关配置则覆盖

    # XXX: remove this hack
    pickled_settings = os.environ.get("SCRAPY_PICKLED_SETTINGS_TO_OVERRIDE")
    if pickled_settings:
        warnings.warn("Use of environment variable "
                      "'SCRAPY_PICKLED_SETTINGS_TO_OVERRIDE' "
                      "is deprecated.", ScrapyDeprecationWarning)
        settings.setdict(pickle.loads(pickled_settings), priority='project')

    # XXX: deprecate and remove this functionality
    env_overrides = {k[7:]: v for k, v in os.environ.items() if
                     k.startswith('SCRAPY_')}
    if env_overrides:
        settings.setdict(env_overrides, priority='project')

    return settings
