from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains

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

    # 模拟鼠标移到指定元素位置
    above = driver.find_element_by_link_text('设置')
    ActionChains(driver).move_to_element(above).perform()#悬浮=鼠标停留
    # ActionChains(driver).move_to_element(above).move_to_element(e2) # 再移动
    # ActionChains(driver).move_to_element(above).click() # 单击
    # ActionChains(driver).move_to_element(above).double_click()  # 双击
    # ActionChains(driver).move_to_element(above).drag_and_drop(e2)  # 拖放

    time.sleep(2)
    driver.close() # 关闭driver



if __name__ == '__main__':
    do_browser()