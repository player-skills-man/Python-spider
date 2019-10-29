import selenium
import selenium.webdriver
import selenium.webdriver.common.keys
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


def get_baidu_search_res_title_list(word):
    driver = ChromeDriverBrowser()# 设置driver 模拟浏览器程序
    # driver.set_window_size(300,200) # ！注意，window_size遮住的按钮，是不可以实现模拟鼠标点击操作的。
    driver.get("http://www.baidu.com") # 模拟浏览器访问url

    # 获取输入框
    input = driver.find_element_by_id('kw')
    input.clear()  # 清空输入框
    input.send_keys('{}'.format(word))  # 输入搜索内容

    # 模拟输入回车键，如下:
    input.send_keys(selenium.webdriver.common.keys.Keys.ENTER)

    driver.implicitly_wait(4)# 隐式等待4s
    '//*[@id="3001"]/div[1]/h3/a'
    title_list = [] # 存储标题信息
    list = driver.find_elements_by_xpath('//div/h3/a')
    for title in list:
        title_list.append(title.text)
    driver.close()  # 关闭模拟器
    return title_list

if __name__ == '__main__':
    title_list = get_baidu_search_res_title_list("Python")
    print(title_list)