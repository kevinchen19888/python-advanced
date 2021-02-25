# 序列化


import pickle


def serialize():
    d = dict(name="kevin", age=10)
    # 序列化
    # pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
    print(pickle.dumps(d))
    # 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object
    with open("test_doc/dump.txt", "wb") as f:
        pickle.dump(d, f)
    # 读取(反序列化)
    with open("test_doc/dump.txt", "rb") as f:
        print(pickle.load(f))


# serialize()

# ===================================================
# JSON处理
import json


def json_serialize():
    d = dict(name="james", age=20, addres=["bj", "gd"])
    # 把Python对象变成一个J0SON
    print(json.dumps(d))
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    # 把JSON的字符串反序列化成 python 对象
    print(json.loads(json_str))


# json_serialize()

# JSON 与 对象 之间的序列化和反序列化

class JsonStu(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


# JsonStu 序列化json的转换函数
def stu2dict(std):
    return {
        "name": std.name,
        "age": std.age
    }


def dict2stu(dic):
    return JsonStu(dic["name"], dic["age"])


# 普通对象的json 序列化与反序列化
def obj_serialize():
    global s
    s = JsonStu("kevin", 100)
    # 使用转换函数进行序列化
    print(json.dumps(s, default=stu2dict))
    # 将class转换成 dict 进行序列化
    print(json.dumps(s, default=lambda obj: s.__dict__))
    # 使用转换函数进行反序列化
    s2 = json.loads('{"age": 20, "score": 88, "name": "Bob"}', object_hook=dict2stu)
    print(s2.name)


# obj_serialize()
