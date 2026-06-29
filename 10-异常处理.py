"""
捕获异常 - 语法
    try:
        可能发生异常的代码
    except:
        如果出现异常执行的代码
"""

try:
    fr = open('bill.txt','r', encoding='utf-8')
    print(fr.read())
except:
    fw = open('bill.txt', 'w', encoding='utf-8')
    fw.write('hello CBA, I am coming. HaHaHa')
    fw.close()
