"""类的创建与使用"""


class Employee:
    """员工基类"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        print("Employee初始化")

    def emp_count(self):
        print("员工数量:", Employee.empCount)

    def emp_salary(self):
        print("薪水:", self.salary)


# emp1 = Employee("kevin", 100)
# emp2 = Employee("kevin", 100)
# print(emp1.salary)
# print(getattr(emp1, 'name'))
# setattr(emp1, 'name', "james")  # 设置对象属性值
# print(getattr(emp1, 'name'))  # 获取对象属性值


# print(emp1.__dict__)  # 类的所有属性与值得字典
# print(emp1.__doc__)  # 类的文档字符串
# print(Employee.__name__)
# print(Employee.__module__)


# print(emp1.empCount)

class ClassTest:
    def prt(self):
        print(self)
        print(ClassTest.__class__)

    def __del__(self):  # 对象被销毁时执行
        class_name = self.__class__.__name__
        print("对象将被销毁,对象类型:", class_name)


# ============================
# 对象回收
# test = ClassTest()


# del test  #
# 销毁对象
# print(test)
# print(id(test))  # 对象id

# ============================
# Python 子类继承父类构造函数说明
class Father:
    def __init__(self, name):
        self.name = name
        print("Father __init__:", self.name)

    def get_name(self):
        print("Father_getName")
        return self.name


class Mother(object):
    # 私有属性,以"__"开头
    __mo_private_attr = 0

    def __init__(self, name):
        self.name = name
        print("Mother create")

    def get_mother_name(self):
        self.__mo_private_method()
        return self.name

    # 私有方法,以"__"开头
    def __mo_private_method(self):
        print("mo_private_method")

    # 受保护方法,只能被基类和子类访问
    def _protected_method(self):
        print("_protected_method")

    def count(self):
        self.__mo_private_attr += 1
        print(self.__mo_private_attr)


class Son(Father, Mother):
    def __init__(self, name):
        # super(Son, self).__init__(name) # 调用父类构造方法
        Father.__init__(self, name)  # 调用父类构造的另一种写法
        print("Son create")
        self.name = name

        def get_name(self):
            print("Son_getName")
            Mother._protected_method(self)
            return self.name


# if __name__ == '__main__':
#     son = Son('hello')
#     #     son.get_name()
#     print(son.get_mother_name())
#     son.count()


# 子类不重写 __init__，实例化子类时，会自动调用父类定义的 __init__
# 如果重写了__init__ 时，实例化子类，就不会调用父类已经定义的 __init__

# ====================私有属性&方法demo
son = Son('hello')
print(son.get_mother_name())
son.count()
son.get_name()


# ====================运算符重载demo
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

# v1 = Vector(2, 10)
# v2 = Vector(5, -2)
# print(v1 + v2)
# print(v1.__str__())
