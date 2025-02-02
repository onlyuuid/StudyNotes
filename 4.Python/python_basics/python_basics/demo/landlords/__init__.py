'''
斗地主
'''
from python_basics.demo.landlords.Board import Board
import random

if __name__ == '__main__':
    count = 13
    list = []
    for i in range(count):
          for j in ["♠","♥","♣","♦"]:
              item = Board(i+1,j)
              list.append(item)
              # print(item.pattern,item.number)

    list.append("大王")
    list.append("小王")
    print("原始牌",list)
    random.shuffle(list) # 打乱
    print("洗牌后",list)
    person01 = {'name':'小张'}
    person02 = {'name': '小李'}
    person03 = {'name': '小韩'}

    item01 = []
    item02 = []
    item03 = []
    for i in range(54):
        # print(i)
        if i < 17:
            item01.append(list[i])
        elif i >= 17 and i < 34:
            item02.append(list[i])
        elif i >= 34 and i < 51:
            item03.append(list[i])
    person01['board'] = item01
    person02['board'] = item02
    person03['board'] = item03
    print(person01['name'],person01['board'])
    print(person02['name'],person02['board'])
    print(person03['name'],person03['board'])
    print("底牌",list[-3:])