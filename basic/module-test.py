# Python 模块(Module)，是一个 以.py为扩展名的Python 文件,包含了 Python 对象定义和Python语句
# 导入模块
import module_demo
import sys

# 导入模块的部分 from...import

# from module_demo import sum_number

print(module_demo.sum_number(1, 2, 7))

# module_demo._private_func_demo() # 不建议访问一个作用域为受保护的函数
