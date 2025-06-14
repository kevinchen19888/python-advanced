# ===============================================
# python 函数使用示例
import functools


def printme(list, str):
    list.append(str)
    print(list)
    return list


# printme(str="dene", list=["kevin", "lucy"])  # 关键字参数使用示例


# 默认参数//调用函数时，默认参数的值如果没有传入，则被认为是默认值
def print_info(name, age=10):
    print(name)
    print(age)
    return


# print_info(name="lucy")
# print_info(age=22, name="lucy")

# ==============================================
# 不定长参数
def variable_args(arg1, *args):
    """打印所有未定义的参数"""
    for a in args:
        print(a)
    return


# variable_args(10, 20, 30)


# =============================================
# 匿名函数//lambda 的主体是一个表达式，而不是一个代码块
# lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。

def lambda_sum():
    sum2 = lambda a, b: a + b
    print(sum2(2,3))
    return


# lambda_sum()

# ============================================
# 变量作用域//定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
overall_a = 0


def variable_test(a, b):
    # 全局变量赋值
    # global overall_a
    overall_a = a * b
    print(overall_a)
    return


# variable_test(10, 20)
# print(overall_a)

# ============================================
# 使用偏函数:设定参数的默认值，降低函数调用的难度

# 对 int 函数 base参数设置默认值
int2 = functools.partial(int, base=2)
# print(int2('100'))

def print_demo(a):
    print(a)

# a=10
# b='11'
# print(str(a))
# print(float(a))
# print(int(b,base=2))
# print(True and False)
#
# print(321 ** 12)    # 求幂运算，输出1196906950228928915420617322241
#
# print(c:=20)
# print(1<2 or 2>3)

"""
将华氏温度转换为摄氏温度
"""
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))
print(f'{f:.1f}华氏= {c=:.1f}摄氏度')
print('%.1f 华氏=%.1f 摄氏度' % (f, c))

