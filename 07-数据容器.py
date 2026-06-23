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
# 清空列表
my_list.clear()
print(my_list)
print('------------------------------------')
# 列表整个删除
del my_list
