"""
命名空间和作用于
"""
# 1.命名空间
"""
命名空间（namespace）是从名称到对象的映射，大部分的命名空间都是通过Python字典来实现的。
命名空间提供了在项目中避免名字冲突的一种方法。各个命名空间是独立的，没有任何关系的，所以一个命名空间中不能有重名，
但不同的命名空间是可以重名而没有任何影响的。
例如，一个文件目录中可以包含多个文件夹，每个文件夹中不能有相同的文件名，但不同文件夹中的文件可以重名。
一般有三种命名空间:
 内置名称(built-in names): python语言内置的名称, 比如函数名abs,char和异常名称BaseException, Exception等待.
 全局名称(global names): 模块中定义的名称, 记录了模块的变量, 包含函数, 类, 其它导入的模块, 模块级的变量和常量.
 局部名称(local names): 函数中定义的名称, 记录了函数的变量, 包括函数的参数和局部定义的变量.(类中定义的也是)
"""
"""
命名空间查找顺序:
假设我们要使用变量runoob, 则python的查找顺序为: 局部的命名空间 -> 全局命名空间 -> 内置命名空间
如果找不到变量runoob, 它将放弃查找并引发一个NameError异常:
NameError: name 'a' is not defined
"""
"""
命名空间的生命周期:
命名空间的生命周期取决于对象的作用域, 如果对象执行完成, 则该命名空间的生命周期就结束.
因此, 我们无法从外部命名空间访问内部命名空间的对象.
"""
# var1 是全局名称
var1 = 5
def some_func():
    # var2 是局部名称
    var2 = 6
    def some_inner_func():
        # var3 是内嵌的局部名称
        var3 = 7
"""
相同的对象名称可以存在于多个命名空间中.
"""

#2.作用域
"""
作用域就是python程序可以直接访问命名空间的正文区域.
在一个python程序中, 直接访问一个变量, 会从内到外依次访问所有的作用域直到找到, 否则会报未定义错误.
python中, 程序的变量并不是在哪个位置都可以访问的, 访问权限决定于这个变量是在哪里赋值的.
变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称. python的作用域一共有4种,
分别是:
有四种作用域:
 L(Local): 最内层, 包含局部变量, 比如一个函数/方法内部.
 E(Enclosing): 包含了非局部(non-local)也非全局(non-global)的变量. 比如两个嵌套函数, 一个函数(或类)A里面又
包含了一个函数B, 那么对于B中的名称来说A中的作用域就为nonlocal
 G(Global): 当前脚本的最外层, 比如当前模块的全局变量.
 B(Built-in): 包含了内建的变量/关键字等, 最后被搜索.
规则顺序: L -> E -> G -> B
在局部找不到, 便会去局部外的局部找(例如闭包), 再找不到就会去全局找, 再者去内置中找
"""
g_count = 0 # 全局作用域
def outer():
    o_count = 1 # 闭包函数外的函数中
    def inner():
        i_count = 2 # 局部作用域
"""
内置作用域是通过一个名为builtin的标准函数模块实现的, 但是这个变量名自身并没有放入内置作用域内, 所以必须导入这个文件
才能使用它. 在python中, 可以使用以下的代码来查看到底预定义了哪些变量:
import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 
'BlockingIOError', 'BrokenPipeError', 'BufferError', ...]
"""
"""
python中只有模块(module), 类(class)以及函数(def, lambda)才会引入新的作用域, 其它的代码块(如:if/elif/else/
,try/except,for/while等)是不会引入新的作用域的, 也就是说这些语句内定义的变量, 外部也可以访问, 如:
"""
a = 3
if(a > 0):
    b = 5
print("b = %d"%(b))
