from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import requests
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


def do():
    driver = ChromeDriverBrowser()# 设置driver 模拟浏览器程序
    # driver.set_window_size(300,200) # ！注意，window_size遮住的按钮，是不可以实现模拟鼠标点击操作的。
    driver.implicitly_wait(30)  # 隐式等待timeout=30s
    driver.get("https://passport.jd.com/new/login.aspx") # 模拟浏览器访问url

    # 人工操作登录
    time.sleep(5) #预设人工操作时间
    items = driver.find_elements_by_class_name("cate_menu_item")
    if(len(items) > 2):
        print("模拟登录成功！")
    else:
        print("模拟登录失败！")




    # 核心，配置cookies
    # 获取cookies
    cookies = driver.get_cookies()
    req_session = requests.session() # 建立会话
    for cookie in cookies:
        req_session.cookies.set(cookie['name'],cookie['value'])

    driver.close()  # 关闭模拟器
    driver.quit()

    page = req_session.get("https://home.jd.com/").text
    print(page)



if __name__ == '__main__':
    do()