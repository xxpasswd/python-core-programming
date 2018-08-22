# -*- coding=utf-8 -*-

import itchat
from itchat.content import *

from wxbot.get_content import Bot


# 群组@消息回复
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        print(msg)
        print('\n')
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))


@itchat.msg_register([TEXT, PICTURE])
def print_content(msg):
    print(msg)
    print('\n')
    if msg['Type'] != 'Text':
        reply_text = "偶的小脑瓜zi还不行，不想看图片，太费脑子啦(〃'▽'〃)"
    else:
        received_text = msg['Text']
        reply_text = Bot().get_content(received_text)
    all_text = reply_text + '\n\n(～￣▽￣)～回复帮助，有更多功能'
    return all_text


def run():
    itchat.auto_login(hotReload=True)
    itchat.run()
