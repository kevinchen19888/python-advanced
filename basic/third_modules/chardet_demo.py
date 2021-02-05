# 对 byte 类型数据进行编码检测
import chardet


def chardet_use():
    s = chardet.detect(b'hello,world')
    print(s)  # 结果中的confidence字段，表示检测的概率是1.0（即100%）
    data = chardet.detect('离离原上草，一岁一枯荣'.encode('gbk'))
    print(data)
    # 对日文进行检测：
    data = '最新の主要ニュース'.encode('euc-jp')
    f = chardet.detect(data)
    print(f)


# 当我们拿到一个bytes时，就可以对其检测编码。用chardet检测编码，只需要一行代码：
# chardet_use()

"""
使用chardet检测编码非常容易，chardet支持检测中文、日文、韩文等多种语言。
"""
