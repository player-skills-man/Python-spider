# YYL->READCODE->5.1
# launcher 启动器子服务，是一个spider的任务进程调度器
# 调用runner 脚本，执行cmd命令 crawl myspider ->启动爬虫
import sys
from datetime import datetime
from multiprocessing import cpu_count

from twisted.internet import reactor, defer, protocol, error
from twisted.application.service import Service
from twisted.python import log

from scrapyd.utils import get_crawl_args, native_stringify_dict
from scrapyd import __version__
from .interfaces import IPoller, IEnvironment

class Launcher(Service):

    name = 'launcher'

    def __init__(self, config, app):
        self.processes = {}
        self.finished = []
        self.finished_to_keep = config.getint('finished_to_keep', 100)
        self.max_proc = self._get_max_proc(config)
        self.runner = config.get('runner', 'scrapyd.runner')
        self.app = app

    def startService(self):
        # print("YYL->launcher.py:max_proc->", self.max_proc)# scrapyd.launcher.Launcher
        # 最大进程数 根据cpu自动计算的cpus = cpu_count()
        for slot in range(self.max_proc):
            self._wait_for_project(slot)
        log.msg(format='Scrapyd %(version)s started: max_proc=%(max_proc)r, runner=%(runner)r',
                version=__version__, max_proc=self.max_proc,
                runner=self.runner, system='Launcher')

    # 等待加入任务
    def _wait_for_project(self, slot):
        """
        IPoller： A component that polls for projects that need to run
        IPoller是一个自定义的接口，真正实现的是poller.py中的QueuePoller，
        并且应用了延迟队列from twisted.internet.defer import DeferredQueue
        """

        poller = self.app.getComponent(IPoller)
        poller.next().addCallback(self._spawn_process, slot)

    # 开启一个进程启动爬虫任务,与scrapy的接口处
    def _spawn_process(self, message, slot):
        # message,slot-> {'settings': {}, '_job': 'adb466b4f93311e984bacf50d0e7550f', '_project': 'yuedu163Spider', '_spider': 'myspider'} 0
        msg = native_stringify_dict(message, keys_only=False)
        # msg {'settings': {}, '_job': 'adb466b4f93311e984bacf50d0e7550f', '_project': 'yuedu163Spider', '_spider': 'myspider'}
        project = msg['_project']
        # project yuedu163Spider
        args = [sys.executable, '-m', self.runner, 'crawl']
        # args1-> [.//python.exe', '-m', 'scrapyd.runner', 'crawl']
        args += get_crawl_args(msg)
        # args2 -> [.//python.exe', '-m', 'scrapyd.runner', 'crawl', 'myspider', '-a', '_job=adb466b4f93311e984bacf50d0e7550f']
        e = self.app.getComponent(IEnvironment)
        # e <scrapyd.environ.Environment...>
        env = e.get_environment(msg, slot)
        env = native_stringify_dict(env, keys_only=False)
        """
        #env2 
        {
        'ALLUSERSPROFILE': 'C:\\ProgramData', 
        'APPDATA': 'C:\\Users\\admin\\AppData\\Roaming', 
        'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 
        'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 
        'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 
        'COMPUTERNAME': 'MAC-YYL', 
        'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 
        'DOCKER_TOOLBOX_INSTALL_PATH': 'C:\\Program Files\\Docker Toolbox', 
        'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 
        'FPS_BROWSER_APP_PROFILE_STRING': 'Internet Explorer', 
        'FPS_BROWSER_USER_PROFILE_STRING': 'Default', 
        'HOMEDRIVE': 'C:', 
        'HOMEPATH': '\\Users\\admin', 
        'IDEA_INITIAL_DIRECTORY': 'C:\\Users\\admin\\Desktop', 
        'LOCALAPPDATA': 'C:\\Users\\admin\\AppData\\Local', 
        'LOGONSERVER': '\\\\MAC-YYL', 
        'NUMBER_OF_PROCESSORS': '4', 
        'ONEDRIVE': 'C:\\Users\\admin\\OneDrive', 
        'OS': 'Windows_NT', 
        
        'PATH': 'C:\\WINDOWS\\system32;C:\\WINDOWS;
        C:\\WINDOWS\\System32\\Wbem;
        C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;
        C:\\WINDOWS\\System32\\OpenSSH\\;
        C:\\Program Files\\nodejs\\;
        C:\\Program Files\\Git\\cmd;
        C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\;
        C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python37\\;
        C:\\Users\\admin\\AppData\\Local\\Microsoft\\WindowsApps;;
        C:\\Program Files (x86)\\yyl\\Fiddler;
        C:\\Users\\admin\\AppData\\Roaming\\npm;
        C:\\Users\\admin\\AppData\\Local\\Microsoft\\WindowsApps;
        C:\\Program Files\\JetBrains\\PyCharm 2019.2.3\\bin;;
        C:\\Users\\admin\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;
        C:\\Program Files\\Docker Toolbox;
        C:\\Users\\admin\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages\\pywin32_system32', 
        
        'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 
        'PROCESSOR_ARCHITECTURE': 'AMD64', 
        'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 61 Stepping 4, GenuineIntel', 
        'PROCESSOR_LEVEL': '6', 
        'PROCESSOR_REVISION': '3d04', 
        'PROGRAMDATA': 'C:\\ProgramData', 
        'PROGRAMFILES': 'C:\\Program Files', 
        'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 
        'PROGRAMW6432': 'C:\\Program Files', 
        'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 
        'PUBLIC': 'C:\\Users\\Public', 
        'PYCHARM': 'C:\\Program Files\\JetBrains\\PyCharm 2019.2.3\\bin;', 
        'PYCHARM_DISPLAY_PORT': '63342', 
        'PYCHARM_HOSTED': '1', 
        'PYTHONIOENCODING': 'UTF-8', 
        
        'PYTHONPATH': 'C:\\Users\\admin\\Desktop\\yyl-docs\\pycharm\\Python-spider;
        C:\\Users\\admin\\Desktop\\yyl-docs\\pycharm\\Python-spider\\READCODE;
        C:\\Users\\admin\\Desktop\\yyl-docs\\pycharm\\Python-spider\\READCODE\\scrapyd;C:\\Users\\admin\\Desktop\\yyl-docs\\pycharm\\Python-spider\\READCODE\\scrapy;
        C:\\Program Files\\JetBrains\\PyCharm 2019.2.3\\helpers\\pycharm_matplotlib_backend;
        C:\\Program Files\\JetBrains\\PyCharm 2019.2.3\\helpers\\pycharm_display', 
        
        'PYTHONUNBUFFERED': '1', 
        'SESSIONNAME': 'Console', 
        'SYSTEMDRIVE': 'C:', 
        'SYSTEMROOT': 'C:\\WINDOWS', 
        'TEMP': 'C:\\Users\\admin\\AppData\\Local\\Temp', 
        'TMP': 'C:\\Users\\admin\\AppData\\Local\\Temp', 
        'USERDOMAIN': 'MAC-YYL', 
        'USERDOMAIN_ROAMINGPROFILE': 'MAC-YYL', 
        'USERNAME': 'admin', 
        'USERPROFILE': 'C:\\Users\\admin', 
        'VBOX_MSI_INSTALL_PATH': 'C:\\Program Files\\Oracle\\VirtualBox\\', 
        'WINDIR': 'C:\\WINDOWS', 
        'SCRAPY_SLOT': '0', 
        'SCRAPY_PROJECT': 'yuedu163Spider', 
        'SCRAPY_SPIDER': 'myspider', 
        'SCRAPY_JOB': 'adb466b4f93311e984bacf50d0e7550f', 
        'SCRAPY_LOG_FILE': 'logs\\yuedu163Spider\\myspider\\adb466b4f93311e984bacf50d0e7550f.log'
        }
        """
        # pp = ScrapyProcessProtocol(0,msg['_project'],msg['_spider'],msg['_job'],env)
        pp = ScrapyProcessProtocol(slot, project, msg['_spider'], msg['_job'], env)
        pp.deferred.addBoth(self._process_finished, slot)

        #没有变化： pp <scrapyd.launcher.ScrapyProcessProtocol object...>
        reactor.spawnProcess(pp, sys.executable, args=args, env=env)# 调用这个进程，开始运行spider
        # args->['python.exe', '-m', 'scrapyd.runner', 'crawl', 'myspider', '-a', '_job=6680830af94811e99667cf50d0e7550f']
        # python -m ->run library module as a script
        #sys.executable->.//python.exe
        # 2019-10-28T11:33:20+0800 [-] Process started:  project='yuedu163Spider' spider='myspider' job='adb466b4f93311e984bacf50d0e7550f' pid=2272 log='logs\\yuedu163Spider\\myspider\\adb466b4f93311e984bacf50d0e7550f.log' items=None

        #reactor.spawnProcess <bound method PosixReactorBase.spawnProcess of <twisted.internet.selectreactor.SelectReactor object
        self.processes[slot] = pp

    # 关闭进程,让此进程重回进入等待状态
    def _process_finished(self, _, slot):
        process = self.processes.pop(slot)
        process.end_time = datetime.now()
        self.finished.append(process)
        del self.finished[:-self.finished_to_keep] # keep last 100 finished jobs
        self._wait_for_project(slot)

    # 返回最大进程数
    def _get_max_proc(self, config):
        max_proc = config.getint('max_proc', 0)
        if not max_proc:
            try:
                cpus = cpu_count()
                # print("YYL->launcher.py:cpus->", cpus) # 4
            except NotImplementedError:
                cpus = 1
            max_proc = cpus * config.getint('max_proc_per_cpu', 4)
        return max_proc

# ScrapyProcessProtocol,just for log
class ScrapyProcessProtocol(protocol.ProcessProtocol):

    def __init__(self, slot, project, spider, job, env):
        self.slot = slot
        self.pid = None
        self.project = project
        self.spider = spider
        self.job = job
        self.start_time = datetime.now()
        self.end_time = None
        self.env = env
        self.logfile = env.get('SCRAPY_LOG_FILE')
        self.itemsfile = env.get('SCRAPY_FEED_URI') # scrapyd.conf还未配置，所以上面参数里没有
        self.deferred = defer.Deferred()

    def outReceived(self, data):
        log.msg(data.rstrip(), system="Launcher,%d/stdout" % self.pid)

    def errReceived(self, data):
        log.msg(data.rstrip(), system="Launcher,%d/stderr" % self.pid)

    def connectionMade(self):
        self.pid = self.transport.pid
        self.log("Process started: ")

    def processEnded(self, status):
        if isinstance(status.value, error.ProcessDone):
            self.log("Process finished: ")
        else:
            self.log("Process died: exitstatus=%r " % status.value.exitCode)
        self.deferred.callback(self)

    def log(self, action):
        fmt = '%(action)s project=%(project)r spider=%(spider)r job=%(job)r pid=%(pid)r log=%(log)r items=%(items)r'
        log.msg(format=fmt, action=action, project=self.project, spider=self.spider,
                job=self.job, pid=self.pid, log=self.logfile, items=self.itemsfile)
