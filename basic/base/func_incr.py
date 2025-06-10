"""
高阶函数:
把一个函数作为其他函数的参数或返回值的用法，我们通常称之为“高阶函数”
"""
import functools


def calc(init_val,op_func,*args,**kwargs):
    items = list(args) + list(kwargs.values())
    res = init_val
    for item in items:
        if type(item) in (int ,float):
            res = op_func(res,item)
    return  res

def add(a,b):
    return a + b

def mul(a,b):
    return a * b

# 把函数作为参数时只需要函数名即可

# print(calc(0, add, 1, 2, 3, age=4))
# print(calc(1, mul, 1, 2, 3, age=4))


# old_strings = ['in', 'apple', 'zoo', 'waxberry', 'pear']
# new_strings = sorted(old_strings, key=len)
# print(new_strings)  # ['in', 'zoo', 'pear', 'apple', 'waxberry']

"""
lambda 表达式使用
"""


def func_lambda_demo():
    old_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, old_nums))))
    print(list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, old_nums))))


# func_lambda_demo()

"""
偏函数是指固定函数的某些参数，生成一个新的函数，这样就无需在每次调用函数时都传递相同的参数。
在 Python 语言中，我们可以使用functools模块的partial函数来创建偏函数
"""

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
print(int2('1010'))
print(int8('1'))

