# coding: utf-8
from bs4 import BeautifulSoup

from utils.requests_kit import get_content


def spider_xici_crawl():
    urls = ['http://www.xicidaili.com/nn/', 'http://www.xicidaili.com/nn/2', 'http://www.xicidaili.com/wn/']
    result = []
    for url in urls:
        try:
            req = get_content(url)
            table = BeautifulSoup(req.text, 'lxml').find('table', id='ip_list').find_all('tr')
        except:
            continue
        for tr in table[1:]:
            try:
                tds = tr.find_all('td')
                ip = tds[1].get_text() + ':' + tds[2].get_text()
                result.append(ip)
            except:
                pass
    return result
