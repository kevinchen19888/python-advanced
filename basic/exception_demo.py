"""异常处理示例"""
import logging


def exception_demo():
    try:
        fh = open("io.txt", "r")
        try:
            readline = fh.readline()
        finally:
            print('关闭文件')
            fh.write("")  # 此处出错会被外面的except捕捉
            # fh.close()
    # except: # 会捕获所有异常
    except (IOError, SyntaxError):
        print('error:没有找到对应文件或文件夹')
    # except BaseException:  # 所有异常的基类
    #     print("获取所有异常")
    else:  # 如果没有出现异常
        fh.close()
        print(fh.closed)
    finally:
        print('finally最终都会执行')


# exception_demo()

# ========================================
def exception_int_convert(var):
    try:
        return int(var)
    except ValueError:
        print("参数没有包含数字:", var)


# exception_int_convert("string")


# ======================== 自主出发异常
def raise_exception(var):
    try:
        if var < 2:
            raise (NameError, "命名错误")
    except Exception:
        print("命名错误捕捉")
    return


# raise_exception(1)

# 自定义异常
# ======================================
class DefinedException(RuntimeError):
    def __init__(self, args):
        self.args = args


def defined_exception():
    try:
        raise DefinedException("自定义异常")
    except DefinedException:
        print("自定义异常")


# defined_exception()
# print(sum([1, 2, 3]))


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        pass
        # print('Error:', e)
        logging.exception(e)
    finally:
        print('finally...')


# main()
# print('END')


def fib(max_val):
    n, a, b = 0, 0, 1
    while n <= max_val:
        a, b = b, a + b
        n = n + 1
    return a


def cache(f):
    _cache = {}

    def wrapper(n):
        if n in _cache:
            return _cache[n]
        _cache[n] = f(n)
        return _cache[n]

    return wrapper


@cache
def f(n):
    return 1 if n < 3 else f(n - 1) + f(n - 2)


def fib_impl():
    print([f(n) for n in range(1000)])
    print([cache(lambda n: 1 if n < 3 else f(n - 1) + f(n - 2))(n) for n in range(1000)])
    print(fib(20))
    print({i: fib(x) for i, x in enumerate(range(20))})


# fib_impl()


# err_raise.py
class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


# bar()

# ======================================
# 使用断言(如果条件不符合,会抛出对应的错误信息
# 启动Python解释器时可以用-O参数来关闭assert,关闭后，可以把所有的assert语句当成pass来看

logging.basicConfig(level=logging.INFO)  # 指定log级别


def to_assert(n):
    nn = int(n)
    # logging.warning('info %s', 'args')
    logging.info('info log...')
    assert nn != 0, 'n is 0'  # 条件不满足,会抛出AssertionError
    return 10 / n


# to_assert(10)
