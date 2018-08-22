# -*- coding:utf-8 -*-

import dataset


class Video:
    DATABASE_URL = 'sqlite:///video.db'
    TABLE_NAME = 'video'

    def __init__(self):
        self._db = dataset.connect(self.DATABASE_URL)
        self._table = self._db[self.TABLE_NAME]

    def get_resource(self, data):
        """
        获取资源
        :param data: string
        :return: string
        """
        query_set = self._table.find(tags=data)
        res_list = [x['url'] for x in query_set]
        return ','.join(res_list)

    def get_resource_test(self, data):
        query_set = self._table.all()
        res_list = [x['url'] for x in query_set]
        return '，'.join(res_list) + '若有密码，则为暂未开放视频，审核通过后即可开放'


if __name__ == '__main__':
    db = dataset.connect(Video().DATABASE_URL)
    table = db[Video().TABLE_NAME]
    table.insert(dict(tags='study', url='http://pan.baidu.com/share/link?shareid=4204796556&uk=3730937393'))
    table.insert(dict(tags='study', url='http://pan.baidu.com/s/1slVEYJz'))
    table.insert(dict(tags='study', url='http://pan.baidu.com/s/1o8Q8efg'))

