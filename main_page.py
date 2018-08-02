#!/usr/bin/python3
# -*- coding: utf-8 -*-
import Tkinter as tk
from PIL import Image, ImageTk
import tkFont
import weixin_server.main_server as wxms


def printList(event, friend_list):
    print friend_list.get(friend_list.curselection())
def main_page():

    main_app = tk.Tk()
    text_font = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)
    text_font2 = tkFont.Font(family='Fixdsys', size=15, weight=tkFont.BOLD)
    friend_list_label = tk.Label(text="好友列表", font=text_font,fg='black')
    friend_list_label.pack()
    friend_list_label.place(x=40, y=40)
    friend_list = tk.Listbox(main_app,selectmode=tk.SINGLE,width=15,height=25,font=text_font2,bg='black',fg='white')
    friend_list.pack()
    friend_list.place(x=15,y=110)
    for i in range(100):
        friend_list.insert(tk.END,i)
        #friend_list.insert(tk.END, '-------')
    friend_list.bind("<Button-1>", printList(event,friend_list))
    main_app.geometry('990x660')
    main_app.title('微信linux客户端')
    main_app.mainloop()
main_page()
