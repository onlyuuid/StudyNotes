"""
注释
    在Python3, 注释不会程序的执行, 而且可以使代码更易于阅读和理解.
    Python中有单行注释和多行注释.
    Python中单行注释以 # 开头, 例如:
"""
# 这是一条单行注释
print("hello world")
# 符号后面的所有文本都被视为注释, 不会被解释器执行

# 多行注释
"""
    在Python中, 多行字符串(由三个单引号'''或者三个双引号\"""包围的文本块)在某些情况下可以被视为一种实现多行注释的技巧
"""
# 单引号(''')
'''
    这是多行注释, 用三个单引号
'''

# 双引号(""")
"""
    这是多行注释, 用三个双引号
"""

"""
注意:
    虽然多行字符串在这里被当作注释使用, 但它实际上是一个字符串, 我们只要不使用它, 它不会影响程序的运行.
    这些字符串在代码中可以被放置在一些位置, 而不起实际的执行, 从而到到注释的效果.
"""

"""
拓展说明:
    在Python中, 多行注释是由三个单引号'''或者三个双引号\"""来定义的, 而这种注释方式并不能嵌套使用. 
    当你开始一个多行注释时, Python会一直将后续的行都当作注释, 直到遇到另一组三个单引号或三个双引号
"""
# 嵌套多行注释会导致语法错误, 例如:
# """
# 这是外部的多行注释
# 可以包含一些描述性的内容
#     """
#         这是尝试嵌套的多行注释
#         会导致语法错误
#     """
# """

"""
    在这个例子中, 内部的三个单引号并没有被正确的识别为多行注释的结束, 而是被解释为普通的字符串.
    这将导致代码结构不正确, 最终可能导致语法错误
    
    如果你需要在注释中包含嵌套结构, 推荐使用单行注释(以 # 开头)而不是多行注释.
    单行注释可以嵌套在多行注释中, 而不会引起语法错误. 例如:
"""
"""
这是外部的多行注释
可以包含一些描述性的内容

# 这是内部的单行注释
# 可以嵌套在多行注释中
"""
# 这样的结构是合法的, 并且通常能够满足文档化和注释的需求.

