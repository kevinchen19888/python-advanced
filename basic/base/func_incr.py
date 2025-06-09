"""
高阶函数:
把一个函数作为其他函数的参数或返回值的用法，我们通常称之为“高阶函数”
"""

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


# print(calc(0, add, 1, 2, 3, age=4))
# print(calc(1, mul, 1, 2, 3, age=4))

