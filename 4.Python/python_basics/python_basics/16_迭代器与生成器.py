"""
    迭代器与生成器
        迭代是Python最强大的功能之一, 是访问集合元素的一种方式.
        迭代器是一个可以记住遍历位置的对象.
        迭代器对象从集合的第一个位置开始访问, 直到所有的元素被访问完结束. 迭代器只会前进不会后退.
        迭代器有两个基本的方法, iter()和next().
        字符串, 列表或元组对象都可以用于创建迭代器.
"""

# 1.列表使用迭代器
list = [1,2,3,4]
it = iter(list)
print(next(it))
print(next(it))

for i in it:  # 使用for遍历迭代器
    print(i)
print("===================")
# 2.集合使用迭代器
set = {'a','b','c','d','e','f','g','h','i','j'}
itset = iter(set)

print(next(itset))
print(next(itset))
print(next(itset))

for i in itset:
    print(i)

print("===================")

# 3.创建一个迭代器
class MyNumbers:

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        x = self.i
        self.i += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter)) # 1
print(next(myiter)) # 2
print(next(myiter)) # 3
print(next(myiter)) # 4

# 4.StopIteration
"""
StopIteration 异常用于标识迭代的完成, 防止出现无限循环的情况, 在 __next()__方法中我们可以设置在完成指定循环次数后触发StopIteration异常来结束循环
"""

class MyNumbers2:

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        if self.i <= 20:
            x = self.i
            self.i += 1
        else:
            raise StopIteration  # 停止迭代
        return x
print("============================1")
a = MyNumbers2()
it2 = iter(a)
for i in it2:
    print(i)
print("==========================")
# 5.生成器
"""
在Python中使用了yield的函数被称为生成器, 本质上, 生成器返回的就是迭代器
"""
def countdown(n):
    while n > 0:
        yield n
        n -= 1

generate = countdown(5)

print(next(generate))
print(next(generate))
print(next(generate))

for i in generate:
    print(i)

print("==========================3")
# # 斐波那契数列
def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if (counter > n):
            return
        yield a
        a,b = b,a+b
        counter += 1

f = fibonacci(10)
for i in f:
    print(i,end=" ")  # 0 1 1 2 3 5 8 13 21 34 55






















