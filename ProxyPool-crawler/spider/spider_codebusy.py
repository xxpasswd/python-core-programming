# coding: utf-8
from bs4 import BeautifulSoup

from utils.requests_kit import get_content


def spider_coderbusy_crawl():
    result = []
    for page in range(5):
        url = 'https://proxy.coderbusy.com/classical/anonymous-type/highanonymous.aspx?page=%s' % (page + 1)
        try:
            req = get_content(url)
            table = BeautifulSoup(req.text, 'lxml').find('div', {'class': 'table-responsive'}).find_all('tr')
        except Exception as e:
            continue
        for item in table[1:]:
            try:
                tds = item.find_all('td')
                ip = tds[0].get_text()
                port = tds[2].get_text()
            except:
                continue
            line = ip + ':' + port
            result.append(line.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', ''))
    return result