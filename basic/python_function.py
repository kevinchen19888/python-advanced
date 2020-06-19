# ===============================================
# python 函数使用示例
def printme(list, str):
    list.append(str)
    # print(list)
    return list


printme(str="dene", list=["kevin", "lucy"])  # 关键字参数使用示例


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
    sum = lambda a, b: a + b
    print(sum)
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


variable_test(10, 20)
print(overall_a)
