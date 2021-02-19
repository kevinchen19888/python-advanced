# 客户端程序
import socket


def socket_client_send_demo():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 建立连接
    s.connect(('127.0.0.1', 9999))
    # 接收欢迎消息
    print(s.recv(1024).decode('utf8'))
    for data in [b'michel', b'lucy']:
        # 发送数据
        s.send(data)
        print(s.recv(1024).decode('utf8'))
    s.send(b'exit')
    s.close


socket_client_send_demo()
