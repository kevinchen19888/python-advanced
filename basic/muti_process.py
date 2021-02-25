# 多进程

import os

"""
在Unix/Linux下，可以使用fork()调用实现多进程。
要实现跨平台的多进程，可以使用multiprocessing模块。
进程间通信是通过Queue、Pipes等实现的
"""


def process_exec():
    print('Process (%s) start...' % os.getpid())
    # Only works on Unix/Linux/Mac:
    pid = os.fork()
    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# Windows系统由于没有fork调用,故此调用失败
# process_exec()

from multiprocessing import Process


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def multi_process1():
    global p
    if __name__ == '__main__':
        print('Parent process %s.' % os.getpid())
        # multiprocessing模块提供了一个Process类来代表一个进程对象
        p = Process(target=run_proc, args=('test',))
        print('Child process will start.')
        p.start()
        # 等待子进程结束后再继续往下运行
        p.join()
        print('Child process end.')


# multi_process1()

# 进程池(需要创建大量子进程时)
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


def pool_exec():
    global p
    if __name__ == "__main__":
        print("parent process is: %s" % os.getpid())
        p = Pool(4)
        for i in range(3):
            p.apply_async(long_time_task, args=(i,))
        print("waiting fro all subprocesses...")
        p.close()
        # 等待所有子进程执行完毕,调用join()之前必须先调用close()
        p.join()
        print("all process done")


# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
# pool_exec()


# 子进程控制
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

import subprocess


# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('exit code:', r)

# 控制字进程输入输出
def control_subprocess():
    global p
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)


# control_subprocess()


# 进程间通信

from multiprocessing import Queue


# 写数据进行执行代码
def write(q):
    print("process to write: %s" % os.getpid())
    for val in ['A', 'B', 'C']:
        time.sleep(random.random())
        print("put %s to queue" % val)
        q.put(val)
        time.sleep(random.random())


# 读进程执行代码
def read(q):
    print("process to read: %s" % os.getpid())
    while True:
        val = q.get(True)
        print("get %s from queue" % val)


if __name__ == "__main__":
    # 父进程创建queue,并传给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    # 等待pw结束
    pw.join()
    # pr进程为死循环,只能强行终止
    pr.terminate()
