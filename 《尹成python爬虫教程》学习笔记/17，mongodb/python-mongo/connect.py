import pymongo


conn = pymongo.MongoClient(host="localhost",port=27017)
testdb = conn.get_database("test")

collections = conn['informations']
# print(type(collections),collections)


