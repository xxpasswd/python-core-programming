# coding: utf-8
from utils.requests_kit import get_content_by_proxy
from utils.db_helper import DBHelper

url = 'https://www.cnblogs.com/time-read/p/9397615.html'

db = DBHelper()

headers = {
    'referer': 'https://www.cnblogs.com/'
}

proxies_ip = db.get_all_ips()

for i in proxies_ip:
    res = get_content_by_proxy(url, i, headers=headers)
    if res:
        print(i)
        print(res.text)
        print(res.status_code)
    else:
        print('failed')

