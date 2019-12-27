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
    scrapy_module = os.environ.get('SCRAPY_SETTINGS_MODULE')
    if scrapy_module is not None:
        try:
            import_module(scrapy_module)
        except ImportError as exc:
            warnings.warn("Cannot import scrapy settings module %s: %s" % (scrapy_module, exc))
        else:
            return True
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
    if ENVVAR not in os.environ:
        project = os.environ.get('SCRAPY_PROJECT', 'default') # os.environ 返回有关系统的各种信息
        # 系统没有SCRAPY_PROJECT键值,project = default.
        # print(project) # default
        init_env(project) # 环境path中加入用户自己编写的爬虫项目project-dir，以便scrapy命令可以找到这个模块
        # print(project) # default
        """
        init_env:
        Initialize environment to use command-line tool from inside a project
            dir. This sets the Scrapy settings module and modifies the Python path to
            be able to locate the project module.
        """
        print(os.environ)


    settings = Settings()
    settings_module_path = os.environ.get(ENVVAR)
    if settings_module_path:
        settings.setmodule(settings_module_path, priority='project')

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
