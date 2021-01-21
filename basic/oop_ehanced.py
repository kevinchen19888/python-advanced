# 面向对象高阶部分


# 使用__slots__

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


s = Std("kevin")


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


