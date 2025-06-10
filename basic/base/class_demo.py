"""
使用'__'声明一个私有属性,使用'_'声明一个受保护属性
"""

class Std:
    # name = 'kevin'
    """
    对象初始化方法
    """
    def __init__(self,  name):
        self.name = name
    def get_name(self):
        return self.name
    """
    对象属性设置方法
    :param name:
    """
    def set_name(self, name):
        self.name = name


def run_student():
    s1 = Std('kevin')
    # 调用对象方法的两种方式
    # print(s1.get_name())
    # print(Student.get_name(s1))
    s1.set_name('James')
    print(s1.get_name())
    # 获取对象的内存地址
    # print(hex(id(s1)))


# run_student()

class Point:
    # 限制为对象动态添加属性
    __slots__=('__x','y')
    def __init__(self, x, y):
        """
        构造方法
        :param x:
        :param y:
        """
        self.__x = x
        self.y = y

    def distance(self):
        return (self.__x ** 2 + self.y ** 2) ** 0.5
    def __str__(self):
        print(f'{self.__x=},{self.y=}')


def exec_point():
    p = Point(3, 4)
    # print(p.distance())
    # 为对象动态添加属性
    # p.sex = 'male'
    p.__str__()

# exec_point()


"""
静态方法/类方法使用示例
对象方法、类方法、静态方法都可以通过“类名.方法名”的方式来调用，区别在于方法的第一个参数到底是普通对象还是类对象，还是没有接受消息的对象
"""
class Triangle(object):
    """三角形"""
    def __init__(self,x,y,z):
        self.__x=x
        self.__y=y
        self.__z=z

    """
    静态方法:独立使用
    """
    @staticmethod
    def is_valid(x, y, z):
        return x + y > z and y + z > x and z + x > y

    """
    类方法:需要访问类属性或实现工厂方法时使用
    """
    @classmethod
    def is_valid2(cls, x, y, z):
        return x + y > z and y + z > x and z + x > y

    def get_area(self):
        half = (self.__x + self.__y + self.__z) / 2
        return (half * (half - self.__x) * (half - self.__y) * (half - self.__z)) ** 0.5

    """
    使方法变成类的一个属性
    """
    @property
    def area(self):
        half = (self.__x + self.__y + self.__z) / 2
        return (half * (half - self.__x) * (half - self.__y) * (half - self.__z)) ** 0.5
def exec_triangle():
    print(Triangle.is_valid(3, 4, 5))
    print(Triangle.is_valid2(3, 4, 5))
    t = Triangle(3, 4, 5)
    # 通过类名调用对象方法
    print(Triangle.get_area(t))
    print(t.area)

# exec_triangle()