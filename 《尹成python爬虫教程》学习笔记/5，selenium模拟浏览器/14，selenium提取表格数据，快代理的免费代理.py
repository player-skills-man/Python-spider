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
    driver.get("https://www.kuaidaili.com/free/") # 模拟浏览器访问url
    time.sleep(2)
    tags = driver.find_elements_by_xpath('//*[@id="list"]/table/tbody/tr')
    # 打印一行数据
    # for tag in tags:
    #     print(tag.text)
    #打印索引数据
    serv_list = []
    for tag in tags:
        ip = tag.find_element_by_xpath('./td[1]').text
        port = tag.find_element_by_xpath('./td[2]').text
        serv_list.append(ip+":"+port)
        # print(tag.find_element_by_xpath('./td[1]').text,end=":")
        # print(tag.find_element_by_xpath('./td[2]').text)

        # print(tag.find_elements_by_xpath('./td')[0].text,end=":")
        # print(tag.find_elements_by_xpath('./td')[1].text)
    driver.close() # 关闭模拟器
    driver.quit()

    # 写入文件
    with open("free_serv.txt", "w") as f:
        f.write("\n".join(serv_list))

if __name__ == '__main__':
    do_baidu()