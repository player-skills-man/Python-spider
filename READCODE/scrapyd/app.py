# YYL->READCODE->4.1
# 配置app服务，为app运行配置类
import sys

from twisted.application.service import Application
from twisted.application.internet import TimerService, TCPServer
from twisted.web import server
from twisted.python import log
from twisted.cred.portal import Portal
from twisted.web.guard import HTTPAuthSessionWrapper, BasicCredentialFactory

from scrapy.utils.misc import load_object

from .interfaces import IEggStorage, IPoller, ISpiderScheduler, IEnvironment
from .eggstorage import FilesystemEggStorage
from .scheduler import SpiderScheduler
from .poller import QueuePoller
from .environ import Environment
from .config import Config
from .basicauth import PublicHTMLRealm, StringCredentialsChecker

def application(config):
    """
    读取Config类加载的配置文件中的配置项
    设置application的名称、端口、地址、poll_interval（轮训间隔），
    #poll_interval 轮询间隔：在频繁签入和完成某些操作后提供快速周转之间的权衡
    """
    app = Application("Scrapyd")
    http_port = config.getint('http_port', 6800)
    bind_address = config.get('bind_address', '127.0.0.1')
    poll_interval = config.getfloat('poll_interval', 5)

    """
    设置其他server组件IPoller、IEggStorage、ISpiderScheduler、IEnvironment
    """
    poller = QueuePoller(config)
    eggstorage = FilesystemEggStorage(config)
    scheduler = SpiderScheduler(config)
    environment = Environment(config)
    app.setComponent(IPoller, poller)
    app.setComponent(IEggStorage, eggstorage)
    app.setComponent(ISpiderScheduler, scheduler)
    app.setComponent(IEnvironment, environment)

    laupath = config.get('launcher', 'scrapyd.launcher.Launcher')
    laucls = load_object(laupath)
    launcher = laucls(config, app) # launcher 启动器

    """
    print("YYL->app.py:laupath->", laupath)# scrapyd.launcher.Launcher
    print("YYL->app.py:laucls->", laucls) # <class 'scrapyd.launcher.Launcher'>
    print("YYL->app.py:launcher->", launcher) #  <scrapyd.launcher.Launcher object at 0x0000018D75810E88>
    # 上面三行代码相当于
    from scrapyd.launcher import Launcher
    launcher = Launcher(config, app)
    """

    timer = TimerService(poll_interval, poller.poll)

    webpath = config.get('webroot', 'scrapyd.website.Root')
    webcls = load_object(webpath)

    username = config.get('username', '')
    password = config.get('password', '')
    if username and password:
        if ':' in username:
            sys.exit("The `username` option contains illegal character ':', "
                     "check and update the configuration file of Scrapyd")
        portal = Portal(PublicHTMLRealm(webcls(config, app)),
                        [StringCredentialsChecker(username, password)])
        credential_factory = BasicCredentialFactory("Auth")
        resource = HTTPAuthSessionWrapper(portal, [credential_factory])
        log.msg("Basic authentication enabled")
    else:
        resource = webcls(config, app)
        log.msg("Basic authentication disabled as either `username` or `password` is unset")
    # print("YYL->app.py:resource->", resource) #<scrapyd.website.Root object at 0x000001C39A22D808>
    webservice = TCPServer(http_port, server.Site(resource), interface=bind_address)
    log.msg(format="Scrapyd web console available at http://%(bind_address)s:%(http_port)s/",
            bind_address=bind_address, http_port=http_port)

    launcher.setServiceParent(app)
    timer.setServiceParent(app)
    webservice.setServiceParent(app)
    """
    把launcher、timer、webservice配置为app的子服务。
    """
    return app

