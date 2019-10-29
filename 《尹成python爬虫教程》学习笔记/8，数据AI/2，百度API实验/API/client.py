from aip import AipOcr,AipSpeech,AipFace

""" 你的 APPID AK SK """
APP_ID = ''
API_KEY = 'x'
SECRET_KEY = 'x'

def get_Ocr_client():
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    return client

def get_Speech_client():
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    return client

def get_Face_client():
    client = AipFace(APP_ID, API_KEY, SECRET_KEY)
    return client