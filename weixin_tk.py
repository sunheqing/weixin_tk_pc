#!/usr/bin/python3
# -*- coding: utf-8 -*-
import Tkinter as tk
from PIL import Image,ImageTk
import tkFont
from weixin_server.main_server import run_weixin

def resize( w_box, h_box, pil_image):
  w, h = pil_image.size
  f1 = 1.0*w_box/w
  f2 = 1.0*h_box/h
  factor = min([f1, f2])
  width = int(w*factor)
  height = int(h*factor)
  return pil_image.resize((width, height), Image.ANTIALIAS)
def run():
    pass
#run_weixin()
app = tk.Tk()
file_path = 'D:\\app\\python\\tk_app\\'
text_font = tkFont.Font(family='Fixdsys',size = 20,weight = tkFont.BOLD)
text_font2 = tkFont.Font(family='Fixdsys',size = 10,weight = tkFont.BOLD)
#--------------
pil_image = Image.open(r'D:\app\python\tk_app\static\linux3.gif')
pil_image_resized = resize(200, 200, pil_image)
linux_image = ImageTk.PhotoImage(pil_image_resized)
#-------------
pil_image_wx = Image.open(r'D:\app\python\tk_app\static\weixin.gif')
pil_image_resized_wx = resize(200, 200, pil_image_wx)
weixin_image = ImageTk.PhotoImage(pil_image_resized_wx)
#--------------
loginwx_img_label = tk.Label(app, image=weixin_image)
loginwx_img_label.pack()
loginwx_img_label.place(x=100, y=20)
#--------------
loginlin_img_label = tk.Label(app, image=linux_image)
loginlin_img_label.pack()
loginlin_img_label.place(x=330, y=10)
#----------------
text_label = tk.Label(text="警告！",font=text_font)
text_label.pack()
text_label.place(x=40,y=200)
text_label2 = tk.Label(text="该软件个人使用，不得转售、贩卖、或用于其他商业用途！仅供学习交流。",font=text_font2)
text_label2.pack()
text_label2.place(x=40,y=234)
text_label3 = tk.Label(text="该软件通过微信网页端接口实现，频繁使用有被微信官方禁止登录网页端的可能！",font=text_font2)
text_label3.pack()
text_label3.place(x=40,y=252)
text_label4 = tk.Label(text="开发者：城市牛仔 Email:2436437774@qq.com  开发者建议使用官方客户端。",font=text_font2)
text_label4.pack()
text_label4.place(x=40,y=270)

quitButton = tk.Button(text='退出软件',width=10,height=3,font=text_font2,command=quit)
quitButton.pack()
quitButton.place(x=400,y=300)

loginButton = tk.Button(text='进入微信',width=10,height=3,font=text_font2,command=run())
loginButton.pack()
loginButton.place(x=120,y=300)
app.geometry('600x400')
app.title('微信linux客户端')
app.mainloop()