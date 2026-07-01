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

# 继承：有单继承和多继承 - 单继承语法 class 类名(父类)
class Person(People):
    __gender = None

    def __init__(self, name, age, gender=None):
        # 调用父类的构造函数
        super().__init__(name, age)
        # 给子类的成员变量赋值
        self.__gender = gender

# 多继承 - 多继承语法 class 类名(父类1，父类2，父类3，...，父类n)
# 注意：如果被继承的父类中的成员属性或成员方法，则按照从左到右的方式决定优先级，即父类1>父类2>父类3>...>父类n
class Phone:
    brand = 'iPhone'
    number = '13939939909'

    def call_4g(self):
        print(f'4g通话中')

class NFCReader:
    nfc_type = '第五代NFC'

    def read_card(self):
        print(f'NFC 读卡')

    def write_card(self):
        print(f'NFC写卡')

class RemoteController:
    rc_type = '红外遥控'

    def control(self):
        print(f'红外遥控开启了')

class MyPhone(Phone, NFCReader, RemoteController):
    # 如果该子类不再有新的成员变量和成员方法，则可以用 pass
    pass

my_phone = MyPhone()
my_phone.read_card()
my_phone.call_4g()

# 复写父类中的成员属性或方法
# 定义子类并复写父类的成员属性和方法
class HisPhone(Phone):
    # 复写父类的成员属性
    brand = 'Huawei Mate 90'

    # 复写父类的成员方法
    def call_4g(self):
        print(f'Huawei mate 90进行4g通话了')
        super().call_4g()


his_phone = HisPhone()
his_phone.call_4g()
print(HisPhone.brand)
print(HisPhone.number)
