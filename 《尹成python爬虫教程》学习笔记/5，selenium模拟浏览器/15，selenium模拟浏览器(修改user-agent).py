"""
一个测试网址：
http://www.httpbin.org/

http://www.httpbin.org/user-agent 访问这个url返回user-agent信息

"""

import time
from selenium import webdriver

options = webdriver.ChromeOptions()

# 更换头部
user_agent = ("Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X)"+
        " AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25")
options.add_argument('user-agent=%s' % user_agent)
'''
# 设置图片不加载
prefs = {
    'profile.default_content_setting_values': {
        'images': 2
    }
}
options.add_experimental_option('prefs', prefs)
# 或者  使用下面的设置, 提升速度
options.add_argument('blink-settings=imagesEnabled=false')

# 设置代理
options.add_argument('proxy-server=' + '192.168.0.28:808')
'''


driver = webdriver.Chrome(executable_path="./tools/chromedriver.exe",chrome_options=options)
driver.get('http://www.httpbin.org/user-agent')
driver.get_screenshot_as_file("user-agent.jpg")
time.sleep(5)
driver.close()
