# 代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义


# 定义装饰器
import functools


def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log
def decorator_demo():
    print('now...')


# decorator_demo()


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log(text):
    def deco(func):
        @functools.wraps(func)  # 将原始函数的__name__等属性复制到wrapper()函数中
        def wrapper(*args, **kwargs):
            print('%s,func is %s():' % (text, func.__name__))
            rv = func(*args, **kwargs)
            print('函数执行之后执行')
            return rv

        return wrapper

    return deco


l = log('exec log')

text_deco_demo = l(lambda: print('execute text_deco..'))

text_deco_demo()
# @l
# def text_deco_demo():
#     print('execute text_deco..')
#
# lambda : print('execute text_deco..')
# text_deco_demo()
# now = log('execute')(text_deco_demo)
# print(now.__name__)
