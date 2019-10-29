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
    time.sleep(2)

    # 操作cookie
    #查看源文档add_cookie
    cookie = {'name' : 'yyl_age', 'value' : '24'}
    driver.add_cookie(cookie)

    cookies = driver.get_cookies()
    for cookie in  cookies:
        print(cookie)

    time.sleep(2)  # ！此处sleep不仅是为了观察，还为了足够的时间使driver.page_source的更新
    driver.close() # 关闭模拟器
    driver.quit()

if __name__ == '__main__':
    do_baidu()