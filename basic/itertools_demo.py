# itertools:Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。

import itertools


def itertools_count():
    t = itertools.count(1)
    for i in t:
        print(i)
        if i > 100:
            break


# itertools_count()

# cycle()方法会把传入的一个序列无限重复下去：
def itertools_repeat():
    re = itertools.repeat('kevin', 10)
    for r in re:
        print(r)


# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
# itertools_repeat()


# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：

def chain_use():
    for s in itertools.chain('ABC', 'def'):
        print(s)


# chain_use()


# groupby()把迭代器中相邻的重复元素挑出来放在一起：

def groupby_use():
    for k, g in itertools.groupby('aaabbbbcccc'):
        print("k:%s,g:%s" % (k, list(g)))


# groupby_use()



