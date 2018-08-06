#!/usr/bin/python3
# -*- coding: utf-8 -*-
from wxpy import *

bot = Bot()
def get_friends():
    friend_list = []
    myFriends = bot.friends()
    for friend in myFriends[1:]:
        friend_list.append(friend.name)
    return friend_list

def send_msg(text_info,friend):
    get_friend = bot.friends().search(friend)[0]
    get_friend.send(text_info)