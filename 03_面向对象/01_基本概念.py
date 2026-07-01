# 声明一个类
class Student:

    # 构造函数 - 内置方法
    def __init__(self, name, age, gender=None, nationality=None, homeland=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality
        self.homeland = homeland

    # 其他常用内置方法 - le,lt,eq,str
    def __str__(self): # 实际上它是 override 了 python 内置的 str 方法
        return f'{self.name}, {self.age}, {self.nationality}, {self.homeland}'

    # 这个方法中的 other 指的是另一个对象与当前对象，然后比较相同的成员变量值的大小，下面的相关方法都是
    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age

    def say_hi(self):
        print(f'Hi, 大家好！我是{self.name}，请大家多多关照。')

# 创建实例对象
stu_1 = Student('John', 21)
stu_2 = Student('Michael', 22)

print(stu_1.name) # 'John'
print(stu_1.gender) # None
print(stu_1.age < stu_2.age) # True

# 封装
class People:
    # 在成员/方法前面使用__后，就会将成员变量、成员方法声明为类中的私有变量/方法
    __name = None
    __age = None

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self, name):
        self.__set_name(name)
        return self.__name
    def __set_name(self, name):
        self.__name = name

p11 = People('John', 21)
print(p11.get_name('Michael'))

# 继承
