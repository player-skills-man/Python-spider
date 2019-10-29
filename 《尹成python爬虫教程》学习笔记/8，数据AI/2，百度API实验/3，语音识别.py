from API.client import get_Speech_client

client = get_Speech_client()

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
res = client.asr(get_file_content('talk.wav'), 'wav', 16000, {
    'dev_pid': 1536,
})

print(res)