'''
在Python中, 模块是一个包含Python代码的文件, 通常用于组织和重用代码. 一个模块可以包含变量,函数,类,甚至其他模块.
通过使用模块, 可以将代码分成多个文件, 更加模块化和易于维护.
'''
# 1.创建模块
'''
一个模块就是一个.py文件. 你可以通过创建一个包含Python代码的文件, 直接作为模块使用. 例如:
创建一个名为 my_module.py的模块
'''

# 2.导入模块
import test.my_module

print(test.my_module.my_function())

print(test.my_module.pi)

# 3.导入特殊的对象
'''
如果只需要模块中的特定部分, 可以使用from...import...语法
'''
from test import my_module

print(my_module.my_function()) # Hello World

# 4.模块搜索路径
'''
当你导入一个模块时, Python会在几个位置查找该模块.
    1.当前脚本所在的目录
    2.PYTHONPATH环境变量中列出的目录
    3.Python的安装目录中标准库所在的目录
可以通过下面方式查看Python查找模块的路径
'''
import sys
print(sys.path)
# ['D:\\Case Code\\4.Python\\python_basics\\python_basics',
# 'D:\\Case Code\\4.Python\\python_basics',
# 'D:\\Program Files\\PyCharm 2024.1.3\\plugins\\python\\helpers\\pycharm_display',
# 'D:\\Program Files\\Python3\\python312.zip',
# 'D:\\Program Files\\Python3\\DLLs',
# 'D:\\Program Files\\Python3\\Lib',
# 'D:\\Program Files\\Python3',
# 'D:\\Case Code\\4.Python\\python_basics\\venv',
# 'D:\\Case Code\\4.Python\\python_basics\\venv\\Lib\\site-packages',
# 'D:\\Program Files\\PyCharm 2024.1.3\\plugins\\python\\helpers\\pycharm_matplotlib_backend']

# 5.标准库模块
'''
Python自带了大量的标准库模块, 你可以直接导入并使用,如
'''
import math
print(math.sqrt(4))  # 2.0

# 6.第三方模块
'''
你还可以安装和使用第三方模块, 通常使用pip来安装
>> pip install requests
然后在代码中导入该模块
import requests
response = requests.get('http://httpbin.org/get')
print(response.text)
'''

# 7.包
'''
包是一个包含模块的文件夹. 一个包至少需要包含一个名为__init__.py的文件, 即使该文件是空的.
'''

