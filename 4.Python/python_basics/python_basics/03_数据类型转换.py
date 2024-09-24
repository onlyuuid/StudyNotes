"""
数据类型转换
    有时候, 我们需要对数据内置的类型进行转换, 数据类型的转换, 一般情况下只需要将数据类型作为函数名即可.
    Python数据类型转换可以分为两种:
        隐式类型转换 - 自动完成
        显式类型转换 - 需要使用类型函数来完成
"""
# 1. 隐式类型转换
"""
    在隐式类型转换中, Python会自动将一种数据类型转换为另一种数据类型, 不需要我们去干预.
    以下实例中, 我们对两种不同类型的数据进行运算, 较低数据类型(整型)就会转换为较高数据类型(浮点型)以避免数据丢失.
"""
num = 123
num2 = 1.23
result = num + num2

print("num的数据类型为: ",type(num))
print("num2的数据类型为: ",type(num2))
print("值为: ",result)  # 124.23
print("result的数据类型为: ",type(result))
"""
num的数据类型为:  <class 'int'>
num2的数据类型为:  <class 'float'>
值为:  124.23
result的数据类型为:  <class 'float'>
"""
# 在上述实例中, result为float类型, 这是因为Python会将较小的数据类型转换为较大的数据类型, 以避免数据丢失.

"""
 再看一个实例, 整型数据与字符串类型的数据进行相加:
"""
a = 123
b = "456"
# c = a + b

print("类型a: ",type(a))
print("类型b: ",type(b))
# print("值",c)
# print("类型c",type(c))
"""
Traceback (most recent call last):
  File "D:\Case Code\4.Python\python_basics\python_basics\数据类型转换_03.py", line 34, in <module>
    c = a + b
        ~~^~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
从上述错误可以看出, 整型和字符串类型运算会报错, 输出ErrorType. Python在这种情况下无法使用隐式转换.
但是, Python为这些类型的情况提供了一种解决方案, 称为显示转换.
"""

# 2.显式类型转换
"""
    在显式类型转换中, 用户将对象的数据类型转换为所需的数据类型. 我们使用int(), float(), str()等预定义函数来执行显式类型转换.
"""
# int()强制转换为整型
print("num的类型是:", type(int(2.5)),"值为:",int(2.5))
print("num的类型是:", type(int("123")),"值为:",int("123"))

# float()强制转换为浮点型
x = float(1)
y = float(3.23)
z = float("123")
v = float(True)

print(x)
print(y)
print(z)
print(v)
"""
1.0
3.23
123.0
1.0
"""

# str()强制转换为字符串类型
d = str(12)
f = str(3.23)
g = str(False)

print(d,type(d))
print(f,type(f))
print(g,type(g))
"""
12 <class 'str'>
3.23 <class 'str'>
False <class 'str'>
"""

# 以下几个内置的函数可以执行类型之间的切换. 这些函数返回一个新的对象, 表示转换的值.
"""
        函数                  值
    int(x[,base])       将x转换为一个整数
    float(x)            将x转换为一个浮点数
    complex(x[,imag])   创建一个复数
    str(x)              将对象x转换为一个字符串
    repr(x)             将对象x转换为表达式字符串
    eval(str)           用来计算在字符串中的有效Python表达式, 并返回一个对象       
    tuple(s)            将序列s转换为一个元组
    list(s)             将序列s转换为一个列表
    set(s)              将序列s转换为可变集合
    dict(d)             创建一个字典, d必须是(key,value)的元组序列
    frozenset(s)        转换为不可变集合
    chr(x)              将一个整数转换为一个字符串
    ord(x)              将一个字符串转换为它的整数值
    hex(x)              将一个整数转换为一个十六进制字符串
    oct(x)              将一个整数转换为一个十八进制字符串
"""