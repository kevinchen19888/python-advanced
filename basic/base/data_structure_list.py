"""
常用数据结构
"""


# item1 = [100,'Python']
# print(item1)
# print(type( item1))
# print(list(range(1,10)))

def list_demo():
    list1 = [1, 2, 3]
    list2 = [3, 4, 5, 6]
    # 使用+拼接两个 列表
    print(list1 + list2)
    # *  列表复制
    # print(list1 * 2)
    #  判断元素是否在列表中
    print(3 in list1)
    print(f'第一个元素为：{list1[0]}, 最后一个元素为：{list1[-1]}')
    # 切片
    print(list2[1:3:2], list2[::2])
    # 列表比较,比较第一个元素
    print(list1 >= list2)

# list_demo()


import random


def roll_dice():
    counters = [0] * 6
    # 模拟掷色子记录每种点数出现的次数
    for _ in range(6000):
        face = random.randrange(1, 7)
        counters[face - 1] += 1
    # 输出每种点数出现的次数
    for face in range(1, 7):
        print(f'{face}点出现了{counters[face - 1]}次')


# roll_dice()

"""
list 的常规操作方法
"""
def list_demo2():
    llist1 = list(range(1, 3))
    llist1.insert(0, 10)
    print(llist1)
    list2 = list(range(1, 3))
    list2.append(10)
    print(list2)
    # 删除
    list2.pop()
    print(list2)
    #  删除指定元素
    list2.remove(1)
    print(list2)
    # 清空
    list2.clear()
    print(list2)
    # 删除指定索引的元素
    items = ['Python', 'Java', 'C++']
    del items[1]
    print(items)  # ['Python', 'C++']


# list_demo2()


"""
list 的元素位置和频次
"""
def list_demo3():
    items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
    print(items.index('Python'))  # 0
    # 从索引位置1开始查找'Python'
    print(items.index('Python', 1))  # 5
    print(items.count('Python'))  # 2
    print(items.count('Kotlin'))  # 1
    print(items.count('Swfit'))  # 0
    # 从索引位置3开始查找'Java'
    # print(items.index('Java', 3))  # ValueError: 'Java' is not in list


# list_demo3()

"""
元素排序和反转
"""
def list_demo4():
    items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
    items.sort()
    print(items)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
    items.reverse()
    print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']

# list_demo4()

"""
列表生成式
优点：可以更简洁生成想要的列表
"""
def list_gen():
    items = [x * x for x in range(1, 11) if x % 2 == 0]
    print(items)
    items = [m + n for m in 'ABC' for n in 'XYZ']
    print(items)
    items = ['Hello', 'World', 'IBM', 'Apple']
    items_upper = [item.upper() for item in items]
    print(items_upper)

# list_gen()

import random


"""
双色球随机选号程序
"""
import random


def selected_balls_demo():
    red_balls = [i for i in range(1, 34)]
    blue_balls = [i for i in range(1, 17)]
    # 从红色球列表中随机抽出6个红色球（无放回抽样）
    selected_balls = random.sample(red_balls, 6)
    # 对选中的红色球排序
    selected_balls.sort()
    # 输出选中的红色球
    for ball in selected_balls:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    # 从蓝色球列表中随机抽出1个蓝色球
    blue_ball = random.choice(blue_balls)
    # 输出选中的蓝色球
    print(f'\033[034m{blue_ball:0>2d}\033[0m')


# selected_balls_demo()



