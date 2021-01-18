import re


# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
def _match():
    print(re.match("www", "www.run.com").span())
    print(re.match("www", "www.run.com"))


# =========================================================
# 	匹配的整个表达式的字符串，group() 可以一次输入多个组号，这种情况下它将返回一个包含那些组所对应值的元组。
def _group():
    line = "Cats are smarter than dogs"
    match_obj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)  # (可选标志)re.I 忽略大小写,re.M 多行模式
    if match_obj:
        print("match.group():", match_obj.group())
        print("match.group(1):", match_obj.group(1))
        print("match.group(2):", match_obj.group(2))


# _group()

# =========================================================
# re.search方法,扫描整个字符串并返回第一个成功的匹配。
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；
# 而re.search匹配整个字符串，直到找到一个匹配。
def _search():
    print(re.search("com", "www.baidu.com"))
    print(re.search("www", "www.baidu.com"))


# _search()


# 检索和替换
def __sub():
    print(re.sub(r"com", "cn", "www.baidu.com"), 0)  # 最后的参数:模式匹配后替换的最大次数，默认 0 表示替换所有的匹配


# __sub()

# =========================================================
# re.compile 函数,用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
def __compile():
    compile = re.compile(r'\d+')
    print(compile.match('one12twothree34four'))  # 查找头部，没有匹配
    print(compile.match('one12twothree34four', 3, 10))  # 从第4个字符开始查找刚好有匹配


# __compile()


# print(re.findall(r'[^a-zA-Z]', "www.baidu.com")) # 匹配除字母外的所有字符
