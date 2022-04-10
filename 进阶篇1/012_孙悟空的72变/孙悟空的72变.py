"""孙悟空的72变.py"""

from glob import glob
from tkinter import messagebox
from random import choice
from winsound import PlaySound,SND_ASYNC,SND_LOOP

music = "images/西游记片头曲敲鼓.wav"

screen = Screen()                   # 建屏幕
screen.bgpic("images\\背景2.png")   # 铺背景
screen.title("孙悟空的72变")        # 设定标题
screen.setup(480,360)               # 设定屏幕分辨率

sunwukong = "images\\孙悟空.gif"    
gif_images = glob("images\\*.gif")  # 获取所有的gif到列表
[screen.addshape(image) for image in gif_images ] # 批量注册到屏幕
gif_images.remove(sunwukong)        # 这个图形不要在'gif_images'里

t = Turtle(shape=sunwukong)
messagebox.showinfo("Hi,", "我是孙悟空,大家都知道我有72变")
messagebox.showinfo("大家好", "请按回车键让我变身吧!")
PlaySound(music,SND_ASYNC|SND_LOOP) # 循环播放背景音乐

screen.onkeypress(lambda:t.shape(choice(gif_images)),"Return")
screen.listen()                     # 监听按键事件(给屏幕设置焦点)
screen.mainloop()                   # 主循环
