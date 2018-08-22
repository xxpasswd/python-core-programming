# -*- coding:utf-8 -*-

from api.tuling import TuLing
from api.resourse import Video


class Bot(object):
    """
    所有信息的处理接口
    """
    def __init__(self):
        pass

    def get_content(self, data):
        """
        判断想要获取的资源类型
        :param data:
        :return:
        """
        help_msg_list = ['help', '帮助', '功能']
        data_list = data.split(' ')
        data_key = data_list[0]
        if data_key in help_msg_list:
            reply = "输入关键字后，空格后输入想要获取的资源比如：\n"\
                    "电影 天下无贼\n"\
                    "目前支持的关键字：\n"\
                    "   1.电影\n"\
                    "   2.av\n"\
                    "   3.美图\n"
        elif len(data_list) > 1:
            if data_key in ['电影']:
                reply = '为你搜索电影 {}'.format(data_list[1]) + ' 没有搜到资源'
            elif data_key in ['av', 'Av', 'AV', 'aV']:
                reply = '有关{}的学习资料，淫家只有这么多了：'.format(data_list[1])
                search_res = Process().search(data)
                reply += search_res
            else:
                reply = Process().tuling_msg(data)
        else:
            reply = Process().tuling_msg(data)
        return reply


class Process(object):
    """
    各种获取信息的操作集合封装
    """
    def __init__(self):
        pass

    def tuling_msg(self, data):
        res = TuLing().get_content(data)
        return res

    def search(self, data):
        video = Video()
        res = video.get_resource_test(data)
        return res
