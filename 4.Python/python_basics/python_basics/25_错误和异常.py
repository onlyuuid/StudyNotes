"""
错误和异常
作为Python初学者, 在刚学习Python编程时, 经常会看到一些报错信息,
Python有两种错误很容易辨认: 语法错误和异常.
Python assert(断言) 用于判断一个表达式, 在表达式条件为false的时候触发异常.
"""
import sys

# 1.错误语法
"""
Python的语法错误或者称之为解析错, 是初学时经常碰到的, 如:
>>> while True print("hello world")
  File "<stdin>", line 1
    while True print("hello world")
               ^^^^^
SyntaxError: invalid syntax
这个例子中, 函数print()被检查到有错误, 是因为它前面缺少了一个冒号: 。
语法分析器指出了出错的一行, 并且在最先找到的错误的位置标记了箭头
"""
# 2.异常
"""
即便python程序的语法是正确的, 在运行它的时候, 也有可能发生错误. 运行期检测到的错误被称为异常.
大多数的异常都不会被程序处理, 都以错误信息的形式展现在这里:
>>> 10 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + a + 3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
异常以不同的类型出现, 这些类型都作为信息的一部分打印出来: 例子中的类型有 ZeroDivisionError，NameError 和 TypeError。
错误信息的前面部分显示了异常发生的上下文, 并以调用栈的形式显示具体信息.
"""
# 3.异常处理
"""
异常捕捉可以使用try/except语句
try
    执行代码
except:
    发生异常时执行的代码
以下例子中, 让用户输入一个合法的整数, 但是允许用户中断这个程序(使用ctrl+c或操作系统提供的方法). 用户中断的信息
会引发一个keyboardInterrupt异常
>>> while True:
...     try:
...         x = int(input("请输入一个数字:"))
...         break
...     except ValueError:
...         print("您输入的不是数字")
...  使用ctrl + c退出       
KeyboardInterrupt 

try语句按照如下方式工作:
 首先, 执行try子句(在关键字try和关键字except之间的语句)
 如果没有异常发生, 忽略except子句, try子句执行后结束.
 如果在执行try子句的过程中发生了异常,那么try子句余下的部分将会被忽略. 如果异常的类型和except之后的名称相符, 那么对应的except子句将被执行
 如果一个异常没有与任何的except匹配, 那么这个异常将会传递给上层的try中.
 
一个try语句可能包含对个except子句, 分别来处理不同的特定的异常. 最多只有一个分支会被执行.
处理程序将只针对对应的try子句中的异常进行处理, 而不是其他的try的处理程序中的异常.
异常except子句可以同时处理多个异常, 这些异常将被放在一个括号()里成为一个元组, 例如:
"""
# try:
#     10/0
# except(RuntimeError,TypeError,ZeroDivisionError):
#     print(ZeroDivisionError)
"""
最后一个except子句可以忽略异常的名称, 它将被当作通配符使用. 你可以使用这种方法打印一个错误信息, 然后再次把它抛出
"""
# try:
#     # a = "d" + 3
#     f = open('test2.txt')
# except FileNotFoundError:
#     print(FileNotFoundError)
# except TypeError:
#     print(TypeError) # 打印异常
# except:
#     print(sys.exc_info()[0])
#     raise  # 抛出异常
# try/except...else
"""
try/except语句还有一个可选的else子句, 如果使用这个子句, 那么必须放在所有的except子句之后
else子句将在try子句没有发生任何异常的时候执行.
try:
    执行代码
except:
    发生异常时执行的代码
else:
    没有异常时执行的代码

以下实例在try语句中判断文件是否可以打开, 如果打开文件时正常的没有发生异常则执行esle部分语句, 读取文件内容:
"""
for arg in sys.argv[1:]:
    try:
        f = open(arg,'r')
    except IOError:
        print('Cannot open', arg)
    else:
        print(arg,'has',len(f.readlines()),'lines')
        f.close()
"""
使用else语句比把所有的语句都放在try子句里面要好, 这样可以避免一些意想不到的错误, 而except有无法捕获异常.
异常处理不仅仅处理那些直接发生在try子句中的异常, 而且还能处理子句中调用的函数(甚至间接调用的函数)里抛出的异常. 例如:
"""
def this_fails():
    x=1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print("ZeroDivisionError", err)

# try-finally语句
"""
try-finally语句无论是否发生异常都将执行最后的代码.
try:
    执行语句
except:
    发生异常时执行的代码
else:
    没有异常时执行的代码
finally:
    不管有没有异常都会执行的代码

以下实例中finally语句无论异常是否发生都会执行:
"""
# def des():
#     "10" + 10
#     print("hello world")
# try:
#     des()
# except TypeError as err:
#     print("TypeError", err)
# else:
#     print("OK")
# finally:
#     print("closed")

# 4.抛出异常
"""
python使用raise语句抛出一个指定的异常.
"""
# a = 10
# if a > 5:
#     raise Exception("a 不能大于5, x 的值为: {}".format(a))
"""
raise唯一的一个参数指定了要抛出的异常. 它必须是一个异常的实例或者是异常的类(也就是Exception的子类).
如果你只想知道这是否抛出了一个异常, 并不想去处理它, 那么一个简单的raise语句就可以再次把它抛出
"""
# try:
#     raise NameError("NameError") # 模拟异常
# except NameError:
#     print("NameError")
#     raise # 再次抛出
# 5.用户自定义异常
"""
你可以通过创建一个新的异常类来拥有自己的异常. 异常类继承自Exception类, 可以直接继承或间接继承, 例如:
"""
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
try:
    raise MyError(2*2)
except MyError as err:
    print("My exception occurred, value",err.value)

# My exception occurred, value 4
"""
Traceback (most recent call last):
  File "D:\StudyNotes\4.Python\python_basics\python_basics\25_错误和异常.py", line 173, in <module>
    raise MyError("oops!")
MyError: 'oops!'
"""
"""
在这个例子中, 类Exception默认的__init__()被覆盖.
当创建一个模块有可能抛出多种不同的异常时, 一种通常的做法是为这个包建立一个基础异常类,然后基于这个基础类为不同的错误情况
创建不同的子类:
"""
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in input.

    Attributes:
        expression -- input expression in which the error occurred.
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

"""
大多数的异常的名字都以"Error"结尾, 就跟标准的异常命名一样
"""
# 6.定义清理行为
"""
try语句还有另外一个可选的子句, 它定义了无论在任何情况下都会执行清理行为. 例如
"""
# try:
#     raise KeyboardInterrupt
# finally:
#     print("Goodbye world!")
"""
Goodbye world!
Traceback (most recent call last):
  File "D:\StudyNotes\4.Python\python_basics\python_basics\25_错误和异常.py", line 225, in <module>
    raise KeyboardInterrupt
KeyboardInterrupt
"""
"""
以上例子不管try子句里面有没有发生异常, finally子句都会执行.
如果一个异常在try子句里(或者在except和else子句里)被抛出, 而有没有任何的except把它截住, 那么这个异常会在finally子句
执行后被抛出
下面是一个更复杂的例子(在同一个try语句里包含except和finally子句)"
"""
# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("divide by zero")
#     else:
#         print("result is",result)
#     finally:
#         print("executing finally clause")
# divide(2,1)
# 2.0
# divide(2,0)
"""
executing finally clause
divide by zero
"""
# divide("2","1")
"""
executing finally clause
"""
# 7.预定义的清理行为
"""
一些对象定义了标准的清理行为, 无论系统是否成功的使用了它, 一旦不需要它了, 那么这个标准的清理就会执行
下面这个例子展示了尝试打开一个文件, 然后把内容打印到屏幕上:
"""
# for line in open("text/myfile.txt",encoding='utf-8'):
#     print(line,end="")
"""
以上这段代码的问题是, 当执行完毕后, 文件会保持打开状态, 并没有被关闭.
关键词with语句就可以保证诸如文件之类的对象在使用完成之后一定会正确的执行他的
清理方法:
"""
with open("text/myfile.txt",encoding='utf-8') as f:
    for line in f:
        print(line,end="")
"""
以上这段代码执行完毕后, 就算在处理过程中出问题了, 文件f总是会关闭
"""