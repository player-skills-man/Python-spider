from API.client import get_Speech_client
client = get_Speech_client()

result  = client.synthesis('我爱你，就像老鼠爱大米', 'zh', 1, {
    'vol': 5,'per':0
})

# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)
else:
    print("错误！")
    print(result)

from playsound import playsound
playsound('audio.mp3')