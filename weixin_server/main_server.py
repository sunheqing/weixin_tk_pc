#!/usr/bin/python3
# -*- coding: utf-8 -*-
from wxpy import *
import itchat
def run_weixin():
    itchat.login()
    itchat.send('Hello, filehelper', toUserName='filehelper')

def test(event):
    bot = Bot()
    my_friend = bot.friends
    print my_friend
