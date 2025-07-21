"""
标准库
    python3的标准库非常庞大,所提供的组件涉及十分广泛,使用标准库可以让我们轻松的完成各种任务
一下是一些python3标准库中的模块:
os模块: os模块提供了许多与操作系统交换的函数, 例如创建, 移动和删除文件目录, 以及访问环境变量等.

sys模块: sys模块提供了与python解释器和系统相关的功能, 例如解释器的版本和路径, 以及与stdin, stdout和stderr
        相关的信息.

time模块: time模块提供了处理时间的函数, 例如获取当前时间, 格式化日期和时间, 计时等.

datetime模块: datetime模块提供了更高级的日期和时间处理函数, 例如处理时区, 计算时间差, 计算日期差等.

random模块: random模块提供了生成随机数的函数, 例如生成随机整数, 浮点数, 序列等.

math模块: math模块提供了数学函数, 例如三角函数, 对角函数, 指数函数, 常数等.

re模块: re模块提供了正则表达式处理函数, 可以用于文本搜索, 替换, 分隔等.

json模块: json模块提供了JSON编码和解码函数, 可以将python对象转换为JSON格式, 并从JSON格式中解析出python对象.

urllib模块: urllib模块提供了访问网页和处理URL的功能, 包括下载文件, 发送POST请求, 处理cookies等
"""
# 1.操作系统接口
"""
os 模块提供了不少与操作系统相关联的函数, 例如文件和目录的操作.
"""
import os
# 获取当前工作目录
current_dir = os.getcwd()
print("当前工作目录为: ",current_dir)

# 列出目录下的文件:
files = os.listdir(current_dir)
print("工作目录下的文件: ")
for f in files:
    print(f)

"""
建议使用 import os 风格而非 from os import *, 这样可以保证随操作系统不同而有所变化的os.open()不会覆盖内置函数open(). 
在使用os这样的大型模块时, 内置的dir()和help()函数非常有用:
>>> import os
>>> dir(os) 
['DirEntry', 'EX_OK', 'F_OK', 'GenericAlias', 'Mapping', ...]
>>> help(os) 
Help on module os:                                                                                                                   

NAME
    os - OS routines for NT or Posix depending on what system we're on.

MODULE REFERENCE
    https://docs.python.org/3.12/library/os.html
...
"""
"""
针对日常的文件和目录管理任务, :mod:shutil模块提供了一个易于使用的高级接口:
"""
# import shutil
# shutil.copyfile("text/a.txt","text/a/b.txt") # 复制文件
# shutil.move("text/a.txt","text/b") # 移动文件

# 2. 文件通配符
"""
glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:
"""
import glob
print(glob.glob("text/*.txt"))

# 3.命令行参数
"""
通用工具脚本经常调用命令行参数. 这些命令行参数以链表形式存储于sys模块的argv变量. 如:
"""
import sys
print(sys.argv)
"""
['D:\\StudyNotes\\4.Python\\python_basics\\python_basics\\28_标准库概览.py']
"""

# 4. 错误输出重定向和终止程序
"""
sys还有stdin, stdout和stderr属性, 即使在sdtout被从定向时, 后者也可以用于显示警告和错误信息.
"""
# sys.stderr.write("waring, log file not found starting a new one\n")
"""
waring, log file not found starting a new one
"""

# 5. 字符串正则匹配
"""
re模块为高级字符串处理提供了正则表达式工具. 对于复杂的匹配和处理, 正则表达式提供了简介, 优化的解决方案.
"""
import re
s = re.findall(r"\bf[a-z]*","which foot or hand fell fastest")
print(s)
"""
['foot', 'fell', 'fastest']
说明:
r"" 表示原始字符串, 避免转义字符被解释
\b  表示单词边界, 确保匹配的是以f开头的完整单词
f   匹配字母f
[a-z]* 匹配f后面的任意数量的小写字母(*表示0次或多次)

字符串 which foot or hand fell fastest 是被搜索的字符串
"""
# 6.数学
"""
math模块为浮点运算提供了对底层C函数库的访问:
"""
import math
print(math.cos(math.pi / 4))
print(math.log(1024, 2)) # 获取以2为底1024的对数

#random提供了随机数生成功能:
import random
result = random.choice(['apple', 'pear', 'banana'])
print("A random choice: ",result) # 随机选择一个元素

result2 = random.sample(range(100), 10) # 从0到99的列表中随机选择10个元素
print("10 random numbers: ",result2)

random3 = random.random()
print("A random float: ",random3) # 随机生成一个0到1的浮点数

# 7.访问互联网
"""
有几个模块用于访问互联网以及处理网络通信协议. 其中最简单的两个是用于处理从utls接收的数据的utllib.request和utllib.request
以及用于发送电子邮件smtplib:
"""
# from urllib.request import urlopen
# response = urlopen("https://gitee.com")
# # 读取响应内容
# html = response.read()
# print(html.decode('utf-8'))

# 8.日期和时间
"""
datetime模块为日期和时间处理同时提供了简单和复杂的方法.
支持日期和时间算法的同时, 实现的重点放在更有效的处理和格式化输出.
"""
import datetime
# 获取当前日期和时间
current_datetime = datetime.datetime.now()
print(current_datetime)

# 获取当前日期
current_date = datetime.date.today()
print(current_date)

# 获取当前时间
current_time = datetime.datetime.now().time()
print(current_time)
# 该模块还支持时区处理:
from datetime import date
now = date.today()

now2 = datetime.date(2003, 12, 25) # 创建一个日期对象

result3 = now2.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(result3)

# 9.数据压缩
"""
以下模块直接支持通用的数据打包和压缩格式: zlib, gzib, bz2, zipfile, 以及tarfile
"""
import zlib
s = b'witch which has which witches wrist watch'
len2 = len(s)
print(len2)
t = zlib.compress(s)
print(len(t))
result4 = zlib.decompress(t)
print(result4)

n = zlib.crc32(s)
n2 = zlib.crc32(result4)
print(n == n2)

# 10.性能度量
"""
有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。
例如，使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多,timeit 证明了现代的方法更快一些。
"""
from timeit import Timer
t = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
t2 = Timer('a,b = b,a', 'a=1; b=2').timeit()
print(t, t2)

# 11.测试模块
"""
开发高质量软件的方法之一是为每一个函数开发测试代码，并且在开发过程中经常进行测试
doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。
通过用户提供的例子，它强化了文档，允许 doctest 模块确认代码的结果是否与文档一致:
"""
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # 自动验证嵌入测试

"""
unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集:
"""
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main() # Calling from the command line invokes all tests

