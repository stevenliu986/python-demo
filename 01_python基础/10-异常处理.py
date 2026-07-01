"""
捕获异常 - 语法
    try:
        可能发生异常的代码
    except:
        如果出现异常执行的代码
    else: 这部分是可选的
        未发生异常执行这部分
    finally: 这部分是可选的
        不管有没有异常，这里的代码都会执行
"""

try:
    fr = open('../bill.txt', 'r', encoding='utf-8')
    print(fr.read())
except:
    fw = open('../bill.txt', 'w', encoding='utf-8')
    fw.write('hello CBA, I am coming. HaHaHa')
    fw.close()

"""
捕获指定异常 - 语法
    try:
        可能发生异常的代码
    except NameError as e:
        如果出现异常执行的代码
    注意：1. 如果尝试执行的代码的异常类型和要捕获的异常的类型不一样，则无法捕获异常
         2. 一般try下方只放一行尝试执行的代码
"""

# 捕获指定异常
try:
    print(name)
except NameError as e:
    print(e)

# 当需要捕获多个指定异常的话，可以将要捕获的异常以元组的形式书写
try:
    print(1/0)
except (ZeroDivisionError, NameError) as e:
    print(e)

# 除了可以使用except来捕获所有异常外，还可以使用Exception来捕获所有异常
try:
    print(1/0)
except Exception as e:
    print(type(e))

# 异常的传递
def func01():
    print('这是func01的开始')
    num = 1/0
    print('这是func01的结束')

def func02():
    print('这是func02的开始')
    func01()
    print('这是func02的结束')

def main(): # 由于func01没有对异常进行捕获，所以异常在这里捕获了
    try:
        func02()
    except Exception as e:
        print(e)
main()