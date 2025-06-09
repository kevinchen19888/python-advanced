# aiohttp 使用demo,asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架。
"""
编写一个HTTP服务器，分别处理以下URL：
1. / - 首页返回b'<h1>Index</h1>'；
2. /hello/{name} - 根据URL参数返回文本hello, %s!。
"""
import asyncio

from aiohttp import web


async def index(req):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1')


async def hello(req):
    await asyncio.sleep(0.5)
    text = '<h1>hello,%s!</h1>' % req.match_info['name']
    return web.Response(body=text.encode('utf8'), content_type='text/html')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('server started')
    return srv


def create_server():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init(loop))
    loop.run_forever()


create_server()


# asyncio 使用demo
async def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = await asyncio.sleep(2)
    print("Hello again!")


async def hello2():
    print('hello2...')
    await asyncio.sleep(1)
    print('hello2 end...')


def asyncio_demo():
    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    # 执行coroutine
    loop.run_until_complete(hello())
    loop.run_until_complete(hello2())
    loop.close()

# asyncio_demo()
