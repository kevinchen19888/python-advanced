# 协程，又称微线程，纤程。英文名Coroutine,Python对协程的支持是通过 generator 实现的。
"""
协程相对于线程的优势:
1,执行效率高(线程不需要进行线程切换,而是由程序自身控制)
2,不需要多线程的锁机制(只有一个线程)
多核环境下提升执行效率,可以通过:多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能
"""


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('consuming %s...' % n)
        r = '200 ok'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('producing %s' % n)
        r = c.send(n)
        print('consumer return:%s' % r)
    c.close()


c = consumer()
produce(c)

"""
consumer函数是一个generator，把一个consumer传入produce后：

1,首先调用c.send(None)启动生成器；
2,然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
3,consumer通过yield拿到消息，处理，又通过yield把结果传回；
4,produce拿到consumer处理的结果，继续生产下一条消息；
5,produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务

'子程序就是协程的一种特例'---Donald Knuth
"""
