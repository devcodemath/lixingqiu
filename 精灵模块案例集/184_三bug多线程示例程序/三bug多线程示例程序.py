"""
   三bug多线程示例程序.py
   本程序创建了三个线程,每个线程都会创建一个bug。
   bug定位后会不断地旋转。本程序需要Python精灵模块支持,请用cmd命令,打开管理员窗口,
   然后输入以下使命令进行安装:   
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple sprites   --upgrade
"""
from threading import Thread       # 从threading模块导入Thread类
from sprites import Sprite,Screen  # 从精灵模块导入Sprite类和Screen函数 

def myt1():
    bug = Sprite()                 # 新建角色,默认为虫子
    while True:                    # 当成立的时候
        bug.fd(1)                  # bug前进1个单位 
        bug.rt(1)                  # bug右转1个单位
        
def myt2():
    bug = Sprite()
    bug.goto(100,100)
    while True:
        bug.fd(1)
        bug.lt(1)

def myt3():
    bug = Sprite()
    bug.goto(-100,100)
    while True:
        bug.fd(1)
        bug.lt(1)

screen = Screen()                  # 新建屏幕对象 

thread1 = Thread(target=myt1)      # 创建一个线程
thread2 = Thread(target=myt2)      # 创建一个线程
thread3 = Thread(target=myt3)      # 创建一个线程

thread1.start()                    # 启动线程1
thread2.start()                    # 启动线程2
thread3.start()                    # 启动线程3  

screen.mainloop()                  # 主线程进入循环
