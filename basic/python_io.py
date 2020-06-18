# input = input("请输入:")
# print(input)

# ==============================
# 文件读写

file = open("io.txt", "r+")
# print(file.encoding)
# print(file.name)
# print(file.mode)
# print(file.closed)
# file.close()
# print(file.closed)

# 写入
print(file.read())
file.write("this is second write\n")
pass
# file.flush()
# print(file.read())
file.close()
