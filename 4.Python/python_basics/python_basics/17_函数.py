"""
 函数
    函数是组织好的, 可重复使用的, 用来实现单一, 或相关联功能的代码段
"""

# 函数定义
"""
def 函数名(参数1,参数2):
    执行代码
    return 返回数据
"""

# 例1:
def run():
    return "hello world!" # 返回一个字符串

s = run()
print(s) # hello world!

# 例2: 带参函数
def get_info(name,age):
    return f"我叫{name},今年{age}岁!"

info = get_info('李四',17)
print(info) # 我叫李四,今年17岁!

# 例3: 获取最大值
def max(a,b):
    if a > b:
        return a
    else:
        return b

m = max(6,3)
print(m) # 6

# 例4: 计算矩形面积
def get_acreage(width,height):
    return width * height

s = get_acreage(10,20)
print('面积为:',s)  # 200
from math import pi
print(pi)

print("===================================================")
# 1.必须参数
'''
必须参数须以正确的顺序传入函数. 调用时的数量必须跟声明时的一样.
'''
def func(a,b,c):
    return a*b*c

a = func(10,20,30)
print(a) # 6000

# 2.关键字参数
'''
关键字参数和函数调用关系紧密, 函数调用使用关键字参数来确定传入的参数值.
使用关键字参数允许函数调用时参数的顺序与声明时不一致, 因为Python解释器能够用参数名匹配参数值
'''
def func2(a,b,c):
    return f"我是{a},今年{b},在读{c}"

b = func2(b = 20,a = '小明',c='大二')
print(b) # 我是小明,今年20,在读大二

# 3.默认参数
'''
默认参数是在调用函数时没有传递参数, 这时就会使用默认参数
'''
def func3(a,b = 18):
    return f"我是{a},今年{b}岁!"

c = func3("李四")
print(c) # 我是李四,今年18岁!

# 4.不定长参数
'''
你可能需要一个函数能处理比当初声明时更多的参数. 这些参数叫做不定长参数, 和上述两种参数不同, 声明时不会命名!
'''
def func4(name,age,*hobby):
    return f"我叫{name},今年{age},我的爱好是: {hobby}" # hobby为不定长参数, 数据以元组的形式呈现

d = func4('张三',23,'唱歌','打游戏','钓鱼')
print(d) # 我叫张三,今年23,我的爱好是: ('唱歌', '打游戏', '钓鱼')

# 5.匿名函数
'''
在Python中匿名函数使用lambda实现
'''
f = lambda a,b: max(a,b) # 返回a和b中较大的值
print(f(21,20)) # 21

# 6.参数传递
'''
在Python中, 类型属于对象, 对象有不同类型的区分, 变量是没有类型的
'''
a = ['a','b','c']
b = 1
'''
在上述代码中, ['a','b','c']是list类型, 1是number类型, 而变量a是没有类型的, 它仅是一个对象的引用, 可以指向
list对象, 也可以指向number对象.
'''

# 7.可更改(mutable)与不可更改(immutable)对象
'''
在Python中, string,tuples,和numbers是不可更改的对象, 而list, dict等则是可以更改的对象.
    1. 不可变类型: 变量赋值a=5后再赋值a=10, 这里实际是新生成一个int值对象10, 再让a指向它, 而5被丢弃,
       不是改变a的值, 相当于新生成了a.
    2. 可变类型: 变量赋值la=[1,2,3,4]后再赋值la[2]=5, 则是将list la的第三个元素值更改, 本身la没有动,
       只是其内部的一部分值被修改了.
'''

# Python传不可变对象实例

def func01(s):
    print("函数内未执行更改前:",id(s))
    s = "world"
    print("函数内执行更改后:",id(s))

s = 'hello'
print("函数外执行",id(s))
func01(s)
'''
函数外执行 2097806132784
函数内未执行更改前: 2097806132784
函数内执行更改后: 2097806134832
'''
print('============================================================')
# Python传可变对象实例
'''
可变对象在函数里修改了参数, 那么在调用这个函数的函数里, 原始的参数也会被改变了
'''
def func2(arr):
    print("函数内未更改前:",id(arr))
    print('函数内未更改前: ', arr)
    arr[2] = 'h'
    print("函数内更改后:",id(arr))
    print('函数内更改后: ', arr)

arr = ['a','b','c']
print('函数外: ',id(arr))
print('函数外: ',arr)
func2(arr)
'''
函数外:  2164922133824
函数外:  ['a', 'b', 'c']
函数内未更改前: 2164922133824
函数内未更改前:  ['a', 'b', 'c']
函数内更改后: 2164922133824
函数内更改后:  ['a', 'b', 'h']
'''
# 传入函数的和在末尾添加新的内容的对象用的是同一个引用.













