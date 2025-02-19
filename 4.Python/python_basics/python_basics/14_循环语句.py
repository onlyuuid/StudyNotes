"""
循环语句:
    1.循环语句用于执行需要重复执行的代码块
    2.Python中有while循环和for循环
"""
# 1.while循环
# list = [1,2,3,4]
# i = 0
# while i < len(list):
#    if list[i] % 2 == 0:
#        print('list中的偶数有', list[i])
#    i += 1

# 实例: 求1-100的总和
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print("sum的和为: ",sum)

# 无限循环:

var = 1
# while var == 1: # 永远为true
#     num = int(input('请输入一个值:\n'))
#     if num % 2 == 0:
#         print("你输入的是偶数!")
#     else:
#         print("你输入的是奇数!")

# while循环使用else语句
m = 1
while m < 5:
    print('m为:',m)
    m += 1
else:
    print('m为',m,'已不满足循环条件')

# 如果while中只有一条语句, 可以将该语句与while写在同一行
g = 1
# while (g): print("hello world!")

print("Boog bye!")

# 2.for语句
"""
    Python的循环语句可以遍历任何可迭代对象, 如一个列表和字符串
"""
s = "hello world!"
for i in s:  # 遍历字符串
    print(i)

d = {'name':'李四','age':18}
for k in d: # 遍历字典
    print(d.get(k))
print(d.items())

for num in range(1,6): # 遍历值域
    print(num)
print("=====")

# for...else语句
"""
else语句用于在循环结束后执行一段代码
"""

for i in range(1,6):
    if i % 2 == 0:
        print(i)
else:
    print("循环结束了!")
"""
当循环执行完毕(即遍历完iterable中的所有元素)后, 会执行else子句中的代码, 如果在循环过程中遇到了break语句, 则会中
断循环, 此时不会执行else子句
"""

for i in range(1,6):
    if i == 3:
        print(i)
        break     # 当满足条件时, 跳出循环, 但不会执行else中的代码
else:
    print("循环体结束")

arr = ['google','facebook','youtube']
for i in range(len(arr)):
    print(i,arr[i])

# 使用range创建一个列表
list2 = list(range(6))
print(list2)



#pass 语句不做任何事情, 一般用于做占位符
# while True:
#     print("111")
#     pass

for j in 'hello world':
    if j == 'o':
        pass
        print('执行pass语句块')
    print(f'当前字母: {j}')
print("bye")