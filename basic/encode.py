import base64


def base64_use():
    print(base64.b64encode(b'binary\x00string'))
    # 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
    print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))


# base64_use()

"""
Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。

"""

# struct模块来解决bytes和其他二进制数据类型的转换
# =======================================================


import struct


def struct_use():
    # >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
    print(struct.pack('>I', 12000))
    # unpack把bytes变成相应的数据类型：
    # 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数
    print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))


# struct_use()

# ==========================================
# hashlib
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
import hashlib


def md5_sha1():
    md5 = hashlib.md5()
    md5.update('how to use md5 in '.encode('utf-8'))
    md5.update('python hashlib?'.encode('utf-8'))
    print("md5:", md5.hexdigest())  # 32 位十六进制串
    # sha1
    sha1 = hashlib.sha1()
    sha1.update('how to use sha1 in '.encode('utf-8'))
    sha1.update('python hashlib?'.encode('utf-8'))
    print("sha1:", sha1.hexdigest())  # 40位十六进制串


# md5_sha1()

"""
摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），
只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
"""

import hmac


# 通过Hmac算法实现带key的哈希(加盐算法),比普通hash算法更安全
def hmac_use():
    global hmac
    key = b'key'
    msg = b'hello world'
    hmac = hmac.new(key=key, msg=msg, digestmod='MD5')
    print(hmac.hexdigest())


# hmac_use()


