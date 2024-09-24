"""
集合:
    1.集合使用大括号进行创建, 元素之间使用逗号隔开, 也可以使用set()函数创建集合
    2.集合中的元素无序且不会重复, 并且可以进行并集, 交集, 差集等常见的集合操作.
"""
parame = {'李四','王五','张三'}
parame2 = set(['李四','王五'])
print(parame2)

# 注意: 创建一个空集合必须使用set()函数, 因为大括号是用来创建空字典的
basket = {'华为','小米','苹果','三星','三星'}
print(basket) # {'三星', '小米', '华为', '苹果'} 去重

a = set('helloworld')
b = set('fklasjdlkfjs')
print(a)
print(b)

print(a - b)  # 返回集合a包含但集合b中不包含的元素集合
print(a | b)  # 返回集合a或集合b中包含的所有元素集合
print(a & b)  # 返回集合a和集合b中都包含的元素集合
print(a ^ b)  # 返回集合a和集合b中不共同拥有的元素集合

g = {x for x in 'abracadabra' if x not in 'abc'}
print(g)

# 集合的基本操作
# 1.添加元素

set1 = set()
set1.add("李四")
set1.add("张三")
# 也可以使用update(x) ,x可以是列表, 字典, 集合
set1.update([1,2],['kk','da'])
print(set1)

# 2.移出元素
set2 = {'李四','张三','王五'}
set2.remove('李四')
print(set2) # {'张三', '王五'}
# 另外也可以使用discard(x)方法, 如果删除的元素不存在也不会报错
set2.discard('王五2')
print(set2)
# 也可以使用pop()随机删除集合中的一个元素
set3 = {'李四','张三','王五','老六'}
set3.pop()
print(set3) # {'张三', '老六', '李四'}

# 3.计算集合元素个数
set4 = {'李四','张三'}
print(len(set4))

# 4.清空集合
set5 = {'李四','张三'}
print(set5.clear())

# 5.判断元素是否在集合中存在
set6 = {'李四','张三','王五'}
print('李四' in set6)

# 集合内置方法完整列表
"""
add()                       为集合添加元素

clear()                     移除集合中所有的元素

copy()                      拷贝一个集合

difference()                返回多个集合的差集 

difference_update()         移出集合中的元素, 该元素在指定的集合也存在      

discard()                   删除集合中指定的元素(没有该元素不会报错)

intersection()              返回集合的交集

intersection_update()       返回集合的交集

isdisjoint()                判断两个集合是否包含相同的元素

issubset()                  判断指定集合是否为该方法参数集合的子集

issuperset()                判断该方法的参数集合是否为指定集合的子集

pop()                       随机移除元素

remove()                    移除指定元素

symmetric_difference()      返回两个集合中不重复的元素集合

symmetric_difference()      移除当前集合中在另外一个指定集合相同的元素, 并将
                            另外一个指定集合中不同的元素插入到当前集合中.

union()                     返回两个集合的并集

update()                    给集合添加元素

len()                       计算集合元素个数

"""
set7 = {'李四','张三','王五'}
set8 = {'李四','老六','罗七'}
print(set7.difference(set8))

set8.difference_update(set7)
print(set8) # {'罗七', '老六'} 从set8中移除set7中也包含的元素
set9 = {'李四','张三','王五'}
set0 = {'李四'}
print(set0.issubset(set9))
print(set9.issuperset(set0))

set11 = {'李四','张三','王五'}
set12 = {'李四','老六','罗七'}
print(set11.symmetric_difference(set12))
set11.symmetric_difference_update(set12)
print(set11) # {'老六', '王五', '罗七', '张三'}




