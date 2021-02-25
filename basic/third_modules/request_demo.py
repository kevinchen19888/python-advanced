# requests 使用demo
import requests


def get_with_no_param():
    req = requests.get('https://www.douban.com/')
    print('status:', req.status_code)
    print('content:', req.text)
    print('encoding:', req.encoding)


# get_with_no_param()

def get_with_param():
    req = requests.get('https://www.baidu.com/search', params={'q': 'python'})
    print(req.url)
    # 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
    print(req.content)


# get_with_param()


# 带参数的get请求,传入一个 dict
def get_with_header():
    req = requests.get(
        'https://www.baidu.com',
        headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
    print(req.json())


# requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：
# get_with_header()


def post_run():
    r = requests.post('https://accounts.douban.com/login',
                      data={'form_email': 'abc@example.com', 'form_password': '123456'})
    print(r.status_code)
    print(r.content)


# post_run()

# requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：

def post_with_param():
    params = {'key': 'val'}
    req = requests.post('https://www.baidu.com', json=params)
    print(req.status_code)


# post_with_param()
def upload_file():
    up_file = {'file': open("D:/Data/pythonWorkspace/python-advanced/basic/test_doc/io.txt", "rb")}
    req = requests.post('url', files=up_file)


# 上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
# upload_file()

# 把post()方法替换为put()，delete()等，就可以以PUT或DELETE方式请求资源。


def get_with_cookie():
    cs = {'status': 'working'}
    # requests对Cookie做了特殊处理，使得我们不必解析Cookie就可以轻松获取指定的Cookie：
    # 同时可以用 timeout 指定超时时间,单位 s
    with requests.get('https://www.baidu.com/?tn=88093251_56_hao_pg', cookies=cs, timeout=4) as req:
        print(req.headers)
        print(req.content)
        print("cookies:", req.cookies)


# get_with_cookie()
