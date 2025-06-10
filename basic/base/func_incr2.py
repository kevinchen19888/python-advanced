"""
装饰器是一个高阶函数，它的参数和返回值都是函数
"""
import random
import time
from functools import wraps, lru_cache


def record_time(func):
    """
    装饰器函数
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        start_time = time.time()
        resp = func(*args,**kwargs)
        end_time = time.time()
        print("函数%s执行时间：%s" % (func.__name__, end_time - start_time))
        return resp
    return wrapper


@record_time # 语法糖
def upload(file_name):
    print("上传文件%s" % file_name)
    time.sleep(random.random()*3)
    print("上传成功")

# 直接调用方式
# upload = record_time(upload)
# upload("test.txt")

# 使用语法糖
# upload('hello')

# 使用 @wraps 去掉装饰器作用,只执行原函数
# upload.__wrapped__('Python从新手到大师.pdf')


@lru_cache # 缓存执行结果,提升性能
def fei(n) -> int:
    if n in (1, 2):
        return 1
    return fei(n-1) + fei(n - 2)

for i in range(1,21):
    print(fei(i))

