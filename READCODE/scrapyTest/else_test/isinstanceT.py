# encoding=utf-8

class A:
    pass


class B(A):
    pass


# type 与 isinstance区别
print(isinstance(A(), A))  # returns True
print(type(A()) == A)  # returns True

print(isinstance(B(), A))  # returns True 继承也是相同类型
print(type(B()) == A)  # returns False 严格类的判定

a = 2
print(isinstance(a, (str, int, list)))  # 是元组中的一个返回 True
