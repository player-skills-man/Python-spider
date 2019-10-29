'''
自定义排序规则---：
'''

import random

def get_level(xueli):
    if("博士"==xueli):
        return 6
    elif("硕士"==xueli):
        return 5
    elif ("本科" == xueli):
        return 4
    elif ("专科" == xueli):
        return 3
    elif ("高中" == xueli):
        return 2
    elif ("初中" == xueli):
        return 1
    else:
        return 0

xue_list = ['博士','硕士','本科','专科','高中','初中']

data_set = [xue_list[random.randint(0,5)] for i in range(50)]
print(data_set)

# 使用自定义排序规则---key=get_level
print(sorted(data_set, key=get_level))