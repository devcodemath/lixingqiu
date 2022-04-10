"""
   放梯子.py
   本程序单击鼠标左键会放置一个蓝色长方体在屏幕上
"""
from sprites import *                   # 从精灵模块导入所有命令   

screen = Screen()                       # 新建屏幕

pic = Image.new("RGBA",(150,50),(0,255,0))
pic.save('green.png')
blue = Sprite('green.png')  

leftkey = Mouse()
delay = 0
clock = Clock()                         # 新建时钟对象
while True:
    blue.goto(mouse_pos())              # 跟随鼠标移动
    if leftkey.down() and delay==0:     # 只有delay为0时才放梯子
        blue.clone()                    # 克隆长方体
        screen.title(len(screen._turtles))
        delay = 30                      # 设为30,这样就不能克隆了
    if delay>0 : delay -= 1             # 让delay减1
    screen.update()                     # 更新屏幕显示 
    clock.tick(60)                      # 时间没到1/60秒则继续等待
    
