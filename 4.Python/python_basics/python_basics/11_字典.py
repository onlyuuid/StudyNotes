"""
字典:
    1.字典是一种键值对的数据结构
    2.每个键值(key=>value)对用冒号:分隔, 每个对之间用逗号(,)分隔, 整个字典包括在花括号{}内
    3.字典的键必须是不可变类型(如:数字,字符串), 值可以是任意类型
"""
# 定义字典
dictionary = {'name':'李四','age':12}

# 创建空字典
# 使用大括号创建空字典
emptyDict = {}
print(emptyDict)
print('len:',len(emptyDict))
print(type(emptyDict))

# 使用内建函数dict()创建字典
emptyDict = dict()
print(emptyDict)

# 访问字典里的值
# 把相应的键放到方括号中, 如:
dict2 = {'name':'李四','age':12,'address':'北京'}
print(dict2['name'])
print(dict2['age'])

# 修改字典
dict3 = {'name':'张三','age':23}
dict3['name'] = '王五'
print(dict3['name']) # 更新name
dict3['email'] = '77979879@qq.com'  # 添加属性
print(dict3)

# 删除字典元素
"""
    可以只删除字典中的某个元素, 也可以清空整个字典
    显式的删除一个字典可以使用del命令
"""
dict4 = {'name':'王五','age':20}
del dict4['name'] # 删除键name
print(dict4)
dict4.clear()     # 清空字典
print(dict4)
del dict4         # 删除字典

"""
注意: 1.在一个字典中, 不允许同一个键出现两次, 但值可以
     2.键必须是不可变类型(如数字,字符串,元组)
"""
# dict5 = {['小米','小张']:'李四'}
# print(dict5)
"""
Traceback (most recent call last):
  File "D:\Case Code\4.Python\python_basics\python_basics\字典.py", line 50, in <module>
    dict5 = {['小米','小张']:'李四'}
            ^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'list'
"""

# 字典内置和方法
"""
函数
len(dict)                   计算字典元素个数, 即键的总数

str(dict)                   输出字典, 可以打印的字符串表示

type(variable)              返回输入的变量类型, 如果变量是字典类型就返回字典类型

方法
dict.clear()                删除字典内所有元素

dict.copy()                 返回一个字典的浅复制

dict.fromkeys(seq,val)      创建一个新字典, 以序列seq中元素做字典的键, val为字典所有键对应的初始值

dict.get(key,default=None)  返回指定键的值, 如键不在字典中返回default设置的默认值

key in dict                 如果在字典中返回True, 否则返回False

dict.items()                以列表返回一个视图对象

dict.keys()                 返回一个键的视图对象

dict.setdefault(key,default=None)
                             和get()类似, 但如果键不在字典中, 将会添加键并将值设置为default

dict.update(dict2)           把字典dict2的键/值更新到dict里

dict.values()                返回一个值的视图对象      

dict.pop(key[,default])      删除字典key(键)所对应的值, 返回被删除的值

dict.popitem()               返回并删除字典中的最后一对键和值              
"""
dict6 = dict.fromkeys(['name','age'],0)
print(dict6)

view = dict.items(dict6)
print(view) # dict_items([('name', '李四')])
print(dict.keys(dict6))

