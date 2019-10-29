print(eval('id'))
#打印：<built-in function id> （内置函数id）
# 只要是内置函数str,eval('内置函数名')都不会报错，不会抛出异常

print(dir(__builtins__))
print(eval('BaseException'))


'''
eval在python什么意思:
eval是Python的一个内置函数，这个函数的作用是，返回传入字符串的表达式的结果。
即变量赋值时，等号右边的表示是写成字符串的格式，将这个字符串作为eval的参数，eval的返回值就是这个表达式的结果。
eval()函数将字符串str当成有效的表达式来求值并返回计算结果。结合math当成一个计算器很好用。

eval的语法格式如下：
eval(expression[, globals[, locals]])
expression ： 字符串
globals ： 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
locals ： 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

python中eval函数的用法十分的灵活，但也十分危险，安全性是其最大的缺点。
强大之处在于：给个字符串给eval，eval给你一个表达式返回值。


关于eval更多黑客利用和exec的辨析：https://blog.csdn.net/weixin_42232219/article/details/88968787
'''
#**************强大********************
# 执行一个表达式
print(eval('[1,2,3,4,5]*3'))

# 深拷贝id变了
a = [1,2,3,4,5]
b = eval(str(a))
print(b)
print(id(a))
print(id(b))


#**************危险之处！！！********************
#可以将字符串转成表达式并执行，就可以利用执行系统命令，删除文件等操作。假设用户恶意输入。
eval("__import__('os').system('dir')") # 执行系统命令
eval("__import__('os').system('whoami')") # 查看系统


#exec的简单使用
"""
查看exec的源码文档：
    Execute the given source in the context of globals and locals.

    The source may be a string representing one or more Python statements
    or a code object as returned by compile().
    The globals must be a dictionary and locals can be any mapping,
    defaulting to the current globals and locals.
    If only globals is given, locals defaults to it.
"""

a = 1
exec('a += 1')
print("a = ",a)

exec("__import__('subprocess').getoutput('whoami')") # 并不执行，安全性有保障