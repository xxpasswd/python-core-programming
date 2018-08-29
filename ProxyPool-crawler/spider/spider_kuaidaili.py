# coding: utf-8
from bs4 import BeautifulSoup

from utils.requests_kit import get_content


def spider_kuaidaili_crawl():
    result = []
    for page in range(1, 10):
        url = 'https://www.kuaidaili.com/ops/proxylist/{}/'.format(page)
        try:
            req = get_content(url)
            table = BeautifulSoup(req.text, 'lxml').find(
                'div', {'id': 'freelist'}).find('table').find_all('tr')
        except Exception as e:
            continue
        for tr in table[1:]:
            try:
                ip = tr.find('td', {'data-title': 'IP'}).get_text()
                port = tr.find('td', {'data-title': 'PORT'}).get_text()
                ip = ip + ':' + port
                result.append(ip)
            except:
                pass
    return result
