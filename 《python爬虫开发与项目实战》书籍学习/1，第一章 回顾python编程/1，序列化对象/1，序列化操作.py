try:
    import cPickle as pickle
except ImportError:
    import pickle

# 序列化对象
d = dict(name="小明",age=23,sex="男",grilfriend="小红")
print("打印对象信息：",d)
with open("se.txt","wb") as file:
    pickle.dump(d,file)


# 反序列化对象
with open("se.txt","rb") as file2:
    obj = pickle.load(file2)

print("获取文件中的对象：",obj)