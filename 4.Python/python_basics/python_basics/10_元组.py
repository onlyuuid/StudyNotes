"""
元组:
    1.元组中的元素不能修改
    2.元组使用小括号()定义, 列表使用方括号[]定义
    3.创建元组只需要在小括号中添加元素即可, 元素之间用逗号分隔
"""
tup1 = ('google','百度','阿里',12)
tup2 = (1,2,3,4)
tup3 = "hello","world"  # 不用括号也可以
print(type(tup3))

# 定义一个空元组
# 元组中只包含一个元素时, 需要在元素的后面添加逗号(,),否则括号会被当做运算符使用:
tup5 = (3,)

# 元组和字符串类似, 下标从0开始, 可以进行截取, 组合等.
tup6 = ('google','百度','阿里',12,43)
print(tup6[0])
print(tup6[1:-2])

# 修改元组
# 元组中的元素是不允许改变的, 但是可以对元组进行连接组合
tup6 = (1,2)
tup7 = (3,4)
tup8 = tup6 + tup7
print(tup8)

# 删除元组
# 元组中的值是不允许删除的, 但我们可以使用del语句删除整个元组

tup9 = (1,2,3,4,5)
del tup9

# 元组运算符
# 元组之间可以使用+, +=和*进行运算, 这就意味着它们可以进行组合和重复
len((1,2,3,4,5))     #  3                       计算元素个数
a = (1,2)
b = (3,4)
c = a + b
print(c) # (1, 2, 3, 4) c 作为新元组, 它包含了a和b的所有元素

d = ('hi',)
print(d * 4) # ('hi', 'hi', 'hi', 'hi') 复制

e = ('do','hi','you')
print('do' in e)  # True  元素是否存在

f = (1,2,3,4,5,6)
for i in f:
    print(i)        # 迭代

# 元组索引, 截取
tup = ('google','runoob','taobao','jingdong','weibo')
print(tup[0]) # 索引
print(tup[1:]) # 截取
print(tup[:-2])

# 元组内置函数
"""
len(tup)            计算元组的长度
max(tuple)          返回元组中元素最大值
min(tuple)          返回元组中元素最小值
tuple(iterable)     将可迭代系列转换为元组
"""
list = [1,2,3,4,5,6,"89"]
tup = tuple(list)
print(tup) # (1, 2, 3, 4, 5, 6, '89')

# 关于元组是不可变的
# 所谓元组的不可变指的是元组所指向的内存中的内容不可变
tup9 = ('t','u','p','l','e')
# tup9[0] = 1
# print(tup9)
"""
Traceback (most recent call last):
  File "D:\Case Code\4.Python\python_basics\python_basics\元组.py", line 73, in <module>
    tup9[0] = 1
    ~~~~^^^
TypeError: 'tuple' object does not support item assignment
"""
print(id(tup9)) # 2505636621552 内存地址
tup9 = ('t','u','p','l','l')
print(id(tup9)) # 2527823704320 内存地址不一样了



