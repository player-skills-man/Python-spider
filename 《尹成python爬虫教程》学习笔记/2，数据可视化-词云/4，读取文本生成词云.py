import jieba  # 分割词语
import matplotlib
from matplotlib import pyplot as plt  # 数据可视化
import wordcloud
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS  # 词云
import numpy as np  # 科学计算
from PIL import Image  # 图片处理

# 打开文本
with open("a.txt", encoding="utf-8") as f:
    txt = f.read()  # 读取文本内容
    word_list = jieba.cut_for_search(txt)  # 切割词语
    space_list = " ".join(word_list)  # 连接词语
    print(space_list)  # 打印
    w_c = WordCloud(
        background_color="black",  # 背景颜色
        max_words=20,  # 最多词语数
        font_path="simkai.ttf",  # ***中文字体，解决不能识别中文文字问题
        max_font_size=100,  # 最大字体大小
        random_state=300,  # 随机状态参数
    ).generate(space_list)  # 生成词云

    plt.imshow(w_c)
    plt.axis("off")
    plt.show()
