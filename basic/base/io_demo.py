"""
文件读写
"""

file_dir = "D:/Files/pythonWorkspace/python-advanced/basic/base/file/test.txt"


# file = open(file_dir, "r", encoding="utf-8")
# print(file.read())
# file.close()

def read_file():
    file = open(file_dir, "r", encoding="utf-8")
    for line in file:
        print(line.strip())
    # 按行读取到一个列表容器中
    # lines = file.readlines()
    # for l in lines:
    #     print(l.strip())
    file.close()

def read_file2():
    with open(file_dir, 'r', encoding="utf-8") as file:
        print(file.read())


# read_file()

def write_file(content: str):
    # w:  覆盖写入,a:  追加写入
    file = open(file_dir, "w", encoding="utf-8")
    file.write(f'{content}\n')
    file.close()
    read_file()


# write_file("hello world")

"""
异常处理:
Python中和异常相关的关键字有五个，分别是try、except、else、finally和raise
"""


def read_file_exception():
    file = None
    try:
        file = open("file_dir", "r", encoding="utf-8")
        for line in file:
            print(line.strip())
    except FileNotFoundError:
        print('error:没有找到对应文件或文件夹')
    except Exception as e:
        print(f'读取文件异常:{e}')
    else:
        print("没有异常")
    finally:
        if file:
            file.close()


# read_file_exception()


class InputError(ValueError):
    """自定义异常"""
    pass


def raise_exception(n):
    if n < 0:
        raise InputError("输入的数字不能小于0")

# raise_exception(-1)

def read_file_exception2(file_dir):
    try:
        # 文件操作完成后自动执行文件对象的close方法(上下文管理器协议（有__enter__和__exit__魔术方法）)
        with open(file_dir, "r", encoding="utf-8") as file:
            print(file.read())
    except  FileNotFoundError:
        print('error:没有找到对应文件或文件夹')
    except Exception as e:
        print(f'读取文件异常:{e}')
    else:
        print("没有异常")


# read_file_exception2(file_dir)
