"""
Python解释器
    在Linux/Unix系统上, 一般默认的Python版本为Python2.x, 我们可以将Python3安装到 /usr/local/python3目录中.
    安装完成后, 我们可以将路径/usr/local/python3/bin添加到Linux/Unix系统环境变量中, 这样就可以通过shell终端输入下面命令来启动Python3.

    $ PATH=$PATH:/usr/local/python3/bin/python3    # 设置环境变量
    $ python3 --version
    Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
"""

# 1. 交互式编程
r"""
    我们可以在命令提示符中输入"python"命令来启动Python解释器:
    PS D:\Case Code\4.Python\python_basics> python
    Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
"""
# 在Python提示符中输入以下语句, 然后按回车键查看运行结果:
"""
>>> print("hello world") 
hello world
"""

# 当键入一个多行结构时, 续航是必须的. 我们可以看下如下语句:
"""
>>> a = True
>>> b = 123
>>> if a:
...     print("a为: ",a)
...
a为:  True
"""

# 2. 脚本式编程
"""
    将如下代码拷贝至hello.py中
"""
print("hello world")
r"""
    通过以下命令执行该脚本
    PS D:\Case Code\4.Python\python_basics\python_basics\test> python .\hello.py
    hello world 输出结果
"""
print("\a")

