'''
Python中使用lambda来创建匿名函数
lambda函数是一种小型, 匿名的, 内联函数, 它可以具有任意数量的参数, 但只能有一个表达式.
匿名函数不需要使用def关键字定义完整函数.
lambda通常用于编写简单的, 单行的函数, 通常在需要函数作为参数传递的情况下使用, 例如在map(), filter(),
reduce()等函数中.
特点:
    1.lambda函数是匿名的, 它们没有函数名称, 只能通过赋值给变量或作为参数传递给其他函数来使用
    2.lambda函数通常只包含一行代码, 这使得它们适用于编写简单的函数.
语法特点:
lambda args: expression
'''

# 例1
a = lambda x, y: x + y # 求x, y的和
print(a(4, 5))  # 9

# 例2
li = [1, 2, 3, 4, 5]
a2 = list(map(lambda x: x ** 2, li))
print(a2) # [1, 4, 9, 16, 25]

# 例3
li2 = [1, 2, 3, 4, 5]
a3 = list(filter(lambda x: x % 2 == 0, li2))
print(a3) # [2, 4]

# 例4
from functools import reduce
li3 = [1, 2, 3, 4, 5]
a4 = reduce(lambda x,y: x * y, li3)
print(a4) # 120