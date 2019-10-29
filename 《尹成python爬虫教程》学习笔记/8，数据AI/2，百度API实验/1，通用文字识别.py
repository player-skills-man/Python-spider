'''
# url = "http//www.x.com/sample.jpg"
#
# """ 调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url)
#
# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url, options)
'''
from API.client import get_Ocr_client
client = get_Ocr_client()



""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('2.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
# response = client.basicGeneral(image)
response = client.handwriting(image) # 手写识别
# print(response)

words_result = response.get('words_result')
txt = ""
for item in words_result:
    txt += item["words"]
print("->",txt)

# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "CHN_ENG"
# options["detect_direction"] = "true"
# options["detect_language"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为本地图片 """
# client.basicGeneral(image, options)



