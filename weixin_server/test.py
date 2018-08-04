#!/usr/bin/python3
# -*- coding: utf-8 -*-
##################模拟微信#####################
import faker
f = faker.Faker(locale='zh_CN')
def product_friends():
    friend_list=[]
    for i in xrange(271):
       friend_list.append(f.name())
    return friend_list
def return_message(str):
    if len(str)!=0:
        return '你好'
    else:
        return