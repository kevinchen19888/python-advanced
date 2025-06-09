# 使用 pdb(python调试器)进行调试
"""
1.使用 python -m pdb err.py 启动
2.以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：
3.输入命令n可以单步执行代码：
4.任何时候都可以输入命令p 变量名来查看变量：
5.输入命令q结束调试，退出程序：
"""
# err.py
import pdb

s = '0'
n = int(s)


# pdb.set_trace()  # 运行到这里会自动暂停
# print(10 / n)


def condition_demo(a):
    if a > 0:
        print("a val is:", a)
    elif a == 0:
        print("a val is 0")
    else:
        print("a is less than 0")


# condition_demo(2)

def for_demo():
    lis1 = [1, 2, 3]
    for i, val in enumerate(lis1):
        print(i, val)


# for_demo()
