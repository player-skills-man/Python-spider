"""
https://cloud.tencent.com/developer/article/1454120
html里面写了：
 target="_blank"
造成新打开一个窗口，但是selenium不会自动跳转到新的串口，需要自己切换

# 你打开的浏览器，谷歌
browser = webdriver.Chrome()
# 你中间的操作
...
# 获取当前浏览器所有的窗口
handles = browser.window_handles
# handles为一个数组：handles = [窗口1，窗口2，...]
# 窗口切换，切换为新打开的窗口
browser.switch_to_window(handles[-1])
# 切换回最初打开的窗口
browser.switch_to_window(handles[0])
# 新增一个窗口打开url
newwindow='window.open("https://www.baidu.com");'
browser.execute_script(newwindow)
# 关闭当前窗口
browser.close()
# 关闭所有窗口
browser.quit()



博文2：selenium切换窗口的几种方法小结:https://blog.csdn.net/daiyu__zz/article/details/86175177
第一种方法，使用场景——打开多个窗口，需要定位到新打开的窗口；

    # 获取打开的多个窗口句柄
    windows = driver.window_handles
    # 切换到当前最新打开的窗口
    driver.switch_to.window(windows[-1])

第二种方法，使用场景——打开两个窗口，需要定位到新的窗口

    # 获得打开的第一个窗口句柄
    window_1 = driver.current_window_handle
    # 获得打开的所有的窗口句柄
    windows = driver.window_handles
    # 切换到最新的窗口
    for current_window in windows:
        if current_window != window_1:
            driver.switch_to.window(current_window)


两种方法的区别：
1.第一种方法比较简单，能提升整体代码的性能；
2.第二种方法是大家最常用的方法，比较容易理解；
"""

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

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


def do_baidu():
    driver = ChromeDriverBrowser()# 设置driver 模拟浏览器程序
    # driver.set_window_size(300,200) # ！注意，window_size遮住的按钮，是不可以实现模拟鼠标点击操作的。
    driver.get("http://www.baidu.com") # 模拟浏览器访问url

    driver.find_element_by_link_text("登录").click()
    time.sleep(4)
    driver.find_element_by_link_text("立即注册").click()
    time.sleep(4)
    pages = driver.window_handles

    #1, 更改driver选择的页面
    page1 = driver.current_window_handle
    for page in pages:
        if page != page1:
            driver.switch_to.window(page)
    #2,
    # # 获取打开的多个窗口句柄
    # windows = driver.window_handles
    # # 切换到当前最新打开的窗口
    # driver.switch_to.window(windows[-1])

    driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("abcdfg")

    time.sleep(2)  # ！此处sleep不仅是为了观察，还为了足够的时间使driver.page_source的更新
    driver.close() # 关闭模拟器
    driver.quit()

if __name__ == '__main__':
    do_baidu()