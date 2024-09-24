"""
字符串
    1. Python中的字符串可以用单引号(')和双引号(")表示
    2. Python中不存在字符类型, 一个字符就是单位长度为1的字符串
    3. 访问字符串可以用[]来截取, Python中的字符串可以从左往右索引[0:5]
        也可以从右往左索引[-4:-1], 截取的字符含左不含右
"""
import string

# 字符串更新
var = "hello world"
print("已更新字符,", var[:11] + " runoob")

# 转义字符
"""
    在需要在字符中使用特殊字符时, Python用反斜杠\转义字符. 如下:
    
    转义字符            描述                      实例
    \(在行尾时)         续航符                     
    
    \\                反斜杠符号                  
    
    \'                  单引号                 
    
    \"                  双引号     
    
    \a                  响铃
    
    \b                  退格
    
    \000                空
    
    \n                  换行
    
    \v                  纵向制表符
    
    \t                  横向制表符
    
    \r                  回车, 将\r后面的内容移到
                        字符串开头, 并逐一替换开
                        头部分字符, 直至将\r后面
                        的内容完全替换完成
    
    \f                  换页
    
    \yyy                八进制数, y代表0~7的字
                        符, 例如: \012代表换行
                        
    \\xyy                十六进制数, 以\\x开头,
                        y代表的字符, 例如\x0a
                        代表换行
    \other              其它的字符以普通格式输出       
"""

# 使用\r实现百分比进度

import time

# for i in range(101):
#     print("\r{:3}%".format(i), end="")
#     time.sleep(0.05)

print("结果垃圾的\r发多了发的") # 发多了发的

# 实例
print("\'hello world\'") # 单引号 'hello world'

print("hello world!\t How are you")  # 缩进 hello world!	 How are you

print("hello, \b world")            # 退格  hello, world

print("A 对应的ASCII值为: ",ord("A")) # A 对应的ASCII值为:  65

print("\x41 为 A的ASCII代码")  # A 为 A的ASCII代码

decimal_number = 42
binary_number = bin(decimal_number) # 十进制转换为二进制
print(binary_number) # 0b101010

octal_number = oct(decimal_number)  # 十进制转换为十八进制
print(octal_number)  # 0o52

hexadecimal_number = hex(decimal_number)    # 十进制转换为十六进制
print(hexadecimal_number)   # 0x2a

# Python 字符串运算符
"""
    下表实体变量a值为字符串"Hello", 变量b值为"Python"
    
    操作符             描述                  实例
    +               字符串连接               a + b 返回HelloPython
    
    *               重复输出字符串            a*2输出结果为HelloHello
    
    []              通过索引获取字符串中       a[2]返回l
                    的字符 
                    
    [:]             截取字符串中的一部分,      a[1:4]返回ell     
                    遵从左闭右开原则, 
                    str[0:2]是不包含第三个
                    字符的
    
    in              成员运算符-如果字符串中    h = "hello"
                    包含指定的字符返回True    bool = 'e' in h
                                           print(bool) True
                                    
    in not          成员运算符-如果字符串中   h = "hello"
                    不包含指定的字符返回True  bool = 'a' in h
                                          print(bool)
                                          
    r/R             原始字符串-原始字符串: 所有的字符串都是直接按照字面意思来使用
                    , 没有转义特殊或不能打印的字符. 原始字符串除在字符串的第一个
                    引号前加上字母r(可以大小写)以外, 与普通字符串有着几乎完全相同
                    的语法
    
    %               格式字符串
"""
h = "hello"
bool = 'a' in h
print(bool)

# 字符串格式化
"""
Python支持格式化字符串的输出. 尽管这样可能会用到非常复杂的表达式, 但最基本的用法是
将一个值插入到一个有字符串格式的符%s的字符串中.
"""
print("我叫%s, 今年%d岁!"% ('小明',10))

# Python字符串格式化符号:
"""
    符号                      描述
    %c                       格式化字符串及其ASCII码
    
    %s                       格式化字符串
    
    %d                       格式化整数
    
    %u                       格式化无符号整型
    
    %o                       格式化无符号八进制数
    
    %x                       格式化无符号十六进制数
    
    %X                       格式化无符号十六进制数(大写)
    
    %f                       格式化浮点数字, 可指定小数点后的精度
    
    %e                       用科学计数法格式化浮点数
    
    %E                       作用同%e, 用科学计数法格式化浮点数
    
    %g                       %f和%e的简写
    
    %G                       %f 和 %E 的简写
    
    %p                       用十六进制数格式化变量的地址
"""

# 格式化操作符辅助指令:
"""
    符号                      功能
    *                        定义宽度或者小数点精度
    
    -                        用做左对齐
    
    +                        在正数前面显示加号 +
    
    <sp>                     在正数前面显示空格
    
    #                       在八进制数前面显示('0),在十六进制前面显示
                            '0x'或者'0X'
                
    0                       显示的数字前面填充'0'而不是默认的空格
    
    %                       '%%'输出一个单一的'%'
    
    (var)                   映射变量(字典参数)
    
    m.n.                    m是显示的最小总宽度, n是小数点后的位数(如果可以的话)
"""

# Python2.6开始, 新增了一种格式化字符串的函数str.format(), 它增强了字符串格式化的功能.

# 三引号
"""
    Python三引号允许一个字符串跨多行, 字符串中可以包含换行符, 制表符以及其他特殊符号
"""
str = ("""hello world
ta\tb 
runoob\n
1111""")
print(str)
"""
hello world
ta	b 
runoob

1111
"""
# 一个典型的案例是, 当你需要一块html或sql时, 这时使用字符串组合, 特殊字符串转义将会非常繁琐.
html = """
<html>
<head></head>
<body>
    <h1>hello world</h1>
</body>
</html>
"""

sql = """
    select * 
    from user 
"""
print(sql)

# f-string
"""
    f-string是Python3.6之后版本添加的, 称之为字面量格式化字符串, 是新的格式化字符串的语法
    之前使用百分号 %
"""
name = 'runoob'
res = "hello %s"%(name)
print(res) # hello runoob

res2 = f"hello {name}"
print(res2) # hello runoob

g = f"{1 + 2}"
print(g)

arr = {"name": "runoob", "url": "www.runoob.com"}
tmp = f"{arr['name']}: {arr['url']}"
print(tmp) # runoob: www.runoob.com

# python3中, 所有的字符串都是Unicode字符串

# 字符串内建函数
"""
方法                          描述
capitalize()                 将字符串的首字母大写

center(width,fillchar)       返回一个指定的宽度width居中的字符串, fillchar为填充的字符串, 默认为空格

count(str,beg=0,end=len(string))
                             返回str在string里面出现的次数, 如果beg或者end指定则返回指定范围内str出现的次数

bytes.decode(encoding="utf-8", errors="strict")
                             Python3中没有decode方法, 但我们可以使用bytes对象的decode()方法来解码给定的bytes
                             对象, 这个bytes对象可以由str.encode()来编码返回.

encode(encoding="utf-8", errors="strict")
                             以encoding指定的编码格式编码字符串
                            
endsWith(suffix,bug=0,end=len(string)) 
                            检查字符串是否以suffix结束, 如果beg或者end指定则检查指定的范围是否以suffix结束,
                            如果是, 返回True,否则返回False.

expandtabs(tabsize=4)       把字符串string中的tab符号转为空格, tab符号默认的空格数是4

find(str,beg=0,end=len(string))
                            检测str是否包含在字符串中, 如果指定范围beg和end, 则检查是否包含在指定范围内, 
                            如果包含返回开始的索引值, 否则返回-1
                        
index(str,beg=0,end=len(string))
                            跟find()方法一样, 只不过如果str不在字符串中会报一个异常.
                        
isalnum()                   检查字符串是否由字母和数字组成, 即字符串中的所有字符都是字母或数字. 如果字符串至少有
                            一个字符, 并且所有字符都是字母或数字, 则返回True, 否则返回False
    
isalpha()                   如果字符串至少有一个字符并且所有字符都是字母或中文字则返回True, 否则返回False

isdigit()                   如果字符串只包含数字则返回True否则返回False

islower()                   如果字符串中包含至少一个区分大小写的字符, 并且所有这些(区分大小写的)字符都是小写,
                            则返回True, 否则返回False
                        
isnumeric()                 如果字符串中只包含数字字符, 则返回True, 否则返回False

isspace()                   如果字符串中只包含空白, 则返回True, 否则返回False

istitle()                   如果字符串时标题化的(见title())则返回True, 否则返回False

isupper()                   如果字符串中包含至少一个区分大小写的字符, 并且所有这些(区分大小写的)字符都是大写, 则
                            返回True, 否则返回False
                        
join(seq)                   以指定字符串作为分隔符, 将seq中所有的元素(的字符串表示)合并为一个新的字符串

len(string)                 返回字符串长度

ljust(width[,fillchar])     返回一个原字符串左对齐, 并且使用fillchar填充至长度width的新字符串, fillchar默认为
                            空格.
                            
lower()                     转换字符串中所有大写字符为小写

lstrip()                    截掉字符串左边的空格或指定字符

maketrans()                 创建字符映射的转换表, 对于接受两个参数的最简单的调用方式, 第一个参数是字符串, 表示
                            需要转换的字符, 第二个参数也是字符串表示转换的目标
                            
max(str)                    返回字符串str中最大的字母

min(str)                    返回字符串str中最小的字母

replace(old,new[,new])      将字符串中的old替换成new, 如果max指定, 则替换不超过max次

rfind(str,beg=0,end=len(string))
                            类似于find()函数, 不过是从右边开始查找
      
rindex(str,beg=0,end=len(string))
                            类似于index(), 不过是从右边开始

rjust(width,[,fillchar])    返回一个原字符串右对齐, 并使用fillchar(默认空格)填充至长度width的新字符串

rstrip()                    删除字符串末尾的空格或指定字符

split(str="",num=string.count(str))                                           
                            以str为分隔符截取字符串, 如果num有指定值, 则仅截取num+1个子字符串
           
splitlines([keepends])      按照行('\r','\r\n','\n')分隔, 返回一个包含各行作为元素的列表, 如果参数keepends
                            为False, 不包含换行符, 如果为True, 则保留换行符.                 
        
startswith(substr, beg=0,end=len(string))
                            检查字符串是否是以指定子字符串substr开头, 是则返回True, 否则返回False. 如果beg
                            和end指定值, 则在指定范围内检查
                            
strip([chars])              在字符串上执行lstrip()和rstrip()

swapcase()                  将字符串中大写转换为小写, 小写转换为大写

title()                     返回"标题化"的字符串, 就是说所有单词都是以大写开始, 其余字母均为小写(见istitle())

translate(table,deletechars="")
                            根据table给出的表(包含256个字符)转换string的字符串, 要过滤掉的字符串放到deletechars
                            参数中

upper()                     转换字符串中的小写字母为大写

zfill(width)                返回长度为width的字符串, 原字符串右对齐, 前面填充0

isdecimal()                 检查字符串是否只包含十进制字符, 如果是返回True, 否则返回False
"""
s = "10111"
table = str.maketrans("", "", "he")
print(s.isdecimal())

