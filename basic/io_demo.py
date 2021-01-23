import os

# input = input("请输入:")
# print(input)

# ==============================================
# 文件读写

file = open("io.txt", "r+")
# print(file.encoding)
# print(file.name)
# print(file.mode)
print(file.closed)

# 读取
# print("读取的string:", file.read(10))
# file.seek(0, 1)
# print("重新读取:", file.read(10))
# file.close()

# print("读取的行:", file.readline())
print("读取的行:", file.__next__())
print("读取的行:", file.__next__())

# 写入
# file.write("hello world/n")
# file.flush()
# print(file.read())
# 文件定位
# print("当前位置:", file.tell())


# 重命名&删除文件,使用os模块
# os.rename("io_new.txt", "io.txt")
# os.remove("io1.txt")

# ==============================================
# 创建&删除&修改目录
# os.mkdir("newDir")
# 进入指定目录
# os.chdir("D:/Data/pythonWorkspace/python-advanced/basic/newDir")
# 显示当前目录
# print(os.getcwd())
# 删除目录
# os.rmdir("D:/Data/pythonWorkspace/python-advanced/basic/newDir")

# 返回指定目录下的所有文件/文件夹
# print(os.listdir("D:/Data/pythonWorkspace/python-advanced/basic"))


# 通过 with 语句来替代 try...finally 完成 流的释放
with open('io.txt', 'r') as f:
    # print("读取到的内容:", f.read())
    print("读取到的内容:", f.read(11))
