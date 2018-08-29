# coding: utf-8
import time
import re

from utils.requests_kit import get_content


def spider_66ip_crawl():
    urls = [
        'http://www.66ip.cn/nmtq.php?getnum=600&isp=0&anonymoustype=0&start=&ports=&export=&ipaddress=&area=0&proxytype=2&api=66ip']
    result = []
    for url in urls:
        try:
            req = get_content(url)
            html = req.text
        except:
            continue
        ips = re.findall('\d+\.\d+\.\d+\.\d+:\d+', html)
        result += ips
        time.sleep(2)
    return result
