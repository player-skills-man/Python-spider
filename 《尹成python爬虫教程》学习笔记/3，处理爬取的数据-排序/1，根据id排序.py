
def isNum(str):
    try:
        int(str) # 此处不能使用eval,因为有id
        return True
    except Exception:
        return False
    finally:
        pass

lines_list = [] # 存储二维列表
with open("shares.txt",encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        lines_list.append(line.split(','))
    # print(lines_list)

# 过滤不规则数据
for line in lines_list:
    if isNum(line[0]):
        pass
        # print(line)
    else:
        lines_list.remove(line)

# print(lines_list)

# 为二维列表line_list排序
rule = lambda x:eval(x[0])
lines_list.sort(key=rule,reverse=True)
print(lines_list)