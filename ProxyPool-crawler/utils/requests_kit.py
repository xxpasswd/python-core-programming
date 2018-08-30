# coding: utf-8
import random

import requests


def my_headers():
    """
    随机生成requests headers信息
    :return:
    """
    headers = {
        # "X-Forwarded-For": '%s.%s.%s.%s' % (
        #     random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
    }
    return headers


def get_content(url, try_times=3):
    """
    请求内容
    :param url:
    :return:
    """
    headers = my_headers()
    res = []
    for i in range(try_times):
        try:
            res = requests.get(url, headers=headers, timeout=5)
            return res
        except:
            continue
    return res


def get_content_by_proxy(url, proxy, try_times=3, headers={}):
    """
    通过代理ip获取内容
    :param url:
    :param proxy:
    :param try_times:
    :return: request.Response
    """
    _headers = my_headers()
    _headers.update(headers)
    res = []
    proxies = {
        'http': 'http://{}'.format(proxy),
        'https': 'http://{}'.format(proxy)
    }
    for i in range(try_times):
        try:
            res = requests.get(url, headers=_headers, proxies=proxies, timeout=5)
            return res
        except:
            continue
    return res
