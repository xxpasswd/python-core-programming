# coding: utf-8
"""
获取代理ip
"""
import time
from threading import Thread

from utils.db_helper import DBHelper
from verify_process.verify_ip import VerifyIp
from spider.spider_66ip import spider_66ip_crawl
from spider.spider_89ip import spider_89ip_crawl
from spider.spider_xici import spider_xici_crawl


class SpiderIp(Thread):
    def __init__(self, fun):
        super(SpiderIp, self).__init__()
        self.fun = fun
        self._res = []

    def run(self):
        self._res = self.fun()

    @property
    def result(self):
        return self._res


def start_spider(crawlers):
    """
    爬取结果
    :param crawlers:
    :return:
    """
    tasks = []
    res = []
    # 创建需要爬行的线程
    for i in crawlers:
        tasks.append(SpiderIp(i))

    # 开始所有线程
    for task in tasks:
        task.start()

    # 等待所有线程完成
    for task in tasks:
        task.join()

    # 获取所有的爬行结果
    for task in tasks:
        try:
            res += task.result
        except:
            continue
    return res


def process_res(ip_list):
    """
    验证ip有效性，并处理结果
    :param res:
    :return:
    """
    ip_valid_list = []
    threads = []
    # 创建处理ip结果的线程
    for i in range(50):
        threads.append(VerifyIp(ip_list, ip_valid_list))

    # 开始所有线程
    for thread in threads:
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    db = DBHelper()
    db.insert_many_ips(ip_valid_list)
    print(ip_valid_list)


if __name__ == '__main__':

    start_time = time.time()
    crawlers = [spider_xici_crawl]
    print('开始进行抓取数据')
    ip_list = start_spider(crawlers)
    print(ip_list, len(ip_list))
    print('已运行完所有爬虫，进行处理数据')
    process_res(ip_list)
    print('所有结果已经处理完毕')
    print('共计用时 {}'.format(time.time()-start_time))
