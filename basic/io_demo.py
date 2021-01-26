import os

# input = input("请输入:")
# print(input)
"""
在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。
"""


# ==============================================
# 文件读写

def basic_rw():
    file = open("test_doc/io.txt", "r+")
    print(file.encoding)
    print(file.name)
    print(file.mode)
    print(file.closed)
    # 读取
    print("读取的string:", file.read(10))
    file.seek(0, 1)
    print("重新读取:", file.read(10))
    file.close()
    # print("读取的行:", file.readline())
    # print("读取的行:", file.__next__())
    # print("读取的行:", file.__next__())
    # 写入
    # file.write("hello world/n")
    # file.flush()
    # print(file.read())
    # 文件定位
    # print("当前位置:", file.tell())
    # 重命名&删除文件,使用os模块
    # os.rename("io_new.txt", "io.txt")
    # os.remove("io1.txt")
    # ==============================================
    # 创建&删除&修改目录
    # os.mkdir("newDir")
    # 进入指定目录
    # os.chdir("D:/Data/pythonWorkspace/python-advanced/basic/newDir")
    # 显示当前目录
    # print(os.getcwd())
    # 删除目录
    # os.rmdir("D:/Data/pythonWorkspace/python-advanced/basic/newDir")
    # 返回指定目录下的所有文件/文件夹
    # print(os.listdir("D:/Data/pythonWorkspace/python-advanced/basic"))


# basic_rw()

# 通过 with 语句来替代 try...finally 完成 流的释放
with open('test_doc/io.txt', 'r') as f:
    # print("读取到的内容:", f.read())
    pass
    # print("读取到的内容:", f.read(11))

# 读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
with open('test_doc/binary-test.png', 'rb') as f:
    pass
    # print(f.name)


def read_binary():
    global f
    with open('test_doc/encoding_demo.txt', 'r', encoding='gbk', errors='ignore') as f:
        # print(f.readline())
        print(f.read())


# 指定字符集读取
# errors参数，表示如果遇到编码错误后会忽略
# read_binary()


# 文件写入,使用'w'(覆盖的方式)
def write_demo_with_w():
    global f
    with open('test_doc/io.txt', 'w') as f:
        f.write('Today is a fine day!')


# write_demo_with_w()

# 追加写入
def write_with_a():
    global f
    with open('test_doc/io.txt', 'a') as f:
        f.write('\rappend txt!')


# write_with_a()


# ==========================================
# StringIO顾名思义就是在内存中读写str
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：

from io import StringIO


def string_io():
    s = StringIO()
    s.write('hello ')
    s.write('world')
    print(s.getvalue())
    s1 = StringIO('fine day!')
    print(s1.getvalue())


# string_io()


# BytesIO: 在内存中操作二进制数据

from io import BytesIO


def bytes_io():
    global b
    b = BytesIO('你好,世界'.encode('utf8'))
    print(b.getvalue())
    print(b.getvalue().decode('utf8'))


# bytes_io()


# ==========================================
# 操作文件和目录


# 环境变量
def env_demo():
    print(os.name)
    # os.uname()
    print(os.environ)  # 获取所有环境变量
    print('PATH is:', os.environ.get('PATH'))


# env_demo()

# 查看当前目录的绝对路径:
# print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# print(os.path.join('/Users/michael', 'testdir'))
# 然后创建一个目录:
# os.mkdir('/Users/michael/testdir')

# 删掉一个目录:
# os.rmdir('/Users/michael/testdir')
def path_opt():
    print(os.path.join(os.path.abspath('.'), '/hello'))
    # 通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
    print(os.path.split('/Users/michael/testdir/file.txt'))
    # os.path.splitext()可以直接让你得到文件扩展名
    print(os.path.splitext('/path/to/file.txt'))


# 拼接路径
# path_opt()

import shutil  # os模块的补充

# shutil.copyfile('test_doc/io.txt', 'test_doc/io_copy.txt')

# 列出当前目录的所有 .py文件
# [print(x) for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

"""
Python的os模块封装了操作系统的目录和文件操作，注意这些函数有的在os模块中，有的在os.path模块中。
"""