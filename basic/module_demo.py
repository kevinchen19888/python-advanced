# Python 模块(Module)，是一个 以.py为扩展名的Python 文件,包含了 Python 对象定义和Python语句 //模块的文档注释
import math


def sum_number(*args):
    sum = 0
    for i in args:
        sum += i
    # print(globals())
    return sum


# print(sum_number(1, 2, 11))

# ==========================================
# Python中，是通过_前缀来实现模块中函数和变量的作用域

# 受保护函数
def _private_func_demo():
    print('this is private func')


# 私有函数
def __private_func_demo2():
    print('this is private func2')


print(_private_func_demo())
