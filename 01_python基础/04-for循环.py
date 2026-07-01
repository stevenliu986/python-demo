# 看看有几个a - itheima is a brand of itcast
name = 'itheima is a brand of itcast'
count = 0
for letter in name:
    if letter == 'a':
        count += 1

print(count)

# range语法1 - range(num)，生成一个不包含num的数字序列，比如 range(5) - 0，1，2，3，4
for num in range(5):
    print(num)

# range语法2 - range(num1,num2)，生成一个从num1到不包含num2的数字序列
for num in range(5, 10):
    print(num) # 5,6,7,8,9

# range语法3 - range(num1,num2,step)，生成一个从num1到不包含num2的步进为step的数字序列
for num in range(0, 10, 2):
    print(num) # 0,2,4,6,8


# 循环嵌套
for i in range(1,101):
    print(f'今天是向小美表白的第{i}天，坚持。')
    for j in range(1,11):
        print(f'送给小美的第{j}朵玫瑰花')
    print(f'小美我喜欢你(第{i}天表白结束)')

print(f'-----------------------------------------------')

# 九九乘法表
for i in range(1,10):
    for j in range(1, i+1):
        print(f'{j} x {i} = {i * j}', end='\t')
    print()

# 循环综合案例
import random

# 工资总数
salary_package = 10000
for employee_num in range(1,21):
    # 员工绩效分
    grade = random.randint(1,10)
    # 员工绩效分 < 5 不发工资
    if grade < 5:
        print(f'员工编号为{employee_num}的绩效为{grade}，小于5，不发工资。')
        continue
    if salary_package < 1000:
        break
    print(f'员工编号为{employee_num}的员工发工资1000元。')
    salary_package -= 1000
print(f'剩余工资为{salary_package}')