""" 太阳花丛中的蝴蝶.py。"""

import glob
from turtle import Turtle,Screen

class Butterfly:

    def __init__(self,images,position):
        """images：造型列表，position：坐标"""
        self.images = images             # 造型列表属性
        self.index = 0                   # 索引号从0开始
        self.amounts = len(images)       # 造型总数量
        
        self.body = Turtle(visible=False)# body属性是一个海龟对象
        self.body.penup()                # 抬笔
        self.body.goto(position)         # 定位
       
        self.body.showturtle()           # 显示
        self.next_costume()              # 下一个造型
        
    def next_costume(self):
        """下一个造型"""
        self.body.shape(self.images[self.index]) # 设定造型
        self.index = self.index + 1              # 索引加1
        self.index = self.index % self.amounts   # 对总数求余
        
        self.body.screen.ontimer(self.next_costume,100) #0.1秒后再次执行
        
if __name__ == "__main__":

    images = glob.glob("butterfly/*.gif")        # 所有gif图片表
    width,height = 800,450                       # 定义宽高

    screen = Screen()                            # 新建屏幕对象
    screen.bgpic("太阳花背景.png")               # 设定背景图
    screen.setup(width,height)                   # 设定屏幕宽高
    screen.title("太阳花丛中的蝴蝶")             # 设定屏幕标题
    
    [screen.addshape(image) for image in images] # 注册所有gif到形状列表

    positions = [(-100,110),(-340,-100),(280,-20)] # 三只蝴蝶的坐标表
    for pos in positions:                          # 迭代坐标表
        Butterfly(images,pos)                      # 根据images和pos生成蝴蝶

    screen.exitonclick()                           # 单击屏幕关闭窗口
