import jieba

str = '小明对我说：你好，我也对他说：你好'

word_list = jieba.cut(str,cut_all=True)
print(word_list) # 返回对象word_list是一个生成器
print("/".join(word_list))

word_list2 = jieba.cut_for_search(str)
print("/".join(word_list2))
