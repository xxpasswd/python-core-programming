# -*- coding:utf-8 -*-

import requests


class TuLing(object):
    """
    图灵机器人操作集
    """
    tuling_url = 'http://openapi.tuling123.com/openapi/api/v2'
    apiKey = 'bfc62dd9cb9742f9a9ecd8b04d32e645'
    userId = 'pf'

    def __init__(self):
        pass

    def get_content(self, msg):
        """
        获取图灵回复的信息
        :return: string
        """
        params = {
            "reqType": 0,
            "perception": {
                "inputText": {
                    "text": msg
                },
            },
            "userInfo": {
                "apiKey": self.apiKey,
                "userId": self.userId
            }
        }
        result = requests.post(url=self.tuling_url, json=params)
        text = result.json()['results'][0]['values'].get('text') or result.json()['results'][0]['values'].get('url')
        return text


if __name__ == '__main__':
    data = TuLing().get_content('你是？')
    print(data)
