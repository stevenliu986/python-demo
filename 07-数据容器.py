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
# 查找元素的下标索引
print(my_list.index('john'))
# 如果元素不在列表中则报错
print(my_list.index('Apple'))
