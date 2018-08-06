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
def product_groups():
    group_list=[]
    for i in xrange(271):
       group_list.append(u'第'+str(i)+u'组')
    return group_list
def return_message(str):
    if len(str)!=0:
        return '你好'
    else:
        return
def send_message(str,friend):
    print u'信息{0}已经发送给了{1}'.format(str,friend)