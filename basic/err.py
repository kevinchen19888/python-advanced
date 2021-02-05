# 使用 pdb(python调试器)进行调试
"""
1.使用 python -m pdb err.py 启动
2.以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：
3.输入命令n可以单步执行代码：
4.任何时候都可以输入命令p 变量名来查看变量：
5.输入命令q结束调试，退出程序：
"""
# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace()  # 运行到这里会自动暂停
print(10 / n)
