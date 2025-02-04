"""
两数之和

def sum(a,b):
    return a+b

print("请输入第一个数字:")
a = int(input())
print("请输入第二个数字:")
b = int(input())
print("a 与 b 的和为:",sum(a,b))
"""

"""
交换两个变量的值

def swap(a,b):
    a,b = b,a
    return a,b # 返回的是一个元组
a = 3
b = 5
print("交换前: a = ",a,",b = ",b)
a,b = swap(a,b)
print("交换后: a = ",a,",b = ",b)
"""

"""
判断一个数是奇数还是偶数

def isBase(n):
    if n % 2 == 0:
        print(f"n = {n},n 为 偶数")
    else:
        print(f"n = {n},n 为 奇数")
print("请输入一个整数:")
n = int(input())
isBase(n)
"""

"""
生成一个包含1到10的列表，并打印

def getlist():
    li = list(range(1,11))
    print(f"生成列表: {li}")
getlist()
"""

"""
计算列表中所有元素的和

def sum(li):
    sum = 0
    for i in li:
        sum += i
    print(f"li 列表的和为: {sum}")
li = [32,5,6,1,12,14,7,21]
sum(li)
"""

"""
找出列表中的最大值

def max(list):
    m = 0
    for i in list:
        if i > m:
            m = i
    print(f"li 中的最大值为: {m}")
li = [32,5,6,1,12,14,74,21]
max(li)
"""

"""
反转一个字符串

def reversal(s):
    new_s = s[::-1] # 步长为-1表示将字符串反转
    print(f"原始字符串: {s}")
    print(f"反转后的字符串: {new_s}")
print("请输入一个字符串:")
s = str(input())
reversal(s)
"""

"""
判断一个数是否为质数

def is_prime_number(n):
    if n <= 1:
        print(f"{n} 不是质数")
        return False
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} 不是质数")
            return False
    print(f"{n} 是质数")
    return True
print("请输入一个整数:")
n = int(input())
is_prime_number(n)
"""

"""
输出斐波那契数列的前10项

def fibonacci(n):
    fib = [0, 1]  # 初始前两项
    for i in range(2, n):
        next_val = fib[i-1] + fib[i-2]
        fib.append(next_val)
    return fib[:n]  # 返回前n项

# 生成前10项
result = fibonacci(10)
print(result)  # 输出: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
"""

"""
将摄氏温度转换为华氏温度（公式：F = C * 9/5 + 32）

def convert_temperature(c):
    f = c * 9/5 + 32
    return f
print("请输入一个整数:")
c = int(input())
f = convert_temperature(c)
print(f"{c}摄氏度等于:{f}华氏度")
"""

"""
计算圆的面积（输入半径，输出面积）

import math
def get_circle_area(radius):
    s = math.pi * radius ** 2 # ** 表示指数关系
    return round(s,2) # 保留两位小数

print("请输入圆的半径:")
r = float(input())
s = get_circle_area(r)
print(f"半径为 {r} 的圆的面积为:{s}")
"""

"""
判断一个字符串是否为回文(是否对称,如madam)

def is_palindrome(s):
   if s == s[::-1]:
       print("该字符串为回文字符串")
   else:
       print("该字符串不是回文字符串")

print("请输入一个字符串:")
s = input()
is_palindrome(s)
"""

"""
统计字符串中某个字符出现的次数

def get_char_number(c,s):
    count = 0
    for char in s:
        if char == c:
            count+=1
    return count

print("请输入一个字符串:")
s = input()
print("请输入要统计的字符:")
c = input()
n = get_char_number(c,s)
print(f"{c} 字符在字符串 {s} 中出现了:{n}次")
"""

"""
找出列表中重复的元素

def get_repetition(li):
    repetition = []
    for i in range(0, len(li)):
        for j in range(i+1, len(li)):
            if li[i] == li[j]:
                repetition.append(li[i])
    print(f"{li}中重复的元素有: {repetition}")
li = [32,2,4,54,65,7,2,7,4]
get_repetition(li)
"""

"""
合并两个字典

def merge_dict(dict1, dict2):
    dict1.update(dict2) # 将set2添加进set1中
    return dict1

dict1 = {"name":"李四"}
dict2 = {"age":12}
dict3 = merge_dict(dict1, dict2)
print(f"set1与set2合并后为: {dict3}")
"""

"""
读取文本文件并统计行数

def read_file(filename):
    with open(filename,"r",encoding='utf-8') as f: # with 在读取完文件后会关闭文件
        content = f.read()
        lines = content.splitlines() # 按行进行切割
        print(f"读取到文件{filename}的内容为:\n{content}")
        print(f"共 {len(lines)} 行")

read_file("file/1.txt")
"""

"""
计算输入数字的阶乘

def calculated_factorial(n):
    if n == 0:
        return 1 # 0 的阶乘为1
    return n * calculated_factorial(n-1)

print("请输入一个整数:")
n = int(input())
cn = calculated_factorial(n)
print(f"{n}的阶乘为:{cn}")
"""

"""
输出九九乘法表

def multiplication_table():
    for i in range(1, 10):
        for j in range(1, i+1): # 实现直角三角的核心在于j的范围随着i的增大而增大
            print(f"{j} * {i} = {i * j}", end="\t")
        print()

multiplication_table()
"""

"""
生成一个包含10个随机数（1-100）的列表

def get_random(range_end):
    random_list = []
    for i in range(10):
        random_number = int(random.randint(0, range_end))
        random_list.append(random_number)
    return random_list

print("请输入要获取的随机数的范围:")
numner = int(input())
list = get_random(numner)
print(f"生成{numner}以内的随机数列表为:{list}")
"""




