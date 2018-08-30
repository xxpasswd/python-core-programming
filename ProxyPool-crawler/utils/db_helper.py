# coding: utf-8
"""
数据操作，读取，存储，删除
"""
import dataset


class DBHelper(object):

    DB_NAME = 'sqlite:///IpPool.db'
    TABLE_NAME = 'proxy'

    def __init__(self):
        self._db = dataset.connect(self.DB_NAME)
        self._table = self._db[self.TABLE_NAME]

    def get_all_ips(self):
        """
        获取所有的ip
        :return:list: [{"ip":"112.112.112.112:3434"}]
        """
        ip_list = self._table.distinct('ip')
        return [item['ip'] for item in ip_list]

    def insert_one_ip(self, ip):
        """
        新插入一个ip
        :param ip: str: 112.112.112.112:3434
        :return:
        """
        self._table.insert({"ip": ip})

    def insert_many_ips(self, ip_list):
        items = [{'ip': ip} for ip in ip_list]
        self._table.insert_many(items)

    def delete_one_ip(self, ip):
        """
        删除一个ip
        :param ip: str 112.112.112.112:3434
        :return:
        """
        self._table.delete(ip=ip)
