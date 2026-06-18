def foo(string):
    count = 0
    for char in string:
        count += 1
    return count


print(foo('hello'))
print(foo('helloworld'))


def add(a, b):
    """
    这是一个计算两数相加的函数
    :param a: 第一个参数
    :param b: 第二个参数
    :return: 返回相加的结果
    """
    return a + b


print(add(3, 4))
print(add.__doc__)


def bar():
    num = 100
    print(num)


bar()

# 综合案例
balance = 500000
name = input('请输入你的姓名')


def deposit(a):
    global balance
    balance += a
    print('------------存款------------')
    print(f'{name} 您好，这次您存入{a}元')

    get_balance(False)


def withdraw(a):
    global balance
    balance -= a
    print('------------取款------------')

    get_balance(False)


def get_balance(show_header):
    if show_header:
        print('------------查询余额------------')
    print(f'{name} 您好，您的余额为{balance}')


def main_func():
    print('------------主菜单------------')
    print(f'{name}，您好，欢迎来到ATM')
    print('查询余额，请输入1')
    print('存款，请输入2')
    print('取款，请输入3')
    print('退出，请输入4')
    return input('请输入你的选择')


while True:
    input_result = main_func()
    if input_result == '1':
        get_balance(True)
        continue
    elif input_result == '2':
        deposit_amount = input('请输入存款金额')
        deposit(int(deposit_amount))
        continue
    elif input_result == '3':
        withdraw_amount = input('请输入取款金额')
        withdraw(int(withdraw_amount))
        continue
    else:
        break
