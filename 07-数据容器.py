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


list_while_loop()
list_for_loop()
