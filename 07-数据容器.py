"""
python的数据容器有：
    1. 列表list，相当于数组，python的列表中可以嵌套，可以是任何元素，比如['john', 123, True, [1,2,3]]
    2. 字符串str
    3. 集合set
    4. 字典dict
    5. 元组tuple
"""

# 列表的常用操作
my_list = ['john', 'tom', 'julie']
# 1.1 查找元素的下标索引
print(my_list.index('john'))
print('------------------------------------')
# 1.2 如果元素不在列表中则报错
# print(my_list.index('Apple'))
# 2. 修改索引指向的元素的值
my_list[2] = 'Julia'
print(my_list[2])
print('------------------------------------')
# 在指定下标插入新元素
my_list.insert(3, 'Jane')
print(my_list[3])
print('------------------------------------')
# 在尾部追加元素
my_list.append('johnny')
print(my_list)
print('------------------------------------')
# 追加一批元素
another_list = ['apple', 'banana']
my_list.extend(another_list)
print(my_list)
print('------------------------------------')
# 删除指定下标的元素，如果不指定，则删除最后一个元素
my_list.pop(2)
print(my_list)
print('------------------------------------')
# del 也可以删除指定下标的元素
del my_list[2]
print(my_list)
print('------------------------------------')
# 统计某个元素在列表中的数量
print(my_list.count('john'))
print('------------------------------------')
# 统计所有元素在列表中的数量
print(len(my_list))
print('------------------------------------')
# 清空列表
my_list.clear()
print(my_list)
print('------------------------------------')
# 列表整个删除
del my_list

# 列表练习

# 创建一个列表
ages = [21, 25, 21, 23, 22, 20]
# 追加一个数字到列表尾部
ages.append(31)
# 追加一个新列表到尾部
ages.extend([29, 33, 30])
# 取出第一个元素
first_element = ages.pop(0)
print(first_element)
# 取出最后一个元素
print(ages.pop())
# 查找元素31的位置
print(ages.index(31))


# 列表循环 - 有两种方法 while/for
def list_while_loop():
    index = 0
    mylist = ['john', 'tom', 'julie']
    while index < len(mylist):
        print(mylist[index])
        index += 1


def list_for_loop():
    mylist = ['apple', 'banana', 'pear']
    for index in range(len(mylist)):
        print(mylist[index])
    for item in mylist:
        print(item)


list_while_loop()
list_for_loop()

# 元组 - tuple 定义后就无法修改，可以认为是一个只读的list
# 定义元组
my_tuple = ('john', 'tom', 'julie')
print(my_tuple)
# 定义单个元素的元组, 注意，这个逗号必须要有，否则就变成 str 类型了
t1 = ('apple',)
t2 = tuple('banana')
print(type(t2))

# 元组的常用方法 index()，count()，len()
t3 = ((1, 2, 3), ('john', 'tom', 'julie'))

# index方法与列表的使用是一致的
index = t3.index((1, 2, 3))
print(index)

# count方法，统一元素在元组中出现的次数
count = t3[0].count(t3[0][1])  # 出现1次
print(count)

print(len(t3))  # 长度为2

# 字符串概念及常用方法
# 字符串也是一种数据容器，它也是不能修改的
my_str = ' apple is a very good fruit.  '

# index方法与其他类型的用法及行为是一样的
# split方法，使用特定字符分隔字符串，返回一个列表，默认是空字符' '
split_my_str = my_str.split()  # ['apple', 'is', 'a', 'very', 'good', 'fruit.']
print(split_my_str)

# strip方法，移除特定字符，默认是空字符
my_str1 = ' hello world     '  # 移除前后空字符
print(my_str1.strip())
my_str2 = '12hello Python123'
print(my_str2.strip('32'))

# 统计字符串中的某个字符出现的次数
print(my_str2.count('o'))

# 统计字符串的长度
print(len(my_str2))

# 字符串练习
my_str3 = 'itheima itcase boxuegu'

# 有多少个'it'字符
print(my_str3.count('it'))
# 空格替换为'|'
result_str = my_str3.replace(' ', '|')
print(result_str)
# 按照'|'分隔字符串
print(result_str.split('|'))
