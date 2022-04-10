"""自我介绍练习一.py,请运行本程序,完善它。
   具体方法:在introduce函数里,新建一只海龟,
   让它用write方法写上相关数据."""
from turtle import *

def introduce():
    screen.onkeypress(None,"Return")  # 取消绑定
    screen.bgpic("这就是我.png")      # 设定背景图
    print("自我介绍")
    
screen = Screen()
screen.setup(600,700)
screen.bgpic("封面.png")               # 设定背景图
screen.onkeypress(introduce,"Return")  # 按回车键就调用introduce函数
screen.listen()                        # 监听键盘按键
screen.mainloop()                      # 进入主循环
