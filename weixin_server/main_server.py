#!/usr/bin/python3
# -*- coding: utf-8 -*-
from wxpy import *
import itchat
def run_weixin():
    itchat.login()
    itchat.send('Hello, filehelper', toUserName='filehelper')