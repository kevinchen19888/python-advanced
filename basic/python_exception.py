"""异常处理示例"""


def exception_demo():
    try:
        fh = open("io.txt", "r")
        try:
            readline = fh.readline()
        finally:
            print("关闭文件")
            fh.write("")  # 此处出错会被外面的except捕捉
            # fh.close()
    # except: # 会捕获所有异常
    except (IOError, SyntaxError):
        print("error:没有找到对应文件或文件夹")
    # except BaseException:  # 所有异常的基类
    #     print("获取所有异常")
    else:  # 如果没有出现异常
        fh.close()
        print(fh.closed)
    finally:
        print("finally最终都会执行")


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
# =============================
class DefinedException(RuntimeError):
    def __init__(self, args):
        self.args = args


def defined_exception():
    try:
        raise DefinedException("自定义异常")
    except DefinedException:
        print("自定义异常")


defined_exception()
