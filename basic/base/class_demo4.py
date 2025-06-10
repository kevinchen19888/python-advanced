"""
工资结算
"""
from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    """
    抽象类
    """

    def __init__(self, name):
        self.name = name

    """
    抽象方法需要子类实现
    """

    @abstractmethod
    def get_salary(self):
        """结算月薪"""
        pass


class Manager(Employee):
    """
    继承抽象类
    """

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """
    继承抽象类
    """

    def __init__(self, name, work_hour=0):
        super().__init__(name)
        self.work_hour = work_hour

    def get_salary(self):
        if self.work_hour > 40:
            return 40 * 150 + (self.work_hour - 40) * 200
        else:
            return self.work_hour * 150


class Salesman(Employee):
    """
    继承抽象类
    """

    def __init__(self, name, sales):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return self.sales * 0.1 + 2000


def main():
    emps = [
        Manager('Bob'),
        Programmer('Jim'),
        Salesman('Tom', 5000),
        Programmer('Lily', 100),
        Salesman('Tom', 5000),
        Programmer('Lily', 100),
        Programmer('Lily', 100),
    ]
    total = sum([emp.get_salary() for emp in emps])
    print('公司总月薪为：%d' % total)

main()