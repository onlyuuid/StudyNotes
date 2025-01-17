"""
二. 基本数据类型
"""

# 1.基本数据类型
"""
    python中的变量不需要声明,每个变量使用前都必须赋值, 只有赋值后变量才会被创建.
    在python中变量就是变量, 没有类型, 我们所指的"类型"是变量所指内存中对象的类型.
    等号(=) 用来赋值
    等号(=) 运算符左边是变量名, 右边是存储在变量中的值: 如
"""
a = 10
b = 32.21
c = "hello"
print(a)
print(b)
print(c)

# 2.多个变量赋值
d = e = f = 3
print(d,e,f)
# 上面创建了一个整型对象, 值为3, 从右往左赋值, 三个变量被赋予了相同的值
# 也可以为多个对象指定多个值
g,h,i = 21,43,"hi"
print('g,h,i')
# 上面实例21,43按照位置分别分配给了g,h, hi分配给了i

# 3.标准数据类型
"""
    Python3中常见的数据类型有:
        Number (数字)
        String (字符串)
        bool   (布尔类型)
        List   (列表)
        Tuple  (元组)
        Set    (集合)
        Dictionary  (字典)
    Python3中六个标准数据类型中:
        不可变数据(3个): Number(数字), String(字符串), Tuple(元组)
        可变数据(3个):  List(列表), Dictionary(字典), Set(集合)
"""

# 4. Number(数字)
"""
    Python3支持 int, float, bool, complex(复数)
    在Python3中只有一种整数类型int, 表示为长整型, 没有Python2中的long类型
    像大多数语言一样, 数值类型的赋值和运算都很直观
    内置的type()函数可用用来查询变量所指的对象类型
"""
a = 12
b = "hello"
c = True
print(type(a))
print(type(b))
print(type(c))
"""
<class 'int'>
<class 'str'>
<class 'bool'>
"""
# 此外,还可以使用isinstance(a,int)来判断
d = isinstance(a,int)
print(d) # True
"""
    isinstance()和type()的区别:
        type()不会认为子类是一种父类类型
        isinstance()会认为子类是一种父类类型
"""
class A:
    print("这是一个父类")

class B(A):
    print("这是一个子类")

print(isinstance(A(),A))    # True
print(type(A()) == A)       # True
print(isinstance(B(),A))    # True
print(type(B()) == A)       # False
# 在Python3中bool是int类型的子类, True 和 False可以和数字进行相加, True为1,False为0, 相加为True, 但可以通过is来判断类型
result = issubclass(bool,int)
a = True == 1
b = False == 0
c = True + 3
d = False * 32

print(result) # True
print(a)      # True
print(b)      # True
print(c)      # 4
print(d)      # 0
#  Python2中没有bool类型, 它用数字0表示False, 用数子1表示True
#  当你指定一个值时, Number对象就会被创建
f = 10
print("===============2")
# 你也可以使用del语句删除一些对象的引用
v = 21
j = "43"
l = "hello"
del v
# 删除多个对象
del j,l
# print(v) NameError: name 'v' is not defined
# print(j)
# print(l)

r"""
File "D:\Case Code\4.Python\python_basics\python_basics\day02.py", line 102, in <module>
    print(v)
          ^
NameError: name 'v' is not defined
对象已删除:
"""

# 5.数值运算
a = 5 + 4       # 加法
b = 10 - 3      # 减法
c = 2.4 * 10    # 乘法
d = 2 / 4       # 除法 得到一个浮点数 0.5
e = 2 // 4      # 除法 得到一个整数 0
t = 5 % 2       # 取余
y = 2 ** 3      # 乘方
print(a)
print(b)
print(c)
print(d)
print(e)
print(t)
print(y)
"""
注意:
    (1).Python中可以同时为多个变量赋值: a,b = 1,4
    (2).一个变量可以通过赋值指向不同类型的对象
    (3).数值的除法包含两个运算符: / 返回一个浮点数, // 返回一个整数
    (4).在混合计算时python会把整型转换为浮点数
"""
# 数值类型实例
"""
    int         float           complex
    12           3.14           3.14j
    -1           5.1            9.3e-3j
    080          -21.9          .785j
    -0x260       32e.32         4e-2J
    0x32         -2e + 3        -.3543-3J         -.3543 = -0.3543
"""
# Python还支持复数, 复数由实数部分和虚数部分构成, 可以用a + bj,或者complex(a,b)表示, 复数的实部a和虚部b都是浮点型
jk = 32+2j
ds = complex(54,8)
print(jk) # (32+2j)
print(ds) # (54+8j)
print('-------------22')

# 6. String(字符串)
r"""
    Python中的字符串用单引号(')或者双引号(")括起来, 同时使用反斜杠(\)转义特殊字符.
    字符串截取的语法格式如下:
    变量[头下标:尾下标]
    
    索引值以0为开始值, 以-1为末尾的开始值
   -5 -4 -3 -2 -1   从后面索引
    0  1  2  3  4   从前面索引
    h  e  l  l  o
    
    : 1  2  3  4 :  从前面截取
    :-4 -3 -2 -1 :  从后面截取
"""
s = "hello"
fa = s[1:4]
ds = s[-4:-1]
print(fa)
print(ds)
# 加号 + 是字符串的连接符, 星号 * 表示复制当前字符串, 后面的数字表示要复制的次数
# 实例:
do = "Do"
you = "you"
speak = "speak Chinese"

result = do + you + speak
cp = do * 3
sp = speak[-7:]
print(result)
print(cp)
print(sp)
"""
Doyouspeak Chinese
DoDoDo
Chines
"""

# 在python中使用反斜杠 \ 转义特殊字符, 如果你不想让反斜杠发生转义, 可以在字符串前面使用r, 如:
ds = r"""
    你好\n世界
    """
# 另外, 反斜杠(\)可以作为续航符, 表示下一行是上一行的延续. 也可以使用"""..."""或'''...'''跨越多行.
# 注意: python没有单独的字符类型, 一个字符就是长度为1的字符串类型
fd = 43 + 54 + \
     12 + 54 + \
     32 + 89

word = "python"
print(word[0],word[5])
print(word[-1],word[-6])

# 与C语言字符串不同的是, python字符串不能被改变, 向一个索引位置赋值,如: word[0] = "d", 会导致报错
r"""
注意:
    (1).反斜杠(\)可以用来转义, 使用r可以让反斜杠不发生转义
    (2).字符串可以用+运算符连接在一起, 可以使用*运算符重复
    (3).python中的字符串有两种索引方式, 从左往右从0开始, 从右往左从-1开始
    (4).python中的字符串不能被改变
"""

# 7.bool(布尔类型)
"""
    boolean(布尔类型)即True和False.
    在python中, True和False都是关键字, 表示布尔值
    布尔类型可以用来控制程序的流程, 比如判断某个条件是否成立, 或者在某个条件满足时执行某段代码.
    布尔类型特点:
        (1).布尔类型只有两个值
        (2).布尔类型可以和其他数据类型进行比较, 比如数字, 字符串等. 在比较时,python会将True视为1,False视为0
        (3).布尔值可以和逻辑运算符一起使用, 包括 and,or或not, 这些运算符可以用来组合多个布尔表达式, 生成一个新的布尔值
        (4).布尔类型也可以转换为其他数据类型, 比如整数, 浮点数和字符串. 在转换时,True会被转换为1, False会被转换为0
"""
# 实例:
a = True
b = False
print("--------------------")
# 比较运算符
print(a > 2)
print(b < 2)

# 逻辑运算符
print(a and b)
print(a or b)
print(not a)

# 类型转换
print(int(a))
print(float(a))
print(str(a))
"""
注意:
    在python中,所有非0的数字和非空的字符串, 列表, 元组等数据类型都为True, 只有0, 空字符串, 空列表, 空元组等被视为False
    因此, 在进行布尔类型转换时, 需要注意数据类型的真假性
"""

# 8.List(列表)
"""
    List(列表)是python中使用最频繁的数据类型.
    列表可以完成大多数集合类的数据结构实现. 列表中元素的类型可以不相同, 他支持数字, 字符串甚至包括列表(嵌套).
    列表是写在方括号[]之间, 用逗号分隔开的元素列表.
    和字符串一样, 列表同样可以被索引和截取, 列表被截取后返回一个包含所需元素的新列表 

    列表的截取的语法格式:
    arr[头下标:尾下标]
"""
# 索引值以0开始, 以-1为末尾的开始
arr = ["h","e","l","l","o"]
tmp = arr[1:3]
tmp2 = arr[:4]
tmp3 = arr[3:]
tmp4 = arr[-4:]
print(tmp)
print(tmp2)
print(tmp3)
print(tmp4)
"""
['e', 'l']
['h', 'e', 'l', 'l']
['l', 'o']
['e', 'l', 'l', 'o']
"""

# 加号+是列表连接的运算符, 星号*是重复操作
print(tmp4 + tmp3)  # ['e', 'l', 'l', 'o', 'l', 'o']
print(tmp4 * 3)     # ['e', 'l', 'l', 'o', 'e', 'l', 'l', 'o', 'e', 'l', 'l', 'o']

# 与Python中的字符串不一样的是, 列表中的元素是可以改变的
arr2 = ["y","o","u"]
arr2[-1] = "ur"
print(arr2) # ['y', 'o', 'ur']

list = [43,32,5,-1,4]
list[2:4] = "you"
print(list) # [43, 32, 'y', 'o', 'u', 4]
list[0:2] = []
print(list) # ['y', 'o', 'u', 4]

# List中内置了许多方法, 例如append(), pop()等等.
"""
注意:
    (1).列表写在方括号之间, 元素用逗号隔开
    (2).和字符串一样, 列表可以被索引和切片
    (3).列表可以使用加号+操作符拼接, 使用*重复
    (4).列表中的元素可以被改变
"""
# python列表截取可以接收第三个参数, 参数作用是截取的步长, 以下实例在索引1到索引4的位置上设置步长为2(间隔一个位置)
validate = ['h','e','l','l','o']
"""
                 ↑       ↑
"""
print(validate[1:4:2]) # ['e', 'l']

# 如果第三个参数为负数表示逆向读取, 以下实例用于反转字符串:
def reverseWords(input):
    inputWord = input.split(" ")

    # 翻转字符串
    # 假设列表list = [1,2,3,4]
    # list[0]=1, list[1]=2,  -1表示最后一个元素,list[-1]=list[3]=4
    # inputWord[-1::-1] 有三个参数
    # 第一个参数-1表示最后一个参数
    # 第二个参数为空, 表示移动到列表末尾
    # 第三个参数为步长, -1表示逆向
    inputWord = inputWord[-1::-1]
    output = ' '.join(inputWord)
    return output

if __name__ == '__main__':
    input = "I like runoob"
    rw = reverseWords(input)
    print(rw) # runoob like I

# 9.Tuple(元祖)
"""
    元组(tuple)和列表类似, 不同之处在于元组的的元素不能改变, 元组写在小括号()里, 元素之间使用逗号隔开.
    元组中的类型也可以不相同 
"""
tuple = (1,32," you",True," like","what do")
tinyTuple = ("Does","do")
print(tuple)        # 输出完整元组
print(tuple[0])     # 输出元组中的第一个元素
print(tuple[1:3])   # 输出元组中前两个元素
print(tuple[-1] +  tuple[2] + tuple[-2] ) # 连接元组中的指定元素
print(tuple * 2)    # 输出两次元组
print(tuple + tinyTuple)  # 连接元组
"""
(1, 32, ' you', True, ' like', 'what do')
1
(32, ' you')
what do you like
(1, 32, ' you', True, ' like', 'what do', 1, 32, ' you', True, ' like', 'what do')
(1, 32, ' you', True, ' like', 'what do', 'Does', 'do')
"""
# 元组和字符串类似，可以被索引且下标从0开始，-1为从末尾开始的位置。也可以进行截取
tup = (1,"hi","you",21)
print(tup[0:2])
# tup[0] = "are" 改变元组中的元素是非法的

# 虽然元组中的元素不能改变, 但是它可以包含可变的对象, 如list
# 构造包含0个或1个元素的元组比较特殊, 所以有一些额外的语法规则
tup2 = ()       # 空元组
tup3 = (3,)     # 包含一个元素的元组
print(tup3)    # (3,)
"""
如果你想创建只有一个元素的元组, 需要注意在元素后面添加一个逗号, 以区分它是元组而不是普通的值, 这是因为没有逗号的情况下,  
python会将括号解释为数学运算中的括号, 而不是元组的表示.
以下实例会打印输出普通值3
"""
tup4 = (3)
print(tup4)    # 3

# 这样 tup4 将是整数类型而不是元组类型
# string,list和tuple都属于sequence(序列)
"""
注意:
    (1).与字符串一样, 元组中的数据不能修改
    (2).元组也可以被索引和切片, 方法一样
    (3).注意构造包含0或1个元素的元组的特殊语法规则
    (4).元组也可以使用+操作符进行拼接, 使用*进行重复
"""
k = (32,43,54)
print(k*3)

# 10. Set(集合)
"""
Python中的集合(set)是一种无序, 可变的数据类型, 用于存储唯一的元素.
集合中的元素不会重复, 并且可以进行交集, 并集, 差集等常见的集合操作.
在Python中, 集合使用大括号{}进行表示, 元素之间使用逗号(,)隔开.
另外, 也可以使用set()函数创建集合.

注意:
    创建一个空集合必须使用set()而不是{ }, 因为{ }是用来创建一个空字典

创建格式:
    params = {value1,value2,value3}
    或
    set()
"""
# 实例
sites = {'Google',"百度","IE","火狐","火狐","百度"}
print(sites) # {'IE', '百度', '火狐', 'Google'}  重复的元素会自动过滤

if 'Google' in sites:
    print("在集合中")
else:
    print("不在集合中")

# set可以进行集合运算
a = set('abcdefg')
b = set('djaklhdkal')
print(a)

print(a - b)    # a和b的差集  返回a集合中有但b集合中没有的元素集合
print(a | b)    # a和b的并集  返回a集合加上b集合后去重的元素集合
print(a & b)    # a和b的交集  返回a集合和b集合中共同有的元素集合
print(a ^ b)    #            返回a集合和b集合中不同时出现的元素集合
"""
{'a', 'e', 'c', 'f', 'b', 'g', 'd'}
{'e', 'f', 'c', 'b', 'g'}
{'l', 'k', 'a', 'e', 'f', 'c', 'b', 'j', 'h', 'g', 'd'}
{'a', 'd'}
{'k', 'e', 'f', 'j', 'l', 'c', 'b', 'h', 'g'}
"""

# 11.字典(Dictionary)
"""
    字典(dictionary)是python中另一个非常有用的内置数据类型
    列表是有序的对象集合, 字典是无序的对象集合. 两者之间的区别在于: 字典当中的元素是通过键来存取的, 而不是通过偏移存取.
    字典是一种映射类型, 字典用{ }标识, 它是一个无序的 键(key):值(value)的集合.
    键(key)必须使用不可变类型.
    在同一个字典中, 键(key)必须是唯一的.
"""
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {"name":"runoob","age":13}
print(dict['one'])          # 打印key为one的值
print(dict[2])              # 打印key为2的值
print(tinydict)             # 打印完整字典
print(tinydict.keys())      # 打印字典中所有的key
print(tinydict.values())    # 打印字典中所有的value
"""
1 - 菜鸟教程
2 - 菜鸟工具
{'name': 'runoob', 'age': 13}
dict_keys(['name', 'age'])
dict_values(['runoob', 13])
"""
# dict()函数可以直接从键值对序列中构建字典如下:
# dict([('name','李四'),('age',18),('addr','贵州')])
"""
>>> dict([('name','李四'),('age',18),('addr','贵州')])
{'name': '李四', 'age': 18, 'addr': '贵州'}
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
>>> dict(runoob=1,google=2,taobao=3) 
{'runoob': 1, 'google': 2, 'taobao': 3}
>>>

{x: x**2 for x in (2, 4, 6)}该代码使用的是字典推导式, 更多推导式可以参考: https://www.runoob.com/python3/python-comprehensions.html
另外,字典类型也有一些内置的函数, 例如clear(), keys(), values()等
"""
"""
注意:
    (1).字典是是一种映射类型, 它的元素是键值对.
    (2).字典的关键字必须为不可变类型, 且不能重复
    (3).创建空字典使用{ }
"""

# 12. bytes类型
"""
    在Python3中, bytes类型表示的是不可变的二进制序列(byte sequence).
    与字符串不同的是, bytes类型中的元素是整数值(0~255之间的整数), 而不是Unicode字符.
    bytes类型通常用于处理二进制数据, 比如图像文件, 音频文件, 视频文件等等. 在网络编程中, 也经常使用bytes类型来传输二进制数据.
    创建bytes对象的方式有多种, 最常见的方式是使用b前缀:
    此外, 也可以使用bytes()函数将其他类型的对象转换为bytes类型. bytes()函数的第一个参数是要转换的对象, 第二个参数是编码方式,
如果省略第二个参数, 则默认使用UTF-8编码:  
"""
x = bytes("hello",encoding="utf-8")
print("x = ",x)
"""
    与字符串类型类似, byte类型也支持许多操作和方法, 如切片, 拼接, 查找, 替换等等. 同时, 由于bytes类型是不可变的, 因此
    在进行修改操作时需要创建一个新的bytes对象. 例如:  
"""
print("---------------")
x = b"hello"
print(x)  # 打印完整信息 b'hello'
y = x[1:3]
print(y)  # 切片操作 b'el'
z = x + b"world"
print(z)  # 拼接操作 b'helloworld'
# 需要注意的是, bytes类型中的元素是整数值, 因此在进行比较操作时需要使用相应的整数值, 例如:
x =b'hello'
if x[0] == ord('h'):
    print(ord('h')) # 104
    print('The first element is "h"')
# 其中ord()函数用于将字符串转为相应的整数值

# 13. Python数据类型转换
"""
    有时候, 我们需要对数据内置的类型进行转换, 数据类型的转换, 你只需要将数据类型作为函数名即可
    以下几个内置的函数可以执行数据类型之间的转换. 这些函数返回一个新的对象, 表示转换的值.
    
    int(x[,base])           将对象x转换为一个整数
    float(x)                将对象x转换为一个浮点数
    complex(real[,imag])    创建一个复数
    str(x)                  将对象x转换为字符串
    repr(x)                 将对象x转换为表达式字符串
    eval(str)               用来计算在字符串中的有效Python表达式, 并返回一个对象
    tuple(s)                将序列s转换成一个元组
    list(s)                 将序列s转换为一个列表
    set(s)                  转为可变集合
    dict(d)                 创建一个字典, d必须是一个(key,value)元组序列
    frozenset(s)            转为不可变集合
    chr(x)                  将一个整数转换为一个字符
    ord(x)                  将一个字符转换为它的整数值
    hex(x)                  将一个整数转换为一个十六进制字符串
    oct(x)                  将一个整数转换为一个十八进制字符串
"""