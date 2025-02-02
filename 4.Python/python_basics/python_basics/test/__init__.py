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


