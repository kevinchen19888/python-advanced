# urllib提供了一系列用于操作URL的功能
import urllib
from urllib import request


def request_run():
    with request.urlopen('https://www.baidu.com') as f:
        data = f.read()
        print('status:', f.status, f.reason)
        print('headers:===================')
        for k, v in f.getheaders():
            print('%s:%s' % (k, v))
        print("==========================")
        print('data:', data.decode('utf8'))


# request_run()


# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，
# 我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：
def request_as_browser():
    req = request.Request('http://www.douban.com/')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 '
                   '(KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print('status:', f.status, f.reason)
        print("===============================")
        for k, v in f.getheaders():
            print('%s:%s' % (k, v))
        print("===============================")
        print('data:', f.read().decode('utf8'))


# request_as_browser()


# ========================================================
# POST请求
# 如果要以POST发送一个请求，只需要把参数data以bytes形式传入。

from urllib import parse


def post_run():
    print('login weibo')
    username = input('username:')
    psd = input('psd:')
    login_data = parse.urlencode([
        ('username', username),
        ('password', psd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
    ])
    req = request.Request('https://passport.weibo.cn/sso/login')
    req.add_header('Origin', 'https://passport.weibo.cn')
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) '
                   'Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Referer',
                   'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

    with request.urlopen(req, data=login_data.encode('utf8')) as f:
        print('status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s:%s' % (k, v))
        print('======================')
        print('data:', f.read().decode('utf8'))


# post_run()


# ========================================================
# Handler
# 如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：

def proxy_run():
    proxy = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
    proxy_auth = urllib.request.ProxyBasicAuthHandler()
    proxy_auth.add_password('realm', 'host', 'username', 'password')
    opener = urllib.request.build_opener((proxy, proxy_auth))
    with opener.open('http://www.example.com/login.html') as f:
        print('status:', f.status, f.reason)


# proxy_run()
