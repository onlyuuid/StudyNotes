"""
===========================================控制台图书管理系统================================================
"""
from python_basics.demo.book.book_server import borrow_books,return_books,del_books

if __name__ == '__main__':
    print("===========欢迎使用图图书管理系统=============")
    print("1.查看图单")
    print("2.添加图书")
    print("3.借阅图书")
    print("4.归还图书")
    print("5.删除图书")
    print("6.退出系统")
    print("==========================================")
    # 初始化列表, 用于存储数据
    list = [{'name':'西游记','state':'已借出','borrow_time':'10天','return_time':'2024-10-10','borrow_count':2},
            {'name':'水浒传','state':'未借出','borrow_time':'暂无','return_time':'暂无时间','borrow_count':0},
            {'name':'三国演义','state':'已借出','borrow_time':'12天','return_time':'2024-10-12','borrow_count':1}]
    inp = 0
    while True:
        inp = int(input("请输入您要执行的指令序号: \n"))
        match inp:
            case 1:
                pass
                print("====================================")
                print("书名     出借状态     借出时间     归还时间     借出次数")
                if len(list) == 0:print("暂无图书")
                for item in list:
                    for key in item:
                        print(f"{item[key]}     ",end="")
                    print()
            case 2:
                pass
                name = str(input("请输入你要添加的书名: \n"))
                newBook = {}
                newBook['name'] = name
                newBook['state'] = '未借出'
                newBook['return_time'] = '暂无时间'
                newBook['borrow_count'] = 0
                list.append(newBook)
                print("添加成功!")
            case 3:
                pass
                name = str(input("请输入你要借的书名: \n"))
                res = borrow_books(name,list)
                if res == 1:
                    print("借阅成功!")
                elif res == 2:
                    print("该书已借出!")
                else:
                    print("没有相关图书!")
            case 4:
                pass
                name = str(input("请输入您要归还的书名: \n"))
                res = return_books(name,list)
                if res:
                    print("归还成功!")
                elif res == 2:
                    print("该书未借出,无需归还!")
                else:
                    print("没有相关图书")
            case 5:
                pass
                name = str(input("请输入您要删除的书名: \n"))
                res = del_books(name,list)
                if res:
                    print("删除成功!")
                else:
                    print("没有相关图书")
            case _:
                print("退出成功!")
                print("欢迎下次使用!")
                break
                pass
        pass


