import redis

# 连接方式1
# r = redis.Redis("127.0.0.1",port=6379) #连接数据库
# # string 类型操作
# r.set('name2',"yinyeli")
# print(r.get("name2").decode(encoding="utf-8"))



"""
redis.py 使用 ConnectionPool 来管理对一个 redis server 的连接
，避免每次建立、释放连接的开销。
默认，每个 Redis 实例都会维护一个自己的连接池。
可以直接建立一个连接池，然后作为参数Redis，这样就可以实现多个Redis实例共享一个连接池。
"""
# 连接方式2
# 使用redis连接池建立连接
pool = redis.ConnectionPool(host="127.0.0.1",port=6379)
r = redis.Redis(connection_pool=pool)
r.set("name3","yinyeli")
print(r.get("name3"))




