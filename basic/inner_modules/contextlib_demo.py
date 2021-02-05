# contextlib
# 并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
# 实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方法：


class Read(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('error')
        else:
            print('end')

    def read(self):
        print('read info about %s' % self.name)


# 这样就可以把自己写的资源对象用于with语句：

def defined_read():
    with Read('hello') as f:
        f.read()


# defined_read()

# 编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：


class Read2(object):

    def __init__(self, name):
        self.name = name

    def read(self):
        print('read:%s' % self.name)


from contextlib import contextmanager


@contextmanager
def create_read():
    read = Read2('kevin')
    print('begin')
    yield read
    print('end')


# @contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，
# 然后，with语句就可以正常地工作了：
def context_read():
    with create_read() as f:
        f.read()


# context_read()


# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：
@contextmanager
def enhance(tag):
    print('<%s>' % tag)
    yield
    print('<%s/>' % tag)


def enhance_run():
    with enhance('h1'):
        print('hello world')


# enhance_run()

"""
代码的执行顺序是：
1,with语句首先执行yield之前的语句，因此打印出<h1>；
2,yield调用会执行with语句内部的所有语句，因此打印出hello和world；
3,最后执行yield之后的语句，打印出</h1>。
"""
