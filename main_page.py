#!/usr/bin/python3
# -*- coding: utf-8 -*-
import Tkinter as tk
from PIL import Image, ImageTk
import tkFont
import weixin_server.main_server as wxms
from weixin_server.test import product_friends,send_message,product_groups
from utils.screen_center import center_window
import time


def main_page():
    def printList(*args):
        def button_send_message():
            message_text = chat_send_text.get('0.0', tk.END)
            if message_text !='\n':
                send_message(message_text[:-1],friend_name)
                message_time_text = u'我: '+ time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + '\n'
                chat_send_text.delete('0.0', tk.END)
                chat_show_me_text.tag_config('show_font', foreground='black', font=text_chat_font)
                chat_show_me_text.tag_config('time_font', foreground='blue', font=text_time_font)
                chat_show_me_text.insert('0.0', message_text, 'show_font')
                chat_show_me_text.insert('0.0', message_time_text, 'time_font')
                wxms.send_msg(message_text[:-1], friend_name)
        def cancel_send():
            chat_send_text.delete('0.0', tk.END)
        def clean_show_text():
            chat_show_me_text.delete('0.0', tk.END)
            chat_show_friend_text.delete('0.0', tk.END)
        indexs = friend_list.curselection()
        index = int(indexs[0])
        friend_name = friend_list.get(index)
        chat_tl = tk.Toplevel()
        chat_tl.geometry("501x334")
        chat_tl.resizable(False, False)
        chat_tl.title(u"与好友 {0} 的聊天窗口".format(friend_name))
        chat_show_friend_text = tk.Text(chat_tl, width=25, height=16, bg='grey')
        chat_show_friend_text.pack()
        chat_show_friend_text.place(x=5, y=5)
        chat_show_me_text = tk.Text(chat_tl, width=25, height=16, bg='grey')
        chat_show_me_text.pack()
        chat_show_me_text.place(x=180, y=5)
        chat_send_text = tk.Text(chat_tl, width=50, height=6, bg='grey')
        chat_send_text.pack()
        chat_send_text.place(x=5, y=225)
        chat_sent_button = tk.Button(chat_tl, text='发送消息', width=12, height=1, bg="green", command = button_send_message)
        chat_sent_button.pack()
        chat_sent_button.place(x=220, y=312)
        chat_sent_quit = tk.Button(chat_tl, text='取消发送', width=12, height=1, bg="red", command = cancel_send)
        chat_sent_quit.pack()
        chat_sent_quit.place(x=60, y=312)
        control_label = tk.Label(chat_tl, text="控制面板", font=text_font3)
        control_label.pack()
        control_label.place(x=390, y=5)
        auto_label = tk.Label(chat_tl, text="自动回复", font=text_font4)
        auto_label.pack()
        auto_label.place(x=370, y=40)
        machine_label = tk.Label(chat_tl, text="机器回复", font=text_font4)
        machine_label.pack()
        machine_label.place(x=370, y=90)
        shut_label = tk.Label(chat_tl, text="屏蔽消息", font=text_font4)
        shut_label.pack()
        shut_label.place(x=370, y=140)
        time_label = tk.Label(chat_tl, text="定时发送", font=text_font4)
        time_label.pack()
        time_label.place(x=370, y=190)
        time_button = tk.Button(chat_tl, text='设时', width=6, height=1, bg="grey")
        time_button.pack()
        time_button.place(x=440, y=188)
        file_label = tk.Label(chat_tl, text="发送附件", font=text_font4)
        file_label.pack()
        file_label.place(x=370, y=240)
        file_button = tk.Button(chat_tl, text='文件', width=6, height=1, bg="grey")
        file_button.pack()
        file_button.place(x=440, y=238)
        clean_label = tk.Label(chat_tl, text="清空屏幕", font=text_font4)
        clean_label.pack()
        clean_label.place(x=370, y=290)
        clean_button = tk.Button(chat_tl, text='清空', width=6, height=1, bg="grey", command = clean_show_text)
        clean_button.pack()
        clean_button.place(x=440, y=288)
        #tk.Checkbutton(chat_tl, text='python').pack()
        #tk.Entry(chat_tl,text='input').pack()

    main_app = tk.Tk()
    text_font = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)
    text_font2 = tkFont.Font(family='Fixdsys', size=15, weight=tkFont.BOLD)
    text_font3 = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)
    text_font4 = tkFont.Font(family='Fixdsys', size=10, weight=tkFont.BOLD)
    text_chat_font = tkFont.Font(family='微软雅黑', size=12, weight=tkFont.BOLD)
    text_time_font = tkFont.Font(family='微软雅黑', size=10, weight=tkFont.BOLD)
    friend_list_label = tk.Label(text="好友列表", font=text_font, fg='black')
    friend_list_label.pack()
    friend_list_label.place(x=70, y=40)
    friend_list = tk.Listbox(main_app, selectmode=tk.SINGLE, width=20, height=25, font=text_font2, bg='black',
                             fg='white')
    friend_list.pack()
    friend_list.place(x=15, y=110)
    for _, i in enumerate(wxms.get_friends()):
        friend_list.insert(tk.END, i)
        # friend_list.insert(tk.END, '-------')
    friend_list.bind("<<ListboxSelect>>", printList)
    group_list_label = tk.Label(text="群组列表", font=text_font, fg='black')
    group_list_label.pack()
    group_list_label.place(x=340, y=40)
    group_list = tk.Listbox(main_app, selectmode=tk.SINGLE, width=20, height=25, font=text_font2, bg='black',
                             fg='white')
    group_list.pack()
    group_list.place(x=290, y=110)
    for _, i in enumerate(product_groups()):
        group_list.insert(tk.END, i)
        # friend_list.insert(tk.END, '-------')
    group_list.bind("<<ListboxSelect>>", printList)
    center_window(main_app, 990, 660)
    main_app.resizable(False, False)
    main_app.title('微信linux客户端')
    main_app.mainloop()

main_page()
