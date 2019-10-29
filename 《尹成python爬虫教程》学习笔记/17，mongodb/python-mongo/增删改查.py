import pymongo


client = pymongo.MongoClient(host="localhost",port=27017)
db = client['test'] #取得数据库
print(db)

collection = db['mycollection'] # 取得集合
print(collection)

# 插入文档
collection.insert({"name":"python","data":[1,2,3,4,5,6]})

# 遍历集合中的所有文档
for data in collection.find():
    print(data)

# # 删除一个文档
# collection.delete_one({"name":"python"})
# # collection.delete_many({"name":"python"}) # 删除所有匹配的文档
# print("delete one")
#
# # 遍历集合中的所有文档
# for data in collection.find():
#     print(data)


# 替换/修改
collection.find_one_and_update({"name":"python"},{"$set":{"name":"Java and CPP"}})
print("update one")
# 遍历集合中的所有文档
for data in collection.find():
    print(data)


