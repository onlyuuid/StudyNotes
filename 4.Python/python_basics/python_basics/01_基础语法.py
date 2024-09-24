"""
一. 基本语法
"""
# 1.单行注释

# 2.打印语句
print("Hello World")

# 3.多行注释
'''
多行注释
'''
"""
多行注释
"""

# 4.行与缩进
#   缩进是python中的一大特点, 可以使用缩进来表示代码块, 不需要大括号{}来表示, 缩进的空格数是可以改变的, 但是同一代码块必须包含相同的缩进空格数.
b = True
if b:
    print("True")
else:
    print("False")
# print("end") 缩进不一样会导致报错

# 5.多行语句
#   python中通常都是一行写完一条语句, 但是如果语句太长,可以使用反斜杠\来实现多行语句, 例如:
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
print(total)
#   在[],{},()中不要使用 \, 如:
arr = ['1','2'
      ,'3','4'
      ,'5','6']

# 6.数字类型
#   python3中数字有3种类型: 整数, 浮点数, 复数
"""
    整数: -2,3,4
    浮点数: 32.1, 11.32
    复数: 2j, 2 + 3j
"""

# 7.boolean类型
bool = True
# boolean 类型只有两个值, True 和 False

# 8.字符串
#   (1).python3中单引号(')和双引号(")完全相同
a = "hello"
b = 'hello'
print(a == b) # True

#   (2).使用三引号('''和""")可以指定一个多行字符串
s = """
        what's 
        you 
        name?
    """
#   (3).转义字符 \ \n为换行
a = "你好\n!"
print(a)

#   (4).反斜杠可以用来转义, 使用r可以让反斜杠不发生转义
d = r"hello world\n!"
print(d) # hello world\n!

#   (5).按字面意义级联字符串, 如: "this" "is" "a" "cat" 会被自动转换为 "thisisacat"
f = "this" "is" "a" "cat"
print(f)

#   (6).字符串可以用 +运算符连接在一起, 用 * 运算符重复
g = "hello" + "world"
h = "hello" * 2
print(g)
print(h)

#   (7).python中的字符串有两种索引方式, 从左往右从0开始, 从右往左从-1开始, s[index,last] index未开始索引,last为结束索引
j = "python is best language at world!"
k = j[0:23]     # 含左不含右
l = j[-9:-1]    # 含左不含右
print(k)
print(l)

#   (8).python中的字符串不能改变
z = "hello!"
# v = z[0]= "3"
# print(v) # 报错

#   (9).python没有单独的字符类型, 一个字符就是长度为1的字符串

#   (10).字符串的字符串切片可以加上步长, s[start,last,step] step为步长
x = "Does your sister likes to watch TV?"
c = x[0:10:2]  # De or
print(c)

# 9.空行
#   空行不是python语法的一部分, 在编写代码是不插入空行也不会引起报错, 但是空行用于分隔两段不同功能或意义的代码, 可以使代码便于维护和管理

# 10. 等待用户输入
# inp = input("按下回车键退出!\n")
# print(inp)

# 11.同一行显示多条语句
import sys; v = "runoob"; sys.stdout.write(v + "\n")
"""
使用交互模式执行:
>>> import sys; a = "runoob"; sys.stdout.write(a + "\n") 
runoob
7
>>>
runoob为6个字符, \n为一个字符,共7个字符
"""

# 12.多个语句构成代码组
"""
    缩进相同的一组语句构成一个代码块, 我们称之为代码组,将首行及后面代码组称为一个子句(clause)
"""
n = 4

if n % 2 == 0:
    print("n 是一个偶数")
else:
    print("n 是一个奇数")

# 13.print输出
#   print输出默认是换行的, 如果想要不换行,需要在变量末尾加上 end=""
m = "你好"
nm = "世界"

# 换行输出
print(m)
print(nm)

# 不换行输出
print(m, end="")
print(nm, end="")

# 14.import与from...import
"""
    (1).在Python中用import或者from...import来导入相应模块
    (2).将整个模块(somemodule)导入, 格式为: import somemodule
    (3).从某个模块中导入某个函数的格式为: from somemodule import somefunction
    (4).从某个模块中导入多个函数的格式为: from somemodule import somefunction1, somefunction2, somefunction3
    (5).从某个模块中导入所有函数的格式为: from somemodule import * 
"""
import sys
print("=================================================")
print("命令行参数为:")
for i in sys.argv:
    print(i)
print("\nPython路径为:",sys.path)
# 导入sys的argv,path
from sys import argv, path
print("======================================")
print("path",path)
print("argv",argv)















