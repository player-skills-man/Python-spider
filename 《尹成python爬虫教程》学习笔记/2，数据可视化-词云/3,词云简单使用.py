import wordcloud

word_cloud = wordcloud.WordCloud()		#配置对象参数
word_cloud.generate("hello world hello PUA hello yyl")  # 加载词云文本
word_cloud.to_file("ciyun.png")