# encoding=utf-8
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from PIL import Image
from GET_headers import getheaders

# 无界面模式
def ChromeDriverNOBrowser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driverChrome = webdriver.Chrome(executable_path="./tools/chromedriver", chrome_options=chrome_options)
    return driverChrome


# 有界面的就简单了
def ChromeDriverBrowser():
    driverChrome = webdriver.Chrome("./tools/chromedriver")
    return driverChrome



def get_snap(driver):  # 对目标网页进行截屏。这里截的是全屏
    driver.save_screenshot('full_snap.png')
    page_snap_obj=Image.open('full_snap.png')
    return page_snap_obj


def get_image(driver):  # 对验证码所在位置进行定位，然后截取验证码图片
    img = driver.find_element_by_id('address')
    time.sleep(2)
    location = img.location
    print(location)
    size = img.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']

    page_snap_obj = get_snap(driver)
    image_obj = page_snap_obj.crop((left, top, right, bottom))
    image_obj.show()
    image_obj.save("1.png")
    return image_obj  # 得到的就是验证码



def get_page():
    driver = ChromeDriverBrowser()  # 设置driver 模拟浏览器程序
    options = webdriver.ChromeOptions()
    # 更换头部
    user_agent = getheaders()
    options.add_argument('user-agent=%s' % user_agent)
    driver.get("http://www.dianping.com/shop/97141937")  # 模拟浏览器访问url
    get_image(driver)




    driver.close()  # 关闭模拟器



if __name__ == '__main__':
    get_page()
