# 面向对象高阶部分


# 使用__slots__
from enum import Enum, unique
from types import MethodType


class Student(object):
    pass


def set_age(self, age):
    self.age = age


def bind_method_to_obj():
    """
    给实例绑定方法
    :return:
    """
    s = Student()
    s.set_age = MethodType(set_age, s)
    s.set_age(10)
    print(s.age)

    # 一个实例绑定的方法对另一个实例无效,可通过给类绑定方法来实现
    # s2 = Student()  # 创建新的实例
    # s2.set_age(10)


# bind_method_to_obj()


def bind_method_to_class():
    Student.set_age = set_age
    s = Student()
    s.set_age(10)
    print(s.age)
    s2 = Student()
    s2.set_age(102)
    print(s2.age)


# bind_method_to_class()


# =================================================
# 通过 __slots__ 限制类的属性
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


def limit_class_attr():
    global s
    s = Student()
    s.name = 'kevin'
    print(s.name)
    # s.score = 100
    # print(s.score) # AttributeError...


# limit_class_attr()


# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 111


# print(g.score)


# =================================================
# 使用@property 对类的属性进行限制

# 原始属性条件限制方式
class Stud(object):
    def set_score(self, score):
        if not isinstance(score, int):
            raise ValueError("score must be a int")
        if not 0 < score <= 100:
            raise ValueError("score must between 0~100")
        self.score = score

    def get_score(self):
        return self.score


def limit_attr_val():
    global s
    s = Stud()
    s.set_score(101)
    print(s.get_score())


# limit_attr_val()

# @property 限制方式
class StudP(object):
    def __init__(self):
        self._score = None
        self._birth = None

    @property  # 把一个getter方法变成属性
    def score(self):
        return self._score

    @score.setter  # @property本身又创建了另一个装饰器@score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    # 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
    @property
    def birth(self):
        return self._birth  # 这里返回的 属性名尽量不要跟方法名重名(eg:birth),否则可能产生递归错误

    @birth.setter
    def birth(self, birth):
        self._birth = birth

    @property
    def age(self):
        return 2015 - self._birth


s = StudP()


# s.score = 111
# print(s._score)
# print(s.score)
# s.birth = 100

# =================================================
# 多重继承

class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class RunnableMixIn(object):
    def run(self):
        print('Running...')


class FlyableMixIn(object):
    def fly(self):
        print('Flying...')


class Bird(Animal):
    pass


# 各种动物:
class Dog(Mammal, RunnableMixIn):
    pass


class Bat(Mammal, FlyableMixIn):
    pass


class Parrot(Bird, FlyableMixIn):
    pass


class Ostrich(Bird, RunnableMixIn):
    pass


# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。这种设计通常称之为MixIn


# =================================================
# 定制类
class Std(object):

    def __init__(self, name):
        self.name = name

    # 让返回的对象信息更具体,而不再是:<__main__.Student object at 0x109afb190>
    def __str__(self):
        return 'Std object(name is: %s)' % self.name

    # 动态返回一个属性,注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
        if attr == 'age':
            return lambda: 25


s = Std("kevin")


# print(s.abc)
# print(s.score)
# print(s)

# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
# 斐波那契数列示例
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self  # 实例本身为迭代对象,即返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration("超过了100")
        return self.a

    # 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


def fib_demo():
    global n
    for n in Fib():
        print(n)


# fib_demo()

def fib_list_deom():
    f = Fib()
    print(f[0])
    print(f[3])


# fib_list_deom()

# 通过 __getattr__ 动态调整属性的作用:可以针对完全动态的情况作调用
"""
例子:如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改,
利用完全动态的__getattr__，我们可以写出一个链式调用,这样，无论API怎么变，
SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
"""


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    # 链式调用
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    # 通过 __call__ 直接对实例进行调用
    def __call__(self, path):
        return Chain('%s/%s' % (self._path, path))

    __repr__ = __str__


def def_and_call_obj():
    print(Chain().status.user.list)
    # 如果要把参数放入,如:GET /users/:user/repos,调用时，需要把:user替换为实际用户名,如下:
    print(Chain().users("kevin").repos)
    # 直接对实例对象进行调用(通过__call__方法)
    chain = Chain()
    print(chain('hello'))


# def_and_call_obj()


class StudentCall(object):
    def __init__(self, name=''):
        self.name = name

    # 对实例直接进行调用
    def __call__(self):
        print('My name is %s.' % self.name)


# s = StudentCall('kevin')
# s()


# 如何判断变量是对象还是函数,需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象

def is_callable():
    print(callable(StudentCall()))
    print(callable(max))
    print(callable('str'))


# is_callable()


# =================================================
# 使用枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


# print(Month.Jan)
def enum_all():
    global name
    # 枚举它的所有成员：
    for name, member in Month.__members__.items():
        print('name:', name, 'member:', member)


# enum_all()

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
@unique  # @unique装饰器可以帮助我们检查保证没有重复值。
class WeekDay(Enum):
    Mon = 1
    Tue = 2
    Wez = 3
    Thu = 4
    Fri = 5
    Sat = 6
    Sun = 7


# 以多种方式访问枚举
def access_enum():
    mon = WeekDay.Mon
    print(mon)
    print(WeekDay['Mon'])
    print(WeekDay(1))
    print(WeekDay.Mon.value)
    print(WeekDay.Mon == mon)
    # print(WeekDay(8)) # ValueError


# access_enum()


# =================================================
# 使用元类
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的


class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)


# h = Hello()
# print(type(h))

# type()函数既可以判断并返回一个对象的类型，又可以创建出新的类型 todo

def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


# 通过type()函数创建出Hello1类，而无需通过class Hello1(object)...的定义：
Hello1 = type('Hello1', (object,), dict(hello=fn))  # 创建Hello class
h = Hello1()
h.hello()



