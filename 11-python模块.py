"""
Python的模块实际上就是一个python文件。模块能定义函数，类和变量，也能包含可执行代码
    模块在使用前要先导入，导入语法：
    [from 模块名] import [模块 | 类 | 变量 | 函数 | * ] [as 别名]：其中*表示导入全部
"""

# Python模块导入
import time

print('休眠4秒')
time.sleep(4)
print('休眠结束')

# 导入模块中的sleep方法
from time import sleep
print('准备休眠2秒')
sleep(2)
print('休眠结束')

# 使用 * 导入模块中的所有功能
from time import *
print('准备休眠3秒')
sleep(3)
print('休眠结束')

"""
自定义模块
"""
import my_module1
result = my_module1.add(1,2)
print(result)
