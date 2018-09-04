# coding: utf-8
"""
验证ip的有效性,并进行处理
"""
from threading import Thread

import requests


class VerifyIp(Thread):
    def __init__(self, ip_list, res):
        super(VerifyIp, self).__init__()
        self.ip_list = ip_list
        self.res = res

    def run(self):
        while self.ip_list:
            self._process_ip(self.ip_list.pop())

    def _process_ip(self, ip):
        """
        对有效ip进行存储，对无效ip进行删除
        :param ip: str：单个ip
        :return:
        """
        try:
            if self._is_available(ip):
                self.res.append(ip)
        except:
            return

    @staticmethod
    def _is_available(ip):
        """
        验证ip的有效性
        :param ip: str：单个ip
        :return: True/False
        """
        proxies = {
            'http': 'http://{}'.format(ip),
            'https': 'http://{}'.format(ip)
        }

        try:
            res = requests.get('https://www.nyloner.cn/checkip', proxies=proxies, timeout=5)
            res_json = res.json()
            remote_ip = res_json['remote_ip'].strip()
        except:
            return False
        if remote_ip in ip:
            return True
        else:
            return False
