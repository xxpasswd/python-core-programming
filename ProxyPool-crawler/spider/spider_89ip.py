# coding: utf-8
import re
import time

from utils.requests_kit import get_content


def spider_89ip_crawl():
    urls = ['http://www.89ip.cn/tiqv.php?sxb=&tqsl=300&ports=&ktip=&xl=on&submit=%CC%E1++%C8%A1']
    result = []
    for pageurl in urls:
        try:
            req = get_content(pageurl)
            html = req.text
        except Exception as e:
            continue
        ips = re.findall('\d+\.\d+\.\d+\.\d+:\d+', html)
        result += ips
        time.sleep(2)
    return result
