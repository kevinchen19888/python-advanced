# 多线程

"""
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，
对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
"""

import threading
import time


def loop():
    print("thread %s is running" % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s ended" % threading.current_thread().name)


def thread_run_demo():
    t = threading.Thread(target=loop, name="subLoopThread")
    t.start()
    t.join()
    print("thread %s ended" % threading.current_thread().name)


# thread_run_demo()


# Lock
"""
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，
所以任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
"""

# 多线程并发修改变量问题demo
balance = 0


def change_it(m):
    global balance
    balance = balance + m
    balance = balance - m


def unsafe_run_thread(m):
    [change_it(m) for i in range(1000000)]


# 通过一个全局锁(Lock)来保证线程安全问题
lock = threading.Lock()


def safe_run_thread(m):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(m)
        finally:
            lock.release()


# 因多线程并发修改问题,导致balance 运行结果与预期不一致
def unsafe_multi_thread_run(method_name):
    t1 = threading.Thread(target=method_name, args=(5,))
    t2 = threading.Thread(target=method_name, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("balance is:", balance)


# unsafe_multi_thread_run(safe_run_thread)


import multiprocessing


def loop():
    x = 0
    while True:
        x = x ^ 1


# 无法真正跑满所有cpu,真正意义上只能使用一个cpu
def run_all_cpu():
    for i in range(multiprocessing.cpu_count()):
        t = threading.Thread(target=loop)
        t.start()


# run_all_cpu()

"""
多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响
"""

# =========================================================
# ThreadLocal: 简化了多线程环境中的变量使用问题

# 创建全局 ThreadLocal 对象
local_s = threading.local()


def process_s():
    # 获取当前线程关联的变量std
    std = local_s.std
    print("hello,%s (in %s)" % (std, threading.current_thread().name))


def process_thread(name):
    # 为ThreadLocal 绑定当前线程的变量name
    local_s.std = name
    process_s()
    time.sleep(1)


def threadlocal_run_demo():
    t1 = threading.Thread(target=process_thread, args=('James',), name="thread1")
    t2 = threading.Thread(target=process_thread, args=('Kevin',), name="thread2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("game over")


# threadlocal_run_demo()

"""
ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。
"""
