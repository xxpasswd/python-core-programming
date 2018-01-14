import threading
import queue


# 自己定义的函数
def fun(param):
    pass


# 定义线程类
class ThreadRun(threading.Thread):

    def __init__(self,function_name,queue):
        threading.Thread.__init__(self)
        self._queue=queue
        self.function = function_name

    def run(self):
        while not self._queue.empty():
            param = self._queue.get()
            self.function(param)


def main():

    params = []
    q = queue.Queue()
    threads = []

    # 将url参数放入队列中
    for i in params:
        q.put(i)

    # 开多进程
    for i in range(7):
        t = ThreadRun(fun,q)
        t.start()

    # 等待所有线程执行完
    for i in threads:
        i.join()

