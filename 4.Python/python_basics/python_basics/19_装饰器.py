'''
装饰器是Python中的一种高级功能, 它允许你动态的修改函数或类的行为.
装饰器是一种函数, 它接受一个函数作为参数, 并返回一个新的函数或修改原来的函数.
装饰器的语法使用@decorator_name来应用在函数或方法上.
Python还提供了一些内置的装饰器, 比如@staticmethod和@classmethod, 用于定义
静态方法和类方法.
装饰器应用场景:
    日志记录: 装饰器可用于记录函数的调用信息, 参数和返回值.
    性能分析: 可以使用装饰器来测量函数的执行时间.
    权限控制: 装饰器可用于限制对某些函数的访问权限.
    缓存: 装饰器可用于实现函数的结果缓存, 以提高性能.
'''

# 1.基本语法
'''
Python装饰器允许在不修改原有函数代码的基础上, 动态地增加或修改函数的功能, 
装饰器本质上是一个接受函数作为输入并返回一个新的包装过后的函数对象.
'''
def before_call_code():
    print('before_call_code...')

def after_call_code():
    print('after_call_code...')
def decorator_func(original_function):
    def wrapper(*args, **kwargs):
        # 在调用原始函数前添加新的功能
        before_call_code()

        result = original_function(*args, **kwargs)

        # 在调用原始函数后添加新的功能
        after_call_code()
        return result
    return wrapper

@decorator_func
def some_func(arg1,arg2):
    print("原始函数执行逻辑...")

res = some_func(1, 2)

# 使用装饰器
'''
装饰器通过@符号应用在函数定义之前, 如:
@time_logger
def target_function():
    pass
    
等同于:
def target_function():
    pass
    target_function = time_logger(target_function)

这会将target_function函数传递给decorator装饰器, 并将返回的函数重新赋值给target_function.
从而, 每次调用target_function时, 实际上是调用了经过装饰器处理后的函数.
通过装饰器, 开发者可以在保持代码整洁的同时, 灵活且高效地扩展程序的功能.
'''

# 带参数的装饰器
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f'Hello,{name}')

greet('John')
'''
Hello,John
Hello,John
Hello,John
'''

# 类装饰器
'''
除了函数装饰器, Python还支持类装饰器. 类装饰器是包含__call__方法的类, 它接受一个函数作为参数, 并返回新的函数.
'''
class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # 在调用原始函数之前执行的代码
        self.func(*args, **kwargs)
        # 在调用原始函数之后执行的代码

@DecoratorClass
def my_function():
    print('my_function...')

my_function() # my_function...



