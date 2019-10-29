import pymongo

"""
注意：mongodb的特点——
都可以连接。但是密码错误，不可以操作特定的数据库。
"""
# python-mongo 支持直接操作...,这里并没有使用它封装好的函数.
# 对比判断是否登录成功---能否对指定的数据库可操作.
#执行成功
conn = pymongo.MongoClient("mongodb://yyl:123456@127.0.0.1:27017")
db = conn.test
myset = db.myset
myset.insert({"name":"hello mongo"})

#抛出异常
conn2 = pymongo.MongoClient("mongodb://yyl:1234256@127.0.0.1:27017")# 错误密码
db = conn2.test
myset = db.myset
myset.insert({"name":"hello mongo"})


# 使用封装的函数如下所示.
# db = conn.get_database("test")
# myset = db.get_collection("myset")
# myset.insert({"name":"hello mongo"})