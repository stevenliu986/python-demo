# # 导入随机数模块
import random
#
# # 1. 随机生成1-10之间的数字
# secret_num = random.randint(1, 10)
#
# # 2. 设定最多3次机会
# chance = 3
#
# print("=== 猜数字游戏 ===")
# print("规则：我已经想好了1~10之间的一个数字，你有3次机会猜中它！")
#
# # 3. 循环让用户猜数字
# while chance > 0:
#     # 提示剩余次数
#     print(f"\n你还剩 {chance} 次机会")
#
#     # 获取用户输入
#     try:
#         guess = int(input("请输入你猜的数字："))
#     except ValueError:
#         print("请输入有效的整数！")
#         continue
#
#     # 4. 判断大小
#     if guess > secret_num:
#         print("猜大了！")
#     elif guess < secret_num:
#         print("猜小了！")
#     else:
#         # 猜对了
#         print(f"恭喜你！猜对啦！正确数字就是 {secret_num}")
#         break
#
#     # 每次猜错减少一次机会
#     chance -= 1
#
# # 5. 用完所有机会还没猜对
# if chance == 0 and guess != secret_num:
#     print(f"\n游戏结束！你用完了所有机会")
#     print(f"正确数字是：{secret_num}")

# 求1-100的和
sum_num = 0
i = 0
while i < 100:
    i += 1
    sum_num += i

print(sum_num)

# 第2种方法，公式求和，时间复杂度为O(1)
num = 100
sum = num * (num + 1) // 2
print(sum)

# 设置一个范围 1 - 100 随机整数变量，通过 while 循环配合 input 判断输入的数字是否等于随机数
count = 1
guess = int(input('请输入一个数字：'))
ramdom_num = random.randint(1, 100)
while guess != ramdom_num:
    count += 1
    if guess > ramdom_num:
        print('大了')
        guess = int(input('请输入一个数字：'))
    else:
        print('小了')
        guess = int(input('请输入一个数字：'))

print(f'你猜了{count}次才猜对。')

# 上述代码的优化版本
count = 0
random_num = random.randint(1, 100)
while True:
    guess = int(input('请输入一个数字：'))
    count += 1
    if guess > random_num:
        print('大了')
    elif guess < random_num:
        print('小了')
    else:
        break

print(f'你猜了{count}次才猜对。')