
def string_demo1():
    s1 = 'hello, world!'
    s2 = "你好，世界！❤️"
    s3 = '''hello,
    wonderful
    world!'''
    print(s1)
    print(s2)
    print(s3)
    s1 = '\'hello, world!\''
    s2 = '\\hello, world!\\'
    # 以r或R开头的字符串，表示原始字符串，原始字符串中的转义字符不会被解析：
    s3 = '\it \is \time \to \read \now'
    s4 = r'\it \is \time \to \read \now'
    print(s3)
    print(s4)

"""
字符串的拼接和重复
"""
def string_demo2():
    s1 = 'hello' + ', ' + 'world'
    print(s1)  # hello, world
    s2 = '!' * 3
    print(s2)  # !!!
    s1 += s2
    print(s1)  # hello, world!!!
    s1 *= 2
    print(s1)  # hello, world!!!hello, world!!!

# string_demo2()

"""
string的成员运算
"""
def string_demo3():
    s1 = 'hello, world'
    s2 = 'goodbye, world'
    print('wo' in s1)  # True
    print('wo' not in s2)  # False
    print(s2 in s1)  # False
    # 获取字符串长度
    s = 'hello, world'
    print(len(s))  # 12
    print(len('goodbye, world'))  # 14

# string_demo3()

"""
string 的索引和切片：
与元组几乎没有区别
"""
def string_demo4():
    s = 'abc123456'
    n = len(s)
    print(s[0], s[-n],s[-1])  # a a
    print(s[n - 1], s[-1])  # 6 6
    print(s[2], s[-7])  # c c
    print(s[5], s[-4])  # 3 3
    print(s[2:5])  # c12
    print(s[-7:-4])  # c12
    print(s[2:])  # c123456
    print(s[:2])  # ab
    print(s[::2])  # ac246
    print(s[::-1])  # 654321cba

# string_demo4()

"""
string 遍历
"""


def string_demo5():
    s = 'abc'
    # 方式1
    for i in s:
        print(i)
    # 方式2
    print('第二种方式')
    for i in range(len(s)):
        print(s[i])

# string_demo5()

"""
string 的相关方法
"""
def string_demo6():
    s1 = 'hello, world!'
    # 字符串首字母大写
    print(s1.capitalize())  # Hello, world!
    # 字符串每个单词首字母大写
    print(s1.title())  # Hello, World!
    # 字符串变大写
    print(s1.upper())  # HELLO, WORLD!
    s2 = 'GOODBYE'
    # 字符串变小写
    print(s2.lower())  # goodbye
    # 检查s1和s2的值
    print(s1)  # hello, world
    print(s2)  # GOODBYE
    # 字符串查找
    s = 'hello, world!'
    print(s.find('or'))  # 8
    print(s.find('or', 9))  # -1，找不到默认返回-1
    print(s.find('of'))  # -1
    print(s.index('or'))  # 8
    # print(s.index('or', 9))  # ValueError: substring not found
    # 反向查找
    print(s.rfind('o'))  # 7
    print(s.rindex('o'))  # 7

# string_demo6()

"""
判断
"""
def string_demo7():
    s1 = 'hello, world!'
    print(s1.startswith('He'))  # False
    print(s1.startswith('hel'))  # True
    print(s1.endswith('!'))  # True
    s2 = 'abc123456'
    # 判断字符串是不是完全由数字构成
    print(s2.isdigit())  # False
    # 判断字符串是不是完全由字母构成
    print(s2.isalpha())  # False
    # 判断字符串是不是由字母和数字
    print(s2.isalnum())  # True

# string_demo7()

"""
string 格式化
"""
def string_demo8():
    s = 'hello, world'
    print(s.center(20, '*'))  # ****hello, world****
    print(s.rjust(20))  # hello, world
    print(s.ljust(20, '~'))  # hello, world~~~~~~~~
    # 填充补0
    print('33'.zfill(5))  # 00033
    print('-33'.zfill(5))  # -0033
    # 格式化
    a = 321
    b = 123
    print('%d * %d = %d' % (a, b, a * b))
    print('{0} * {1} = {2}'.format(a, b, a * b))
    c = 2324242
    print(f'{c=:,}')

# string_demo8()

"""
string 修剪/替换操作
"""
def string_demo9():
    s1 = '   jackfrued@126.com  '
    print(s1.strip())  # jackfrued@126.com
    s2 = '~你好，世界~'
    print(s2.lstrip('~'))  # 你好，世界~
    print(s2.rstrip('~'))  # ~你好，世界
    # 替换操作
    s = 'hello, good world'
    print(s.replace('o', '@'))  # hell@, g@@d w@rld
    print(s.replace('o', '@', 1))  # hell@, good world

# string_demo9()

"""
拆分与合并
"""
def string_demo10():
    s = 'I love you'
    words = s.split()
    print(words)  # ['I', 'love', 'you']
    print('~'.join(words))  # I~love~you
    print('编码与解码====>')
    a = '哈哈'
    b = a.encode('utf-8')
    c = a.encode('gbk')
    print(b)  # b'\xe9\xaa\x86\xe6\x98\x8a'
    print(c)  # b'\xc2\xe6\xea\xbb'
    print(b.decode('utf-8'))  # 哈哈
    print(c.decode('gbk'))  # 哈哈

string_demo10()