from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

# 等待页面加载完成
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


def get_baidu_search_res_page(word):
    driver = ChromeDriverBrowser()# 设置driver 模拟浏览器程序
    # driver.set_window_size(300,200) # ！注意，window_size遮住的按钮，是不可以实现模拟鼠标点击操作的。
    driver.get("http://www.baidu.com") # 模拟浏览器访问url

    #显示等待,最多等待10秒
    # wait = WebDriverWait(driver, 10)
    # input = wait.until(EC.presence_of_element_located((By.ID, 'kw')))
    # button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'btn self-btn bg s_btn')))

    # # 隐式等待,最多等待10秒
    # driver.implicitly_wait(10)

    # 获取输入框
    input = driver.find_element_by_id('kw')
    input.clear()  # 清空输入框
    input.send_keys('{}'.format(word))  # 输入搜索内容

    submit = driver.find_element_by_xpath('//*[@id="su"]')# 获取【搜索】按钮
    submit.click()  # 模拟鼠标点击
    # 或者模拟输入回车键，如下:
    # input.send_keys(selenium.webdriver.common.keys.Keys.ENTER)

    time.sleep(1)  # ！此处sleep不仅是为了观察，还为了足够的时间使driver.page_source的更新
    page_source = driver.page_source
    driver.close() # 关闭模拟器
    return page_source

if __name__ == '__main__':
    res = get_baidu_search_res_page("Python")
    print(res)