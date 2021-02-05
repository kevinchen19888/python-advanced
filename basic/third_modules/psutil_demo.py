# psutil
# 在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities，
# 它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。


import psutil


def cpu_count():
    # CPU逻辑数量
    print(psutil.cpu_count())
    print(psutil.cpu_count(logical=False))
    # 统计CPU的用户／系统／空闲时间：
    print(psutil.cpu_times())


# cpu_count()


def refresh_cpu():
    for _ in range(10):
        print(psutil.cpu_percent(interval=1, percpu=True))


# 实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
# refresh_cpu()
def get_memory_info():
    # 获取物理内存信息
    print(psutil.virtual_memory())
    # 获取交换内存信息
    print(psutil.swap_memory())


# get_memory_info()


def get_disk_info():
    # 获取磁盘信息(磁盘分区信息)
    print(psutil.disk_partitions())
    # 磁盘使用情况
    print(psutil.disk_usage('/'))
    # 磁盘io情况
    print(psutil.disk_io_counters())


# get_disk_info()


def get_net_info():
    # 获取网络读写字节／包的个数
    print(psutil.net_io_counters())
    # 获取网络接口信息
    print(psutil.net_if_addrs())
    # 获取网络接口状态
    print(psutil.net_if_stats())


# get_net_info()

# 获取进程信息
# print(psutil.pids())
# p = psutil.Process(3776) # 获取指定进程ID=3776，其实就是当前Python交互环境
# print(p)


"""
psutil使得Python程序获取系统信息变得易如反掌。

psutil还可以获取用户信息、Windows服务等很多有用的系统信息，具体请参考psutil的官网：https://github.com/giampaolo/psutil
"""
