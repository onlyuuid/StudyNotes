"""
    python面向对象
"""
# 1.面向对象技术简介
"""
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
方法：类中定义的函数。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：定义在方法中的变量，只作用于当前实例的类。
实例变量：在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

和其它编程语言相比，Python 在尽可能不增加新的语法和语义的情况下加入了类机制。
Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，
派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
对象可以包含任意数量和类型的数据。
"""
# 2.类定义
"""
语法格式如下:
"""
"""
class ClassName:
    <statement-1>
    <statement-2>
    ...
    <statement-n>
类实例化后, 可以使用其属性, 实际上, 创建一个类之后, 可以通过类名访问其属性.
"""

# 3.类对象
"""
类对象支持两种操作: 属性引用和实例化
属性引用使用和Python中所有的属性引用一样的标准语法: obj.name
类对象创建后, 类命名空间中所有的命名都是有效属性名. 所以如果类定义是这样:
"""
class MyClass:
    """一个简单的实例"""
    i = 12345
    def f(self):
        return "hello world"

# 实例化类
# x = MyClass()
#
# # 访问类的属性和方法
# print("MyClass 类的属性 i 为: ", x.i)
# print("MyClass 类的方法 f 输出为: ", x.f())
"""
以上创建了一个新的类实例并将该对象赋给局部变量x, x为空的对象.
执行以上程序输出结果为:
MyClass 类的属性 i 为:  12345
MyClass 类的方法 f 输出为:  hello world
"""

"""
类有一个名为__init__()的特殊方法(构造方法), 该方法在类实例化时会自动调用, 如:
"""
# def __init__(self):
#     self.data = []
"""
类定义了__init__()方法, 类的实例化操作会自动调用__init__()方法. 如下实例化类MyClass对应的__init__()方法就会被调用:
"""
class MyClass:

    def __init__(self):
        self.data = []
x = MyClass()
x.data.append(1)
print(x.data) # [1]
"""
当然, __init__()方法可以有参数, 参数通过__init__()传递到类的实例化操作上. 如:
"""
class Complex:
    def __init__(self, realpart, imagpart):
        self.realpart = realpart
        self.imagpart = imagpart
x = Complex(1, 2)
print(x.realpart, x.imagpart) # 1 2

# self代表类的实例, 而非类
"""
类的方法与普通的函数只有一个特别的区别. 它们必须有一个额外的第一个参数名称, 按照惯例它的名称是self.
"""
# class Test:
#     def prt(self):
#         print(self)
#         print(self.__class__)
#
# t = Test()
# t.prt()
"""
<__main__.Test object at 0x000002CDF5DF5ED0>
<class '__main__.Test'>
从执行结果可以看出, self代表的是类的实例, 代表当前对象的地址, 而self.class则指向类
"""
"""
self不足python的关键字, 我们把它换成其他的,如hello也是可以正常执行的
"""
class Test:
    def prt(hello):
        print(hello)
        print(hello.__class__)

t = Test()
t.prt()
"""
<__main__.Test object at 0x0000021BAEBD5F10>
<class '__main__.Test'>
"""
"""
python中, self是一个惯用的名称, 用于表示类的实例(对象)自身. 它是一个指向实例的引用, 使得类的方法能够访问和操作实例的属性
当你定义一个类, 并在类中定义方法时, 第一个参数通常被命名为self,尽管你可以使用其他名称, 但强烈建议使用self, 以
保持代码的一致性和可读性.
"""
class MyClass:
    def __init__(self,value):
        self.value = value

    def display_value(self):
        print(self.value)
# 创建一个类的实例
obj = MyClass(42)

# 调用实例的方法
obj.display_value() # 输出 42

"""
在上面的例子中, self是一个指向类实例的引用, 它在__init__构造函数中用于初始化实例的属性, 也在display_value方法
中用于访问实例的属性. 通过使用self, 你可以在类的方法中访问和操作实例的属性, 从而实现类的行为.
"""

# 4.类的方法
"""
在类的内部，使用def关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数self, 且为第一个参数, self代表的是类的
实例(相当于java中this)
"""
# 类的定义
class people:
    # 定义基本属性
    name = ''
    age = 0

    # 定义私有属性, 私有属性在类外部无法直接访问
    __weight = 0

    #定义构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def speak(self):
        print("%s说: 我 %d 岁 "%(self.name, self.age))
# 实例化people
p = people('李四',19,30)
p.speak() # 李四说: 我 19 岁

# 5.继承
"""
python同样支持类的继承, 如果一种语言不支持继承, 类就没什么意义. 派生类的定义如下:
"""
# 基类
class BaseClassName:
    name = "李四"

    def des(self):
        print(self.name)

class DerivedClassName(BaseClassName):
    name = "张三"

    def des(self):
        print(self.name)

d = DerivedClassName()
d.des()
# 实例
class people:
    name = ''
    age = 0
    __weight = 0
    # 定义构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def speak(self):
        print("%s 说: 我 %d 岁 "%(self.name, self.age))
# 单继承示例
class student(people):
    grade = ''
    def __init__(self, name, age, grade):
        people.__init__(self, name, age, grade)
        self.grade = grade
    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了, 我在读 %d 年级"%(self.name,self.age,self.grade))

s = student("ken", 10, 6)
s.speak() # ken 说: 我 10 岁了, 我在读 6 年级

# 6.多继承
"""
python同样有限的支持多继承形式. 多继承的类定义形式如下:
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-n>
需要注意圆括号中父类的顺序, 若是父类中有相同的方法名, 而在子类使用时未指定, python从左至右搜索 即方法在子类中未
找到时, 从左到右查找父类中是否包含方法.
"""
# 类定义
class people:
    # 定义基本属性
    name = ""
    age = 0
    # 定义私有属性
    __weight = 0
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    def speak(self):
        print("%s 说: 我 %d 岁"%(self.name, self.age))
# 单继承示例
class student(people):
    grade = ''
    def __init__(self, name, age, weight, grade):
        people.__init__(self, name, age, weight)
        self.grade = grade
    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了, 我在读 %d 年级"%(self.name,self.age,self.grade))
# 另一个基类, 多继承之前准备
class speaker():
    topic = ""
    name = ""
    def __init__(self, name, topic):
        self.name = name
        self.topic = topic
    def speak(self):
        print("我叫 %s, 我是一个演说家, 我演讲的主题是 %s"%(self.name, self.topic))

# 多继承
class sample(speaker,student):
    a = ""
    def __init__(self, name, age, weight, grade,topic):
        student.__init__(self, name, age, weight, grade)
        speaker.__init__(self, name, topic)
test = sample("Tim",25,80,4,"python")
test.speak() # 方法同名, 默认调用的是在括号中参数位置排前的父类的方法
#输出结果: 我叫 Tim, 我是一个演说家, 我演讲的主题是 python


# 7.方法重写
"""
如果你的父类方法的功能不能满足你的需求, 你可以在子类重写你的父类的方法, 实例如下:
"""
class Parent:
    def myMehoda(self):
        print("调用父类方法")

class Child(Parent):
    def myMehoda(self):
        print("调用子类方法")

c = Child() # 子类实例
c.myMehoda() # 之类方法
super(Child, c).myMehoda() # 用子类对象调用父类已被覆盖的方法
"""
输出结果:
调用子类方法
调用父类方法
"""
# 8.类属性与方法
"""
类的私有属性
__private_attrs: 两个下划线开头, 声明该属性为私有, 不能在类的外部使用或直接访问. 
在类内部的方法使用时self.__private_attrs

类的方法
在类的内部, 使用def关键字类定义一个方法, 与一般函数不同, 类方法必须包含参数self, 且为第一个参数, self代表的是类的实例
self的名字并不是规定死的,也可以使用this, 但最好还是按照约定使用self

类的私有方法
__private_method: 两个下划线开头, 声明该方法为私有方法, 只能在类的内部调用, 不能在类的外部调用. self.__private_method.
"""
"""
实例:
"""
# class JustCounter:
#     __secretCount = 0 # 私有变量
#     publicCount = 0   # 公开变量
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print(self.__secretCount)
#
# counter = JustCounter()
# counter.count()
# counter.count()
# print(counter.publicCount)
# print(counter.__secretCount)
"""
私有方法
"""
class Site:
    def __init__(self, name,url):
        self.name = name # public
        self.url = url   # private

    def who(self):
        print("name:",self.name)
        print("url:",self.url)

    def __foo(self):
        print("这是私有方法")

    def foo(self):
        print("这是公共方法")
        self.__foo()

x = Site("菜鸟教程","www.runoob.com")
x.who()
x.foo()
# x.__foo()
"""
这是公共方法
这是私有方法
Traceback (most recent call last):
  File "D:\StudyNotes\4.Python\python_basics\python_basics\26_面向对象.py", line 332, in <module>
    x.__foo()
    ^^^^^^^
AttributeError: 'Site' object has no attribute '__foo'
"""
"""
类的专有方法:
    __init__: 构造方法, 在生成对象时调用
    __del__: 析构函数, 释放对象时调用
    __repr__: 打印, 转换
    __setitem__: 按照索引赋值
    __getitem__: 按照索引获取值
    __len__: 获得长度
    __cmp__: 比较运算
    __call__: 函数调用
    __add__: 加运算
    __sub__: 减运算
    __mul__: 乘运算
    __truediv__: 除运算
    __mod__: 求余运算
    __pow__: 乘方

运算符重载:
python同样支持运算符重载, 我们可以对类的专有方法进行重载, 实例如下:
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Vector (%d, %d)"%(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2) # Vector (7, 8)
