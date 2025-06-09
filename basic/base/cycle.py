"""
循环结构demo
"""
import time

def for_demo():
    for i in range(1,10,2):
        print("i=", i)
        time.sleep(1)

# for_demo()

def for_demo2():
    total = 0
    for i in range(1, 10):
        if i % 2 == 0:
            continue
        total += i
    print(total)

# for_demo2()
# print(sum(range(2, 101, 2)))

def while_demo():
    total = 0
    i = 1
    while i<=100:
        total += i
        i+=1
        # if i==50:
        #     break
    print(total)

# while_demo()

"""
循环嵌套demo:
九九乘法表
"""
def for_nest_demo():
    for i in range(1,10):
        for j in range(1,i+1):
            print(f'{j}*{i}={j*i}\t', end='')
        print()

# for_nest_demo()

"""
求最大公约数
"""

def max_common_divisor():
    a = int(input('a='))
    b = int(input('b='))
    for i in range(a, 0, -1):
        if a % i == 0 & b % i == 0:
            print("最大公约数为:", i)
            break

# max_common_divisor()

def feibonaqie():
    a, b = 0, 1
    for _ in range(10):
        a, b = b, a + b
        print(a)
# feibonaqie()

"""
水仙花数
"""
def daffodil_num():
    for i in range(100,1000):
        low = i % 10
        mid = i // 10 % 10
        high = i // 100
        if i == low ** 3 + mid ** 3 + high ** 3:
            print(f'水仙花数为:{i}')

# daffodil_num()
