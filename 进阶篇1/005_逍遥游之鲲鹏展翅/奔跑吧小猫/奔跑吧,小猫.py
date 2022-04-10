from turtle import *
from time import sleep

def spawn(images,angle):
    sprite = Turtle(visible=False)  # 新建不可见海龟对象
    sprite.index = 0                # 设定新的属性index
    sprite.setheading(angle)        # 设定方向为angle
    sprite.penup()                  # 抬笔
    def run():                      # 定义运行函数        
        sprite.fd(10)               # 角色前进10
        sprite.index = 1 - sprite.index   # 索引在0和1之间切换
        sprite.shape(images[sprite.index])# 设定形状
        sprite.screen.ontimer(run,100)    # 100毫秒后运行
    sprite.showturtle()                   # 显示角色
    run()
    
if __name__ == "__main__":                # 如果是直接运行(非做为模块导入)
        
    screen = Screen()                      # 新建屏幕对象
    cat_images = ['造型1.gif','造型2.gif'] # 猫的两个造型
    for image in cat_images:               # 此for循环添加造型
        screen.addshape(image)
        
    for i in range(5):                     # 此for循环生成5个角色
        spawn(cat_images,i * 360/5)
        
    screen.exitonclick()                   # 单击屏幕关闭窗口

