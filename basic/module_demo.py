# Python 模块(Module)，是一个 以.py为扩展名的Python 文件,包含了 Python 对象定义和Python语句
import math


def sum_number(*args):
    sum = 0
    for i in args:
        sum += i
    print(globals())
    return sum


print(sum_number(1, 2, 11))
