# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# 这是我的第一个python程序
print("零基础，学python，月薪过万，就来黑马程序员。");

money:float = 50.49;

print(money);

money = money - 10;

print(money);

# money = "money";
# print(money);
money = money + 10;
print(money);

money = money - 10.49;
print(int(money));
print(type(str(money)));

# 占位符拼接字符串
class_year = 57
class_salary = 16678
print('北京第%s期的学员平均工资是%s元。' % (class_year,class_salary))

# 控制精度
a = 12.234
b = 23
print('第一个数的精度控制在小数点后2位%.2f' % a)

# 第2种格式化字符串的方式
print(f'北京第{class_year}期的学员平均工资是{class_salary}元')

# 使用 input 来接收输入
# print('Your name: ')
# name = input()
# print('你的名字是%s' % name)

# age: int = 10
# if age >= 18:
#     print("我已经成年了")
#     print('我即将进入大学了')
#
# print('这一行也打印吗？')
#
# age = input('请输入你的年龄：')
# if (int(age) > 18):
#     print('你已成年，需要补票10元')
#     print('祝你游玩愉快')

# height = int(input('请输入你的身高：'))
# height_rule = 120
# ticket_fare = 10
# if height > height_rule:
#     print(f'你的身高超过{height_rule}CM，需要购票{ticket_fare}元。')
# else:
#     print(f'你的身高未超过{height_rule}CM，可以免费游玩。')


# age = 10
# height = 110
# if age >= 18:
#     if height >= 120:
#         print('old + tall')
#     else:
#         print('old + not tall')
# else:
#     if height >= 120:
#         print('young + tall')
#     else:
#         print('young + not tall')

# image_num = 10
# if int(input('请输入第一次猜想的数字：')) == image_num:
#     print('你猜对了。')
# elif int(input('请输入第二次猜想的数字：')) == image_num:
#     print('你猜对了。')
# elif int(input('请输入第三次猜想的数字：')) == image_num:
#     print('你猜对了。')
# else:
#     print('你都没猜对。')

#
