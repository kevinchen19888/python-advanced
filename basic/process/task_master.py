# 分布式进程

"""
python的multiprocessing模块不但支持多进程，
其中managers子模块还支持把多进程分布到多台机器上。
一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信
"""
import queue
import random
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收任务的队列
result_queue = queue.Queue()


# 从BaseManager继承的 QueueManager
class QueueManager(BaseManager):
    pass


# 将两个queue 都注册到网络上,callable 参数关联了queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# 绑定端口 5000,设置验证码'abc'
manager = QueueManager(address=('', 8081), authkey=b'abc')

# 启动queue
manager.start()
# 获得通过网络访问的queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 放任务进去
for i in range(10):
    n = random.randint(0, 1000)
    print("put task %d..." % n)
    task.put(n)

# 从result队列读取结果
print('try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print("result:%s" % r)

# 关闭管理器
manager.shutdown()
print("master exit")
