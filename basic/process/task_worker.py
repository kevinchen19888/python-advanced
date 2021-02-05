import time, sys, queue
from multiprocessing.managers import BaseManager

# 创建类似的 QueueManager
from multiprocessing.queues import Queue


class QueueManager(BaseManager):
    pass


# 由于此 QueueManager只从网络上获取 queue,所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
# 连接到服务器,即运行task_master.py的机器,端口与验证码保持与task_master的完全一致
server_addr = '127.0.0.1'
print('connect to server %s' % server_addr)
m = QueueManager(address=(server_addr, 8081), authkey=b'abc')
# 从网络连接
m.connect()
# 获取queue的对象
task = m.get_task_queue()
result = m.get_result_queue()
# 从task队列获取任务,并把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print("run task %d * %d" % (n, n))
        r = "%d * %d = %d" % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print("task queue is empty")

# 处理结束
print("worker exit")
