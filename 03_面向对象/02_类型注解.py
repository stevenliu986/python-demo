# 类型注解 - python在3.5版本引入了类型注解，以方便静态类型检查工具，IDE等第三方工具。
# 类型注解：在代码中涉及数据交互的地方，提供数据类型的注解（显式的说明）
# 主要功能：1. 帮助第三方IDE工具对代码进行类型推断，协助作代码提示；2. 帮助开发者自身对变量进行类型注释
# 注意：类型注解并没有强制性，即使类型注解错误，也不会影响程序的运行

from __future__ import annotations # 所有文件都应该加上这句，尤其是包含类型注解的项目

# 对变量进行类型注解 - 语法：变量:类型
age: int = 10
hasValue: bool = False

# 对类的实例进行类型注解
class Person:
    pass

p: Person = Person()

# 基础容器类型注解
my_books_list: list = ['Java', 'Python', 'JS', 'TS']
my_books_tuple: tuple = ('Java', 'Python', 'JS', 'TS')
my_books_dict: dict= {'Java':'Java on detail', 'Python':'Python on detail', 'JS':'Think on JS'}
my_books_str: str = 'Java on detail'
my_books_set: set= set(my_books_list)

# 容器类型详细注解
my_books_list1: list[str] = ['Java', 'Python', 'JS', 'TS']
# 元组需要给每一个元素的类型都标注出来
my_books_tuple1: tuple[int, int, int] = (1, 2, 3)
my_books_dict1: dict[int, str] = {1: 'Java', 2: 'Python', 3: 'JS'}
try:
    print(my_books_dict1[1])
except Exception as e:
    print(e)

# 在注释中进行类型注解
var_1 = 10 # type: int
var_2 = True # type: bool

# 函数/方法的类型注解
def func(data: list[int])-> int:
    data.append(var_1)
    return data[0]

