import urllib.request

# 下载url图片
def down_load_img(imgURL,name):
    try:
        urllib.request.urlretrieve(imgURL, name)
        print(name,"下载成功")
    except Exception as e:
        print(name,"下载失败")

if __name__ == '__main__':
    imgURL = "https://img3.doubanio.com/view/ark_article_cover/retina/public/58299442.jpg?v=0"
    down_load_img(imgURL,"1.jpg")