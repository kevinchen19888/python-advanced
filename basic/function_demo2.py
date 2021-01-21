import math

# 函数导入demo
# from_demo("hello")

# 默认参数demo
from functools import reduce


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


# 计算x的n次方
def couple(x, n):
    a = 1
    while n > 0:
        a = a * x
        n = n - 1
    return a


def add_end(L=[]):
    """多次调用后 L 添加进每次添加'END'"""
    L.append('END')
    return L


# print(add_end([1, 2, 3]))
# print(add_end())
# print(add_end())
#  定义默认参数要牢记一点：默认参数必须指向不变对象！

# =========================================
# 可变参数函数
def calc(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum


# print(calc(1, 2, 3))
list = [1, 2, 3]


# print(calc(*list))

# ============================================
# 关键字参数
def key_params(age, name, **kwargs):
    print("age:", age, "name:", name, "other:", kwargs)
    # print(kwargs['city'])


dic = {'city': 'beijing'}


# key_params(10, "kevin", **dic)
# key_params(20, "kevin", city="beijing")


# =============================================
# 命名关键字参数:限制关键字参数的名字
def limit_key_paras(age, name, *, city, job):
    print("age:", age, "name:", name, city, job)


# limit_key_paras(10, "kevin", city='bj', job='program')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def limit_key_paras2(name, age, *args, city, job):
    print(name, age, args, city, job)


# ===========================================

# 各种参数类型组合使用:
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b=0, *args, **kwargs):
    print(a, b, args, kwargs)


# f1(1, 100, {'key': "val"}, 'kw', city='bj')


# ==========================================
# 函数递归
def recursion(n):
    if n < 1:
        return 1
    return n * recursion(n - 1)


# print(recursion(997))


# ==========================================
# list 和 tuple 的切片
def partition_demo():
    list = [1, 2, 3]
    print("list pt 0~2:", list[0:2])
    print("list pt 1~last:", list[0:])
    tup = tuple(list)
    print("tup pt last~last-2:", tup[-2:])
    return None


# partition_demo()

# ===========================================
# 通过 enumerate 函数对list实现类似Java那样的下标循环

def enumerate_demo():
    for i, value in enumerate(['A', 'B', 'C']):
        print('key:', i, "val:", value)


# enumerate_demo()

# ===========================================
# 列表生成式
def list_gen(list):
    for i in range(1, 11):
        list.append(i)
    return list


# print(list_gen([]))

# 通过列表生成式，可以写出非常简洁的代码
def list_gen2():
    print([x + 1 for x in range(1, 11)])
    print([x + x for x in range(1, 10) if x % 2 == 0])
    print([x + y for x in 'ABC' for y in 'abc'])


# list_gen2()


# 斐波那契数列
# ===========================================
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        a, b = b, a + b
        print(a)
        n = n + 1
    return 'done'


# fib(6)


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
# 变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

    # for i in fib2(6):
    #     print(i)


# ===========================================
# 可以使用isinstance()判断一个对象是否是Iterator对象：

from collections.abc import Iterator


def is_iterator(it):
    print(isinstance(it, Iterator))


# is_iterator((i for i in range(10)))
# Iterable 转 Iterator
# print('is Iterator:', isinstance(iter([1, 2]), Iterator))

# ===========================================
# 高阶函数 map/reduce
def f_map(x):
    return x * x


def map_demo():
    """
    map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，
    并把结果作为新的Iterator返回
    """
    iterator = map(f_map, [1, 2, 3, 4])
    for i in iterator:
        print(i)


# map_demo()

def add_demo(x, y):
    return x + y


def reduce_demo(it):
    """
    reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
    """
    return reduce(add_demo, it)


# print(reduce_demo([1, 2, 3, 4]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


# lambda函数 使用
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# print(str2int(['1', '5']))


# Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(x):
    return x % 2 != 0


def filter_demo():
    for i in filter(is_odd, [1, 2, 3, 4]):
        print(i)


# filter_demo()


# ===========================================
# 使用 sorted()函数 对list进行排序
# 还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序

def sorted_demo():
    l = [36, 5, -12, 9, -21]
    print(sorted(l))
    print(sorted(l, key=abs))
    print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


# sorted_demo()


# ===========================================
# 返回函数:将函数作为结果进行返回

def lazy_sum(*args):
    def sum_():
        su = 0
        for i in args:
            su = su + i
        return su

    return sum_


# fuc = lazy_sum(1, 2, 3)
# print(fuc())

# 闭包
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


def closure_demo():
    f1, f2, f3 = count()
    print(f1())
    print(f2())
    print(f3())


# closure_demo()


# 执行结果全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# todo 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。


# ===========================================
# 匿名函数

def anonymity_fuc(li):
    it = map(lambda x: x * x, li)
    for i in it:
        print(i)


# anonymity_fuc([1, 2, 3])
