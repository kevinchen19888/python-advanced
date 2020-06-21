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


emp1 = Employee("kevin", 100)
# emp2 = Employee("kevin", 100)
# print(emp1.salary)
print(getattr(emp1, 'name'))
setattr(emp1, 'name', "james")  # 设置对象属性值
print(getattr(emp1, 'name'))  # 获取对象属性值


# print(emp1.__dict__)  # 类的所有属性与值得字典
# print(emp1.__doc__)  # 类的文档字符串
# print(Employee.__name__)
# print(Employee.__module__)


# print(emp1.empCount)

class ClassTest:
    def prt(self):
        print(self)
        print(ClassTest.__class__)

# ============================
# 对象回收
