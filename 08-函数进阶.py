"""
函数返回多个值
"""


def test_return():
    return 1, 'John', True


# 使用多个变量接收返回值
x, y, z = test_return()
print(x)
print(y)
print(z)

"""
函数传递参数的多种形式
"""


# 1. 按位置传参
def my_func(name, age, gender):
    if gender == "male":
        internal_gender = "男"
    else:
        internal_gender = '女'
    print(f'姓名：{name}, 年龄：{age}, 性别：{internal_gender}')


my_func('john', 24, 'male')

# 2. 关键字传递参数
my_func(age=45, gender='female', name='Jane')


# 3. 不定长参数 (参数类型是元组) - 用于位置形式传递参数
def user_info(*args):
    print(args)


user_info('john')


# 4. 关键字不定长参数 (参数类型是字典) - 用于关键字形式传递参数
def user_info1(**kwargs):
    print(kwargs)


user_info1(name='John')

"""函数作为参数传递"""


def test_func(func, num1, num2):
    return func(num1, num2)


def add(num1, num2):
    return num1 + num2


result = test_func(add, 1, 2)
print(result)


# lambda 匿名函数
def test_func2(func):
    return func(1, 2)


result1 = test_func2(lambda num1, num2: num1 + num2)
print(result1)
