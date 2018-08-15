# -*- coding=utf-8 -*-

import itchat
from itchat.content import *

from wxbot.get_content import Bot


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
        r_text = "我的小脑瓜zi还不行，不想看图片，太费脑子了(〃'▽'〃)"
    else:
        u_text = msg['Text']
        r_text = Bot().get_content(u_text)
    all_text = r_text + '\n\n（小哥哥莫要着急(～￣▽￣)～，更多功能还在开发中哦）'
    return all_text


def run():
    itchat.auto_login(hotReload=True)
    itchat.run()
