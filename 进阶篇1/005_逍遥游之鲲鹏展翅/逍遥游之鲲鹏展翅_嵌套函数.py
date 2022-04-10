"""逍遥游之鲲鹏展翅_嵌套函数.py"""

from glob import glob
from turtle import *
from time import sleep

def spawn(images,pos):
    """产生一个海龟对象,我们称之为角色sprite"""
    sprite = Turtle(visible=False)  # 新建不可见海龟对象
    sprite.index = 0                # 设定新的属性index
    sprite.penup()                  # 抬笔
    sprite.goto(pos)
    sprite.costume_amounts = len(images)    
    def alt_costume():
        """切换角色造型"""
        sprite.index = sprite.index + 1
        sprite.index = sprite.index % sprite.costume_amounts
        sprite.shape(images[sprite.index])# 设定形状        
    def run():
        """不断地切换造型"""
        alt_costume()        
        sprite.screen.ontimer(run,100)    # 100毫秒后运行        
    sprite.showturtle()                   # 显示角色
    run()                                 # 调用run函数
    
if __name__ == "__main__":                # 如果是直接运行(非做为模块导入)
        
    screen = Screen()                     # 新建屏幕对象
    screen.bgcolor("black")               # 设定屏幕背景为黑色
    screen.title("逍遥游之鲲鹏展翅")      # 设定屏幕标题
    screen.setup(800,360)                 # 设定屏幕大小
    sprite_images =  glob("bird/*.gif")   #  造型列表
    
    for image in sprite_images:               # 此for循环添加造型
        screen.addshape(image)
        
    spawn(sprite_images,(-200,0))          # 生成一只鸟
    spawn(sprite_images,(200,0))          # 生成一只鸟 
    screen.exitonclick()                   # 单击屏幕关闭窗口

