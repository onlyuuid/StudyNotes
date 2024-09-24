"""
借书
"""
from datetime import date


def borrow_books(name, list):
    for item in list:
        for key in item:
            if item[key] == name:
                if item['state'].__eq__('已借出'):
                    return 2
                borrow_time = str(input("请输入借阅时间: \n"))
                item['borrow_time'] = borrow_time
                item['state'] = '已借出'
                item['borrow_count'] += 1
                return 1
            else:
                if item.__eq__(list[len(list) - 1]) and item[key] != name:
                    return 0
                continue

def return_books(name, list):
    for item in list:
        for key in item:
            if item[key] == name:
                if item['state'].__eq__('未借出'):
                    return 2
                item['return_time'] = date.today()
                item['state'] = '未借出'
                item['borrow_time'] = '暂无'
                return 1
            else:
                if item.__eq__(list[len(list) - 1]) and item[key] != name:
                    return 0
                continue
"""
删除图书
"""
def del_books(name, list):
    for item in list:
       if item['name'] == name:
           list.remove(item)
           return True
       else:
           return False