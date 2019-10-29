from API.client import get_Face_client
import imgbase64,base64
from urllib.parse import urlencode
client = get_Face_client()

# 图片按要求编码
def get_img_content(path):
    with open(path, 'rb') as f:
        image = base64.b64encode(f.read())
        image64 = str(image,'utf-8')
        return image64

'''
def get_img_content2(path):
    return imgbase64.file2base64(path)

def test(path):
    print(get_img_content(path))
    print(get_img_content2(path))
test('0.jpg')

# /9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQ
# data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD

#经测试发现，imgbase64.file2base64(path)base后，多出一块数据data:image/jpeg;base64,
'''
import re
def get_img_content2(path):
    reStr = '[\s\S]+?base64,([\s\S]+)'
    regex = re.compile(reStr)
    res = regex.findall(imgbase64.file2base64(path))[0]
    return res

imageType = "BASE64"
""" 调用人脸检测 """
res = client.detect(get_img_content2("0.jpg"), imageType)
print(res)

# """ 如果有可选参数 """
# options = {}
# options["face_field"] = "age"
# options["max_face_num"] = 2
# options["face_type"] = "LIVE"
# options["liveness_control"] = "LOW"
#
# """ 带参数调用人脸检测 """
# client.detect(image, imageType, options)

