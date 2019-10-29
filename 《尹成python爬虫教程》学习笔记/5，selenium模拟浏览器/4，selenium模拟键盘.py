from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

# 无界面模式
def ChromeDriverNOBrowser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driverChrome = webdriver.Chrome(executable_path="./tools/chromedriver.exe", chrome_options=chrome_options)
    return driverChrome


# 有界面的就简单了
def ChromeDriverBrowser():
    driverChrome = webdriver.Chrome("./tools/chromedriver.exe")
    return driverChrome


def do_browser():
    driver = ChromeDriverBrowser()# 设置driver 模拟浏览器程序
    # driver.set_window_size(300,200) # ！注意，window_size遮住的按钮，是不可以实现模拟鼠标点击操作的。
    driver.get("http://www.baidu.com") # 模拟浏览器访问url

    # 获取输入框
    input = driver.find_element_by_id('kw')
    input.clear()  # 清空输入框
    input.send_keys("hello") # 字符串
    time.sleep(2)
    input.send_keys(Keys.BACK_SPACE) # 特殊键
    time.sleep(2)
    input.send_keys(Keys.CONTROL,"a") # 组合键
    time.sleep(2)


    driver.close() # 关闭driver



if __name__ == '__main__':
    do_browser()