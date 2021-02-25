# “测试驱动开发”（TDD：Test-Driven Development）
# 单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。

# 单元测试demo
import unittest


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


# 为了编写单元测试，我们需要引入Python自带的unittest模块
# 同时可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行
class TestDict(unittest.TestCase):
    """
    编写单元测试时，我们需要编写一个测试类，从unittest.TestCase继承。
    以test开头的方法就是测试方法，不以test开头的方法不被认为是测试方法，测试的时候不会被执行。
    """

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
        print("test_init run...")

    def test_key(self):
        d = Dict()
        d['key'] = 'val'
        self.assertEqual(d.key, 'val')
        print("test_key run...")

    def test_attr(self):
        d = Dict()
        d.key = 'val'
        self.assertEqual(d['key'], 'val')
        self.assertTrue('key' in d)
        print("test_attr run...")

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
        print("test_keyerror...")

    def test_attrerror(self):
        d = Dict()
        # with 上下文管理
        with self.assertRaises(AttributeError):  # 通过d['empty']访问不存在的key时，断言会抛出KeyError
            value = d.empty
        print("test_attrerror run...")

    def setUp(self):
        print("setUp run...")

    def tearDown(self):
        print("tearDown run ...")


dic = TestDict()
# dic.test_init()
# dic.test_key()

# 运行单元测试
# 在命令行通过参数-m unittest直接运行单元测试：
# python -m unittest mydict_test
