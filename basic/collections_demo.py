# collections


# namedtuple (快速创建自定义的元组对象)
import argparse
import os
import unittest
from collections import namedtuple
import random


def namedtuple_use():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print(p.x)
    # 验证对象是否为 tuple子类
    print(isinstance(p, tuple))


# namedtuple_use()

# deque:为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

from collections import deque


def deque_use():
    d = deque([1, 2, 3])
    d.append(5)
    d.appendleft(0)
    print(d)
    d.pop()
    print(d)
    d.popleft()
    print(d)


# deque_use()

# defaultdict:使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。

from collections import defaultdict, OrderedDict


def defaultdict_use():
    d = defaultdict(lambda: 'N/A')
    d['key1'] = 'val1'
    print(d['key1'])
    print(d['key2'])  # 返回默认值


# defaultdict_use()


# OrderedDict:使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict,其实现了一个FIFO的dict
# =========================================

def order_dict_use():
    d = dict([('a', 1), ('b', 2), ('c', 3)])
    for _ in range(10):
        print(d)
    od = OrderedDict([('ac', 1), ('ba', 2), ('bc', 3)])


# order_dict_use()


# =============================================

from collections import ChainMap


def chainmap_use():
    # 缺省参数
    default_args = {'color': 'red', 'user': 'guest'}
    # 构造命令行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user')
    parser.add_argument('-c', '--color')
    namespace = parser.parse_args()
    # 字典推导式
    cml = {k: v for k, v in vars(namespace).items() if v}
    combined = ChainMap(cml, os.environ, default_args)
    print('color=%s' % combined['color'])
    print('user=%s' % combined['user'])


# chainmap_use()


# ================================================
# Counter:是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter


def counter_use():
    global c
    c = Counter()
    for cs in 'programing':
        c[cs] = c[cs] + 1
    print(c)
    c.update('hello')
    print(c)


# counter_use()


class BaseTest(unittest.TestCase):

    def test_chain_map(self):
        chainmap_use()
