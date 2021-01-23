# 文档测试

# 自动执行写在注释中的这些代码


def abs(n):
    """
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    """
    return n if n >= 0 else (-n)


# Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。


# mydict2.py
class Dict(dict):
    """
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    """

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


# 什么输出也没有。这说明我们编写的doctest运行都是正确的,如果程序有问题，比如把__getattr__()方法注释掉，再运行就会报错
if __name__ == '__main__':
    import doctest

    doctest.testmod()

# 小结:
# doctest非常有用，不但可以用来测试，还可以直接作为示例代码。通过某些文档生成工具，
# 就可以自动把包含doctest的注释提取出来。用户看文档的时候，同时也看到了doctest。
