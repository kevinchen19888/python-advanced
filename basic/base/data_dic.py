"""
字典使用
todo:列表，集合，字典等可变类型不能作为key
"""

def dic_demo1():
    dic = {'age':10,'name':'kevin'}
    # print(dic)
    print(len( dic))
    for key in dic:
        print(key, dic[key])

# dic_demo1()

"""
成员运算/索引运算
"""

def dic_demo2():
    dic = {'age':10,'name':'kevin'}
    print('name' in dic)
    # 索引运算获取字典中值，如果获取不到，会报错
    print(dic['name'])

# dic_demo2()

"""
字典方法
"""
def dic_demo3():
    dic = {'age':10,'name':'kevin'}
    # print(dic.get('name'))
    print(dic.keys())
    # for key in dic.keys():
    #     print(key, dic[key])
    print(dic.values())
    # for v in dic.values():
    #     print(v)
    print(dic.items())
    # for k, v in dic.items():
    #     print(k, v)
    # 更新操作
    dic.update({'age':20,'sex':'male'})
    # print(dic)
    # 3.9版本可以使用 | 更新
    dic = dic | {'age':20,'sex':'male'}
    # print(dic)
    # 删除操作
    # dic.pop('age')
    del dic['age']
    print(dic)
    dic.popitem()
    dic.clear()
    print( dic)

# dic_demo3()

# 输入一段话，统计每个英文字母出现的次数，按出现次数从高到低输出
def dic_demo4():
    sentence = input('请输入一段话: ')
    counter = {}
    for ch in sentence:
        if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
            counter[ch] = counter.get(ch, 0) + 1

    sorted_keys = sorted(counter, key=counter.get, reverse=True)
    for key in sorted_keys:
        print(f'{key} 出现了 {counter[key]} 次.')



# dic_demo4()

# 在一个字典中保存了股票的代码和价格，找出股价大于100元的股票并创建一个新的字典。
def dic_demo5():
    stocks = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29
    }
    stocks2 = {key: val for key, val in stocks.items() if val > 200}
    print(stocks2)


# dic_demo5()