"""
列表:
    1.列表的每一个值都有对应的位置值, 位置从0开始
    2.列表支持从左至右和从右至左进行切片, 从左至右时从0开始, 从右至左时从-1开始
    3.列表使用中括号[]定义
    4.列表中的元素可以是不同类型的, 元素之间用逗号隔开
"""
# 访问列表中的值
list = ['a', 'b', 'c']
print(list[0])
print(list[-1])

# 截取元素
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(list[1:5])
print(list[1:-1])
print(list[4:])
print(list[:-3])

# 更新列表
list2 = ['he','i','you']
list2[0] = 'she'
list2[-1] = 'your'
print(list2)

# 删除列表元素
list3 = ['he','i','you']
del list3[0]
print(list3)

# 列表脚本操作符
list4 = ['do','you','me']
print(len(list4))
print(list4 + ['hello','world'])
print(list4 * 2)
print('do' in list4)

# 截取与拼接
list5 = [1,2,3,4,5]
list6 = [6,7,8,9]
print(list5[:3])
list5 += list6
print(list5)

# 嵌套列表
a = ['a','b','c']
b = ['d','e','f']
c = [a,b]
print(c)
print(c[0][1])

# Python列表函数&方法
"""
函数
len(list)               列表元素个数

max(list)               返回列表元素最大值

min(list)               返回列表元素最小值

list(seq)               将元组转换为列表

方法
append(obj)                在列表末尾添加新的对象

count(obj)                 统计某个元素在列表中出现的次数

extend(seq)                在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原来的列表)

index(obj)                 从列表中找出某个值第一个匹配项的索引位置              
        
insert(index,obj)          将对象插入列表

pop(index=-1)              移出列表中的第一个元素(默认为最后一个元素), 并且返回该元素的值

remove(obj)                移除列表中某个值的第一个匹配项              

reverse()                  反向列表中的元素

sort(key=None,reverse=False)    对原列表进行排序(False表示列表不进行反转)

clear()                    清空列表

copy()                     复制列表
"""












li = [1,2,2,3,4,5]
li.append(6)
print(li)
print(li.count(6))
li.extend([4,5])
print(li)
print(li.index(2))
li.insert(1,"you")
print(li)
li.pop(-3)
print(li)
li.remove('you')
print(li)
li.reverse()
print(li)
li.sort(key=None, reverse=False)
print(li)
# li.clear()
# print(li)

print("------")
k = li.copy()
print(k)







