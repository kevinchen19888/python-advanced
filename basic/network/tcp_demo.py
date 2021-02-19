# tcp/ip编程demo


import socket
import threading
import time


def socket_client_demo():
    # AF_INET 指定使用ipv4协议,SOCK_STREAM指定使用面向流的TCP协议
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号
    # 建立连接
    s.connect(('www.sina.com.cn', 80))
    # 发送数据
    s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
    # 接收数据
    try:
        buffer = []
        while True:
            # 每次最多接收1k 字节
            d = s.recv(1024)
            if d:
                buffer.append(d)
            else:
                break
    finally:
        # 关闭连接:
        s.close()
    data = b''.join(buffer)
    # 接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，
    # 直到recv()返回空数据，表示接收完毕，退出循环
    # print('接收到的sina数据:', data)
    header, html = data.split(b'\r\n\r\n', 1)
    print(header.decode('utf-8'))
    # 把接收的数据写入文件:
    with open('sina.html', 'wb') as f:
        f.write(html)


# socket_client_demo()


# 服务端demo
def tcplink(sock, addr):
    print('accept new connection from:', addr)
    sock.send(b'welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello,%s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('connection from %s closed' % str(addr))


def socket_server_demo():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    s.bind(('127.0.0.1', 9999))
    s.listen(5)  # 传入的参数指定等待连接的最大数量
    print('waiting for the connection...')
    while True:
        # 接收一个新连接
        sock, addr = s.accept()
        # 创建新线程来处理tcp连接
        t = threading.Thread(target=tcplink, args=(sock, addr))
        t.start()


socket_server_demo()

"""
连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端。
如果客户端发送了exit字符串，就直接关闭连接
"""
