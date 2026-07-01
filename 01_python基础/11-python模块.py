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
result = my_module1.add(1, 2)
print(result)

# 导入python包中的方法 - 语法 import 包名.模块名 或 from 包名 import 模块名
import my_package.my_module1
result = my_package.my_module1.decrement(2,1)
print(result)

from my_package import my_module1
result1 = my_module1.decrement(5 - 10,1)
print(result1)

"""
第三方包及如何安装，由于是第三方包，python并没有内置，所以必须要安装才能进行导入使用
安装：
    使用 python3 -m pip 命令进行安装
    python3 -m pip install 包名。例如：python3 -m pip install numpy
注：我当前的mac使用的是pipx install 包名 这样的命令
"""

from my_utils import str_util
result1 = str_util.str_reverse('hello');
print(result1)
result2 = str_util.substr('hello', 1,2)
print(result2)