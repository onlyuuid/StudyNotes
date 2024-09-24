"""
条件控制:
    条件控制语句用于在满足条件的情况下执行相应的语句
    1.每个条件后面要使用冒号:, 表示接下来是满足条件后要执行的语句块
    2.使用缩进来划分语句块, 相同缩进数的语句在一起组成一个语句块
    3.Python中没有switch...case语句, 但Python3.0添加了match...case语句
"""
# if语句
list = [1, 2, 3, 4, 5]
if 1 in list:
    print('1 在集合list中')
else:
    print("1 不在集合list中")
a = 4
if a == 2:
    print('2')
elif a == 3:
    print('3')
else:
    print('a不等于2和3')
print("执行结束!")

print('=====================')
# age = int(input('请输入你家狗狗的年龄: '))
# if age <= 0:
#     print("年龄不合法!")
# elif age == 1:
#     print("相当于14岁的人")
# elif age == 2:
#     print("相当于22岁的人")
# elif age > 2:
#     human = 22 + (age - 2)*5
#     print("对应的人类年龄为: ",human)

# 实例
# number = 7
# guess = -1
# while guess != number:
#     guess = int(input("输出你猜的数字: "))
#     if guess == number:
#         print("恭喜你猜对了!")
#     elif guess > number:
#         print("你猜大了")
#     elif guess < number:
#         print("你猜小了")

# if 嵌套
# list = [1, 2, 3, 4, 5]
# a = int(input("请输入一个数:"))
# if a in list:
#     print(a,'在list中')
#     if a % 2 == 0:
#         print(a,"是一个偶数")
#     else:
#         print(a,"是一个奇数")
# else:
#     print(a,'不在list中')

# match...case
n = 5
match n:
    case 1:
        print('1')
    case 2:
        print('2')
    case 3:
        print('3')
    case _:  # 相当于java中的default
        print("默认执行!")

# 实例

def http_status(code):
    match code:
        case 200:
            return '访问成功!'
        case 403:
            return '没有权限'
        case 404:
            return '路径错误'
        case _:
            return '未知错误!'
states = 300
print(http_status(states))

# 一个case也可以设置多个条件, 多个条件之间使用 | 分隔
a = 500
match a:
    case 500|503|502:
        print("后端系统异常!")
    case _:
        print("未知系统异常!")



