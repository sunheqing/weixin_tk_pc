#!/usr/bin/python3
# -*- coding: utf-8 -*-
import Tkinter as tk
from PIL import Image, ImageTk
import tkFont
import weixin_server.main_server as wxms
from weixin_server.test import product_friends
from utils.screen_center import center_window


def main_page():
    def printList(*args):
        def test_index():
            print index

        indexs = friend_list.curselection()
        index = int(indexs[0])
        friend_name = friend_list.get(index)
        chat_tl = tk.Toplevel()
        chat_tl.geometry("501x334")
        chat_tl.title(u"与好友 {0} 的聊天窗口".format(friend_name))
        chat_show_text = tk.Text(chat_tl, width=50, height=16, bg='grey')
        chat_show_text.pack()
        chat_show_text.place(x=5, y=5)
        chat_send_text = tk.Text(chat_tl, width=50, height=6, bg='grey')
        chat_send_text.pack()
        chat_send_text.place(x=5, y=225)
        chat_sent_button = tk.Button(chat_tl, text='发送消息', width=12, height=1, bg="green")
        chat_sent_button.pack()
        chat_sent_button.place(x=60, y=312)
        chat_sent_quit = tk.Button(chat_tl, text='取消发送', width=12, height=1, bg="red", command=test_index)
        chat_sent_quit.pack()
        chat_sent_quit.place(x=220, y=312)
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
        #tk.Checkbutton(chat_tl, text='python').pack()
        #tk.Entry(chat_tl,text='input').pack()

    main_app = tk.Tk()
    text_font = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)
    text_font2 = tkFont.Font(family='Fixdsys', size=15, weight=tkFont.BOLD)
    text_font3 = tkFont.Font(family='Fixdsys', size=12, weight=tkFont.BOLD)
    text_font4 = tkFont.Font(family='Fixdsys', size=10, weight=tkFont.BOLD)
    friend_list_label = tk.Label(text="好友列表", font=text_font, fg='black')
    friend_list_label.pack()
    friend_list_label.place(x=40, y=40)
    friend_list = tk.Listbox(main_app, selectmode=tk.SINGLE, width=15, height=25, font=text_font2, bg='black',
                             fg='white')
    friend_list.pack()
    friend_list.place(x=15, y=110)
    for _, i in enumerate(product_friends()):
        friend_list.insert(tk.END, i)
        # friend_list.insert(tk.END, '-------')
    friend_list.bind("<<ListboxSelect>>", printList)
    center_window(main_app, 990, 660)
    main_app.resizable(False, False)
    main_app.title('微信linux客户端')
    main_app.mainloop()


main_page()
