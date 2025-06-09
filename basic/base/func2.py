
""""
Python 中每个文件就代表了一个模块（module），我们在不同的模块中可以有同名的函数，在使用函数的时候，
通过import关键字导入指定的模块再使用完全限定名（模块名.函数名）的调用方式，就可以区分到底要使用的是哪个模块中函数
"""
import string
import random


def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)


# print(fac(5))

# 使用func中函数
# import func

# print(func.fac(5))

# Python 标准库中还有一类函数是不需要import就能够直接使用的，我们将其称之为内置函数

# print(abs(-1))



def gen_code(*,code_len):
    return ''.join(random.choices(string.digits + string.ascii_letters, k=code_len))


# random.sample 实现无放回抽样,choices 实现放回抽样
# print(random.sample(string.digits + string.ascii_letters, 4))
# print(gen_code(code_len=4))


def is_prime(num: int) -> bool:
    """
    判断一个正整数是不是质数
    :param num: 大于1的正整数
    :return: 如果num是质数返回True，否则返回False
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# print(is_prime(11))