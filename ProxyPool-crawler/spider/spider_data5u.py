# coding: utf-8
from bs4 import BeautifulSoup

from utils.requests_kit import get_content


def spider_data5u_crawl():
    urls = ['http://www.data5u.com/free/gngn/index.shtml', 'http://www.data5u.com/free/gwgn/index.shtml',
            'http://www.data5u.com/free/gnpt/index.shtml', 'http://www.data5u.com/free/gwpt/index.shtml']
    result = []
    for url in urls:
        try:
            req = get_content(url)
            table = BeautifulSoup(req.text, 'lxml').find_all('ul', {"class": 'l2'})
        except Exception as e:
            continue
        for item in table[1:]:
            try:
                spans = item.find_all('span')
                ip = spans[0].get_text()
                port = spans[1].get_text()
            except:
                continue
            line = ip + ':' + port
            result.append(line.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', ''))
    return result
