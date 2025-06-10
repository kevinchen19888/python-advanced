"""
继承和多态
"""


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def sleep(self):
        print(f'{self.name} is sleeping')


"""
继承的类,在类名后的圆括号中指定当前类的父类
Student(Person)
"""
class Student(Person):
    def __init__(self, age:int, name:str):
        # 通过super().__init__()来调用父类初始化方法
        super().__init__(age, name)

    def study(self):
        print(f'{self.name} is studying')


class Teacher(Person):
    def __init__(self, age, name, school):
        super().__init__(age, name)
        self.school = school

    def teach(self):
        print(f'{self.name} is teaching')
    def sleep(self):
        print(f'teacher:{self.name} is sleeping')

class Male(Person):
    def __init__(self, age, name):
        super().__init__(age, name)
    def sex(self):
        print(f'{self.name}is male')

"""
多重继承
"""
class MaleTeacher(Male, Teacher):
    def __init__(self, age, name, school):
        super().__init__(age, name)
        self.school = school
    def sex(self):
        print(f'{self.name} is male teacher')

def to_exec():
    student = Student(18, 'kevin')
    # 继承
    student.sleep()
    teacher = Teacher(18, 'James', 'HIT')
    # 多态(重新实现父类方法)
    teacher.sleep()


# to_exec()
