"""
集合
@:keyword 集合中元素必须是hashtable类型
"""


def set_demo1():
    # s=set([1,2,3,3])
    s = {1, 2, 3}
    print(type(s))
    print(s)
    # 集合生成式
    set2 = {n for n in range(1, 10) if n % 3 == 0 or n % 5 == 0}
    print(set2)


# set_demo1()

"""
set 遍历
"""

def set_demo2():
    set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
    for s in set1:
        print(s)

# set_demo2()

"""
集合运算
"""
def set_demo3():
    set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
    print('Swift' in set1)
    # print('Swift' not in set1)
    set2 = {'Python', 'Kotlin', 'Swift', 'C#'}
    # 交集
    print(set1 & set2)
    print(set1.intersection(set2))
    # 并集
    print(set1 | set2)
    print(set1.union(set2))
    # 差集
    print(set1 - set2)
    print(set1.difference(set2))
    # 对称差
    print(set1 ^ set2)
    print(set1.symmetric_difference(set2))

# set_demo3()

"""
集合的方法
"""
def set_demo4():
    set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
    # 添加
    set1.add('C#')
    print(set1)
    # 删除
    set1.remove('C#')
    set1.discard('C++')
    print(set1)
    # 清空
    set1.clear()
    print(set1)
    set2 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
    # 判断两个集合是否没有元素相同
    print(set1.isdisjoint(set2))  # False


# set_demo4()
