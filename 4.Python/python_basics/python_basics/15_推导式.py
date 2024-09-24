"""
    Python推导式是一种独特的数据处理方式, 可以从一个数据序列构建另一个新的数据序列的结构体.
    Python推导式是一种强大且简洁的语法, 适用于生成列表, 字典, 集合和生成器. 在使用推导式时, 需要注意可读性, 尽量保持表达式简洁, 以免影响代码的可读性和可维护性.
    Python支持各种数据结构的推导:
    1.列表(list)推导式
    2.集合(set)推导式
    3.字典(dict)推导式
    4.元组(tuple)推导式
"""

# 1.列表推导式
names = ['google','baidu','ali','tenxun','yahu']
list = [name.upper() for name in names]
print(list) # ['GOOGLE', 'BAIDU', 'ALI', 'TENXUN', 'YAHU'] 将列表中的元素转换为大写

names2 = ['google','baidu','ali','tenxun','yahu']
list2 = [name.upper() for name in names2 if len(name) == 6]
print(list2) # ['GOOGLE', 'TENXUN']  将list2中满足条件的元素转换为大写

# 2.字典推导式
list = ['google','baidu','ali','tenxun','yahu']
dict = {key:len(key)for key in list} # 将list中的元素作为键,其长度作为值
print(dict) # {'google': 6, 'baidu': 5, 'ali': 3, 'tenxun': 6, 'yahu': 4}

# 3.集合推导式
list = ['google','baidu','ali','tenxun','yahu']
set = {name for name in list if len(name) < 6} # 将list中满足条件的元素用于构建出新的集合set
print(set) # {'yahu', 'ali', 'baidu'}

a = {s for s in 'dadafdafeadfas' if s not in 'daf'}
print(a) # {'e', 's'}

# 4.元组推导式(生成器表达式)
"""
元组推导式的用法和列表推导式相同, 只是元组推导式返回的是一个生成器表达式, 而列表推导式返回的是列表数据
"""
list3 = ['google','baidu','ali','tenxun','yahu']
tup = (name.upper() for name in list3 if len(name) > 3)
print(tup) # <generator object <genexpr> at 0x00000230A1FED9A0> 返回的是生成器对象
print(tuple(tup)) # ('GOOGLE', 'BAIDU', 'TENXUN', 'YAHU')  # 使用tuple函数进行解析



