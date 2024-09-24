'''
数据结构
'''
# 1.列表
'''
Python中的列表是可变的, 这是它区别于字符串和元组的最重要的特点, 即: 列表可以修改, 而字符串和元组不能.
Python中列表的方法:
方法                     描述
list.append(x)          把一个元素添加到列表的结尾,相当于a[len(a)] = [x]

list.extend(L)          通过添加指定列表的所有元素来扩充列表, 相当于a[len(a)] = L

list.insert(i,x)        在指定位置插入一个元素. 第一个参数是准备插入的索引(位置)

list.remove(x)          删除列表中值为x的第一个元素. 如果没有这样的元素, 就返回一个错误

list.pop([i])           从列表的指定位置移出元素, 并将其返回. 如果没有指定索引, a.pop()返回最后一个元素.
                        元素随即从列表中被移除. (方法中i两边的方括号表示这个参数是可选的)
                        
list.clear()            移除列表中的所有项

list.index(x)           返回列表中第一个值为x的元素的索引. 如果没有匹配的元素就会返回一个错误.

list.count(x)           返回x在列表中出现的次数

list.sort()             对列表中的元素进行排序

list.reverse()          倒排列表中的元素

list.copy()             返回列表的浅复制, 等于a[:]
'''
# 实例
a = [54.66,765.65,54.66,98.65]
print(a.count(54.66),a.count(765.65),a.count(1)) # 2 1 0

a.insert(4,12.22)
print(a) # [54.66, 765.65, 54.66, 98.65, 12.22]

print(a.index(98.65))  # 3

a.remove(765.65)
print(a) # [54.66, 54.66, 98.65, 12.22]

a.reverse()
print(a) # [12.22, 98.65, 54.66, 54.66]

a.sort()
print(a) # [12.22, 54.66, 54.66, 98.65]

a.clear()
print(a) # []

# 将列表当做栈使用
'''
在Python中, 可以使用列表(list)来实现栈的功能. 栈是一种后进先出的数据结构, 意味着最后添加的元素最先被移除. 列表提供了
一些方法, 使其非常合适于操作, 特别是append()和pop()方法
用append()方法可以把一个元素添加到栈顶, 用不指定索引的pop()方法可以把一个元素从栈顶释放出来.
栈操作:
    压入(push): 将一个元素添加到栈的顶端
    弹出(pop):  移出并返回栈顶元素
    检查栈顶元素(peek/top): 返回栈顶元素而不移出它
    检查是否为空(isEmpty): 检查栈是否为空
    获取栈的大小(size): 获取栈中元素的数量 
'''

# 1. 创建一个空栈
stack = []

# 2.压入(push)操作
stack.append('a')
stack.append('b')
stack.append('c')
print(stack) # ['a', 'b', 'c']

# 3.弹出(pop)操作
stack.pop()
print(stack) # ['a', 'b']

# 4.查看栈顶元素
print(stack[-1]) # b

# 5.检查栈是否为空
print(len(stack) == 0) # False

# 6.获取栈的大小
print(len(stack)) # 2

# 将列表当做队列使用
'''
在Python中, 列表(list)可以用作队列(queue), 但由于列表的特点, 直接使用列表来实现队列并不是最优的选择.
队列是一种先进先出的数据结构, 意味着最早添加的元素最先被移除.
使用列表时, 如果频繁地在列表的开头插入或删除元素, 性能会收到影响, 因为这些操作的时间复杂度是O(n), 为了解决这个问题,
Python提供了collections.deque, 它是双端队列, 可以在两端高效地添加和删除元素.
'''

# 1.使用collections.deque实现队列
'''
collections.deque是Python标准库的一部分
'''
from collections import deque

# 创建一个空队列
queue = deque()

# 向尾部添加元素
queue.append('a')
queue.append('b')
queue.append('c')

print(queue) # deque(['a', 'b', 'c'])

# 从队首移除元素
front_element = queue.popleft()
print('移除的元素:',front_element) # 移除的元素: a
print('队列状态:',queue) # 队列状态: deque(['b', 'c'])

# 查看队首元素(不移除)
front_element = queue[0]
print("队首元素:",front_element) # 队首元素: b

# 检查队列是否为空
is_empty = len(queue) == 0
print(is_empty) # False

# 获取队列的大小
size = len(queue)
print(size) # 2

# 2.使用列表实现队列

# 创建队列
queue = []

# 向队尾添加元素
queue.append('a')
queue.append('b')
queue.append('c')
print('队列状态:',queue) # 队列状态: ['a', 'b', 'c']

# 从队首移除元素
'''
使用pop[0]方法从队首移除元素
'''
first_pop = queue.pop(0)
print('移出的元素:',first_pop) # 移出的元素: a
print('队列状态:',queue) # 队列状态: ['b', 'c']

# 查看队首元素(不移除)
front_element = queue[0]
print('队首元素:',front_element) # 队首元素: b

# 检查队列是否为空
is_empty = len(queue) == 0
print(is_empty) # False

# 获取队列的大小
size = len(queue)
print('队列大小:',size) # 队列大小: 2

# 实例(使用列表实现队列)
class Queue:

    def __init__(self):
        self.queue = []

    # 入队
    def enqueue(self, x):
        self.queue.append(x)

    # 出队
    def dequeue(self):
        if not is_empty:
            return self.queue.pop(0)
        else:
            raise IndexError('Queue is empty')

    # 查看队首元素
    def peek(self):
        if not is_empty:
            return self.queue[0]
        else:
            raise IndexError('Queue is empty')

    # 判断队列是否为空
    def is_empty(self):
        return len(self.queue) == 0

    # 获取队列的大小
    def size(self):
        return len(self.queue)



queue = Queue()
queue.enqueue('a')
queue.enqueue('b')
queue.enqueue('c')

print('队首元素:',queue.peek()) # 队首元素: a
print('队列大小:',queue.size()) # 队列大小: 3
print('移出的元素',queue.dequeue()) # 移出队列元素 a
print('队列是否为空',queue.is_empty()) # False
print('队列大小',queue.size()) # 队列大小 2

# 列表推导式
'''
列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定
条件创建子序列。
每个列表推导式都在for后面跟一个表达式，然后有零到多个for或if子句。返回结果是一个根据表达式从其后的for和if上下文环境中生长出来的列表。如果希望
表达式推导出一个元祖，就必须使用括号。
'''
vec = [1,2,3]
res = [x*3 for x in vec]
print('res的结果为:',res)

# 推导二维列表
list2 = [2,3,4]
two_list = [[x,x*2] for x in list2]
print(two_list) # [[2, 4], [3, 6], [4, 8]]

# 将序列里的每个元素逐个调用某个方法
s4 = ['  google  ',' baidu   ','   alibaba ']
formation = [s.strip() for s in s4] # strip 去掉元素的前后空格
print(formation) # ['google', 'baidu', 'alibaba']

# 可以使用if语句进行过滤
numbers = [1,2,4,5,6,7,8,9]
x = [i for i in numbers if i > 4]
print(x)

'''
注意:
在 Python 中，推导式可以用于生成列表、集合、字典等数据结构，但不能直接用于生成元组。不过，可以使用推导式生成一个列表，然后将其转换为元组。
'''

# 循环和其他技巧
s2 = [2,4,-2,5]
s3 = [-4,3,5,7]
result = [x*y for x in s2 for y in s3]
print(result) # [-8, 6, 10, 14, -16, 12, 20, 28, 8, -6, -10, -14, -20, 15, 25, 35]

# 列表推导式可以使用复杂表达式或嵌套函数
d1 = [str(round(355/113, i)) for i in range(1, 6)]
print(d1)

# 嵌套列表解析
'''
Python的列表还可以嵌套, 下面是3x4的矩阵列表
'''
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
# 将3x4的矩阵转换为4x3矩阵
g1 = [[row[i] for row in matrix] for i in range(4)]
print(g1) # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 以上实例也可以使用以下方法来实现:
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed) # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# 另一种方式
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed) # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# del语句
'''
1.使用del语句可以从一个列表中根据索引来删除一个元素, 而不是值来删除元素. 这与使用pop()返回的值不同. 
2.可以使用del语句从列表中删除一个切割, 或清空整个列表
3.也可以使用del删除一个变量
'''
a = [1,2,3]
del a

# 元组和序列
'''
元组由若干逗号分隔的值组成, 例如:
'''
tuple = '李四','张三','王五'
print(tuple) # ('李四', '张三', '王五')
print(tuple[0]) # 李四
'''
注意: 元组在输出时总是有括号, 但在输入时可能有也可能没有, 不过括号对于元组是必须的
'''

# 集合
'''
集合是一个无序不重复的元素集, 基本功能包括关系测试和消除重复元素.
可以用大括号{}创建集合. 如果要创建一个空集合, 必须使用set(), 而不是使用{}. 后者创建一个空字典
'''
set01 = {'李四','张三','王五','张三'}
print(set01) # {'张三', '李四', '王五'} 去除重复

bool = '李四' in set01 # 检测成员
print(bool) # True

# 以下演示了两个集合的操作
a = set('abbcddefeghaf')
b = set('alaggjjekldag')
print(a) # {'g', 'e', 'a', 'f', 'b', 'c', 'd', 'h'}
print(b) # {'g', 'e', 'l', 'a', 'k', 'd', 'j'}
print(a - b) # {'c', 'h', 'b', 'f'} 在a中的字母但不在b中
print(a | b) # {'j', 'k', 'c', 'h', 'a', 'g', 'd', 'f', 'b', 'e', 'l'} 在a中或在b中的字母
print(a & b) # {'e', 'g', 'a', 'd'} 在a中,并且在b中的字母
print(a ^ b) # 在a中或在b中, 但不同时在a和b中的字母

# 集合也支持推导式
a = {x for x in 'abcdef' if x not in 'abc'}
print(a) # {'e', 'd', 'f'}

# 字典
'''
另一个非常有用的Python内建数据类型是字典.
序列是以连续的整数为索引, 与此不同的是, 字典是以关键字为索引, 关键字可以是任意不可变类型, 通常用字符串或数字.
理解字典的最佳方式是把它看做无序的键=>值对集合. 在同一个字典内, 关键字必须是互不相同.
使用一对大括号{} 创建一个空字典
'''
dist = {'name':'李四','age':18,'email':'65644@qq.com'}
dist['age'] = 20
print(dist) # {'name': '李四', 'age': 20, 'email': '65644@qq.com'}

# 删除字典元素
del dist['name']
print(dist) # {'age': 20, 'email': '65644@qq.com'}

# 将字典中的key提取为列表
l = list(dist.keys())
print(l) # ['age', 'email']

# 构造函数dict()直接从键值对元组列表中构建字典. 如果有固定的模式,列表推导式指定特定的键值对;
d = dict([('ls',7820),('le',420),('lsg',290)])
print(d) # {'ls': 7820, 'le': 420, 'lsg': 290}

k = {x:x*x for x in range(4)} # 字典推导式
print(k) # {0: 0, 1: 1, 2: 4, 3: 9}

# 如果关键字只是简单的字符串, 使用关键字参数指定键值对有时候更方便
d2 = dict(name='李四',age=39)
print(d2) # {'name': '李四', 'age': 39}

# 遍历技巧
'''
在字典遍历时, 关键字和对应的值可以使用items()方法同时解读出来
'''
name2 = {'name':'李四','age':19,'qq':46841145,'address':'贵阳'}
for k,v in name2.items():
    print(k,':',v)
'''
name : 李四
age : 19
qq : 46841145
address : 贵阳
'''

# 同时遍历两个或更多序列, 可以使用zip()组合
m1 = ['name','question','favorite','color']
m2 = ['hand','ear','nose','eye']
for item1,item2 in zip(m1,m2):
    print(f"this is my {item1}, this is my {item2}")

# 要反向遍历一个序列, 首先指定这个序列, 然后调用reverse()函数
for i in reversed(range(1,10,2)):
    print(i)
'''
9
7
5
3
1
'''

# 要按顺序遍历一个序列, 使用sorted()函数返回一个已经排序的序列, 并不修改原值
b3 = ['apple','orange','app','color','black','distinct','eye']
for item in sorted(set(b3)):
    print(item) #
'''
app
apple
black
color
distinct
eye
orange
'''



