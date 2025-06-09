"""
求阶乘
"""
def fac(n):
    res = 1
    for i in range(2,n+1):
        res*=i
    return res

# print(fac(5))

# from math import factorial as fact
# print(fact(5))

"""
函数传参可以使用两种形式:
1.位置参数
2.关键字参数
"""
def calc(a, b, c):
    return a + b + c


# print(calc(1,2,3))
# 可以在参数列表中用/设置强制位置参数,Python 3.8 引入的新特性
def calc2(a, b, c, /):
    print(a, b, c)

# print(calc(b=1, a=2, c=3))

"""
命名关键字参数:
命名关键字参数只能通过“参数名=参数值”的方式来传递和接收参数
"""
def func_demo4(*,a,b,c):
    print(a,b,c)

# func_demo4(1,2,3) # 报错:TypeError
# func_demo4(a=1,b=2,c=3)

def func_demo5(a,b,c,*,d,e):
    print(a,b,c,d,e)

# func_demo5(1,2,3,d=4,e=5)
# func_demo5(1,2,3,4,5) # 报错:TypeError

"""
函数默认值,定义时设置
todo:带默认值的参数必须放在不带默认值的参数之后
"""
def func_demo6(a,b,c=3):
    print(a,b,c)

# func_demo6(1,2)

"""
可变参数
参数会被组装成元组
"""
def func_demo7(*args):
    print(args)

# func_demo7(1,2,3)
def func_demo8(*args):
    total = 0
    for i in args:
        if type(i) in (int,float):
            total += i
        else:
            print("参数类型错误")
    print( total)

# func_demo8(1,2,3,'4')

"""
可变关键字参数
"""
def func_demo9(*args,**kwargs):
    print(f'可变参数：{args},\t可变关键字参数：{kwargs}')

# func_demo9(1,2,3,a=1,b=2)


"""
from...import...语法从模块中直接导入需要使用的函数
"""
from func2 import fac
print(fac(5))