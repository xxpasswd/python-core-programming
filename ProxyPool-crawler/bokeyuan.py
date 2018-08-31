# coding: utf-8
from utils.requests_kit import get_content_by_proxy
from utils.db_helper import DBHelper
from utils.logger import logger

url = 'https://www.cnblogs.com/time-read/p/9397615.html'

db = DBHelper()

headers = {
    'referer': 'https://www.cnblogs.com/'
}

proxies_ip = db.get_all_ips()

url = 'https://www.nyloner.cn/checkip'

for i in proxies_ip:
    headers.update({"X-Forwarded-For": "{}".format(i.split(':')[0])})
    res = get_content_by_proxy(url, i, headers=headers)
    if res:
        print(i)
        print(res.text)
        print(res.status_code)
    else:
        print('failed')

