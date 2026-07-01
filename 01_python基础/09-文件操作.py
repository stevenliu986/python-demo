# python打开文件使用 open 函数，语法如下：open(name, mode, encoding) - name：文件名，
# mode：操作方式（读，写，追加等），encoding：编码方式
# 特别注意：read 相关方法会接着上一次 read 方法获取的内容的末尾读取

file = open('测试.txt', 'r', encoding='utf-8')
print(type(file))

# read 方法
# print(file.read(4))  # 这是一段

# readlines 方法
# print(file.readlines())

# readline 方法
# line1 = file.readline()
# line2 = file.readline()
# line3 = file.readline()
# print(line1)
# print(line2)
# print(line3)

# 循环读取文件内容
# for line in file:
#     print(line)

# 关闭文件
file.close()

# with open 操作文件，会自动关闭文件
# with open('测试.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         print(line)


# 文件写入 - file.write(str)
file = open('测试.txt', 'w', encoding='utf-8')
# 写入内容
file.write('CBA I am coming')
# 刷新文件
file.flush()
file.close()

# 文件追加
# 打开一个不存在的文件（会新建它并写入内容）
file1 = open('test.txt', 'a', encoding='utf-8')
file1.write('Hello CBA, I am coming. ')
file1.flush()
file1.close()
file2 = open('test.txt', 'r', encoding='utf-8')
print(file2.read())
