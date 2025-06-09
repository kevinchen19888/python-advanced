"""
元组
元组和列表的不同之处在于，元组是不可变类型
"""
def tuple_demo():
    t1 = (1, 2, 3, 4, 5)
    print(type(t1))
    # 查看元组长度
    print("t1 length is:", len(t1))
    # 索引
    print("t1[2] is:", t1[2])
    # 切片
    # print("t1[1:3] is:", t1[1:3])
    # 遍历
    # for i in t1:
    #     print(i)
    # 拼接
    t2 = (6, 7, 8)
    print("t1 + t2 is:", t1 + t2)
    # 如果元组中只有一个元素，需要加上一个逗号，否则()就不是代表元组的字面量语法
    t3 = (9,)
    print(type(t3))

# tuple_demo()

"""
打包和解包
"""
def  tuple_demo2():
    # 打包操作
    a = 1, 10, 100
    # print(type(a))  # <class 'tuple'>
    # print(a)  # (1, 10, 100)
    # 解包操作
    i, j, k = a
    # print(i, j, k)  # 1 10 100
    # 通过星号表达式，我们可以让一个变量接收多个值
    d,*e = a
    print(type(e))
    print(e)

# tuple_demo2()


def tuple_demo3():
    a = 1
    b = 10
    # 交互变量的值
    a, b = b, a
    print(a, b)


# tuple_demo3()

"""
元组与列表的比较：
1.元组为不可变类型，更适合多线程环境
2.不可变类型在创建时间上优于对应的可变类型
"""
import timeit
def tuple_demo4():
    print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
    print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

# tuple_demo4()

def tuple_demo5():
    l =  [1, 2, 3, 4, "5", 6, 7, 8, 9]
    # 将列表转换成元组
    print(tuple(l))
    tup = (1,2,3,4,5)
    # 将元组转换成列表
    print(list(tup))

# tuple_demo5()