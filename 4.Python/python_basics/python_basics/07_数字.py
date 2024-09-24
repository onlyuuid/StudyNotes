"""
数字(number)
    Python数字数据类型用于存储数值
    数据类型是不允许改变的, 这意味着如果改变数据类型的值, 将重新分配内存空间.
"""
import math
import random

# 以下实例在变量赋值时, number对象将被创建
a = 1
b = 10

# 可以使用del语句删除一些数字对象的引用
# 语法: del val1[, val2[,val3[...valN]]]
del a

# Python支持三种不同的数值类型:
"""
    整型(int)
    通常被称为整型或整数, 是正或负整数, 不带小数点. Python3整型是没
    有限制大小的, 可以当作long类型使用, 所以Python3没有Python2的long类型.
    布尔(bool)是整型的子类型.
    
    浮点型(float)
    浮点型由整数部分与小数部分组成, 浮点型也可以使用科学计数法表示
    (2.5e = 2.5 * 10^2 = 250)
    
    复数(complex)
    复数由实数部分虚数部分构成, 可以用a + bj, 或者complex(a,b)表示, 
    复数的实部a和虚部b都是浮点型
"""

# 数字类型转换
"""
有时候, 我们需要对数据内置的类型进行转换, 数据类型的转换, 只需要将数据类型作为
函数名即可
int(x)          将x转换为整数
float(x)        将x转换为浮点数
complex(x)      将x转换到一个复数, 实部为x, 虚部为0
complex(x,y)    将x和y转换到一个复数, 实数部分为x, 虚数部分为y. x和y是数字表达式
"""

# 算数运算
"""
Python解释器可以作为一个简单的计算器, 您可以在解释器里数一个表达式, 它将输出表达式的值
表达式的语法很直白: + - * 和 /, 和其他语言一样, 如:
"""
a = 2 + 4

g = 5 - 3

h = 6 * 4

j = 8 / 2

l = 9 // 2

print(a)
print(g)
print(h)
print(j)
print(l)
"""
6
2
24
4.0
4
"""
"""
注意:
    在不同的机器上浮点运算的结果可能不太一样.
    在整数除法中, 除法 / 总是返回一个浮点数, 如果只想得到整数的结果, 
    丢弃可能的分数部分,可以使用运算符//
"""
t = 5 // 2 # 2
print(t)

"""
注意:
    // 得到的不一定是整数类型的数, 它与分母分子的数据类型有关系.
"""
s = 6.0 // 2
print(s) # 3.0

u = 8 // 3.0
print(u) # 2.0

# Python可以使用**操作来进行幂运算:
o = 5 ** 2  # 25

# 变量在使用前必须先'定义'(即赋予变量一个值), 否则会出错:
# r
"""
Traceback (most recent call last):
  File "D:\Case Code\4.Python\python_basics\python_basics\数字_07.py", line 90, in <module>
    r
NameError: name 'r' is not defined
"""

# 不同类型的数进行混合运算时, 会将整数转换为浮点数:
n = 5 * 3.2 / 3.1
print(n) # 5.161290322580645

# 在交互模式中, 最后被输出的表达式结果被赋值给了变量_, 如:
"""
>>> a = 12.5 / 20
>>> b = 100.60
>>> a * b
62.875
>>> b + _
163.475
>>> round(_,2) 
163.47
>>>
"""

# 数学函数
"""
    abs(x)          返回数字的绝对值, 如abs(-10)返回10
    ceil(x)         返回数字向上取整, 如math.ceil(4.1)返回5
    exp(x)          返回e的x次幂(e^x), 如math.exp(1)返回2.718281828459045
    fabs(x)         以浮点数形式返回数字的绝对值, 如math.fabs(-10)返回10.0
    floor(x)        返回数字向下取整, 如math.floor(3.8)返回3
    log(x)          如math.log(math.e)返回1.0, math.log(100,10)返回2.0
    log10(x)        返回以10为基数的x对数, 如math.log10(100)返回2.0
    max(x1,x2)      返回给定参数的最大值, 参数可为序列
    min(x1,x2)      返回给定参数的最小值, 参数可为序列
    mod(x)          返回x的整数部分和小数部分, 两部分的数值符号与x相同, 整数部分以浮点型表示
    pow(x,y)        返回x ** y运算后的值
    round(x[,n])    返回浮点数x四舍五入值, 如给出n值, 则代表舍入到小数点后的位数.
    sqrt(x)         返回数字x的平方根
"""

# 随机数函数
"""
随机数函数可用于数学, 游戏, 安全等领域中, 还经常被嵌入到算法中, 以提高算法的效率, 
并提高程序的安全性.
Python包含以下常用随机函数:
    choice(seq)     从序列的元素中随机挑选一个元素, 比如random.choice(range(10)), 
                    从0到9中随机挑选一个整数.
    
    randrange([start,] 从指定范围内, 按指定基数递增的集合中获取一个随机数, 
    stop[,step])       基数默认值为1
    
    random()        随机生成一个实数, 它的范围在[0,1)范围内
    
    seed([x])       改变随机数生成器的种子seed. 如果你不理解其原理, 
                    你不必特别去设定seed, Python会帮你选择seed
    
    shuffle(lst)    将序列的所有元素随机排序
    
    uniform(x,y)    随机生成下一个实数, 它的范围在[x,y]以内                  
"""
a = random.choice(range(20))
t = random.randrange(10)
h = random.random()
jk = [1,32,5,6,7,54]
random.shuffle(jk)
le = random.uniform(19,20)
print("-----------------")
print(a)
print(t)
print(h)
print(jk)
print(le)

# 三角函数
"""
Python包含以下三角函数
    acos(x)         返回x的反余弦弧度值
    asin(x)         返回x的反正弦弧度值
    atan(x)         返回x的反正切弧度值
    atan2(y,x)      返回给定的x及y坐标值的反正切值
    cos(x)          返回x的弧度的余弦值
    hypot(x,y)      返回欧几里德范数sqrt(x*x + y*y), 获取直角三角形斜边的长
    sin(x)          返回x的弧度的正弦值
    tan(x)          返回x的弧度的正切值
    degree(x)       将弧度转换为角度, 如degree(math.pi/2), 返回90.0
    radians(x)      将角度转换为弧度
"""

















