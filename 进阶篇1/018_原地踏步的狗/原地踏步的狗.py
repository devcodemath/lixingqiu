""" 原地踏步的狗.py,本程序定义狗了类。
它实例化后就能不断地原地踏步,但不能向前移动,请完善move方法让它能移动。"""

import glob
from turtle import Turtle,Screen

class Dog:

    def __init__(self,images_right,images_left,position):
        """images：造型列表，sound声音"""
        self.images_right = images_right # 右造型列表
        self.images_left = images_left   # 左造型列表
        self.images = [images_right,images_left]
        self.images_index = 0            # 决定用右还是用左造型的变量
        
        self.index = 0                   # 索引号从0开始
        self.amounts = len(images_right) # 右造型总数量
                
        self.body = Turtle(visible=False)# body属性是一个海龟对象
        self.body.penup()                # 抬笔
        self.body.goto(position)         # 定位
        self.sw = self.body.screen.window_width()
        self.sh = self.body.screen.window_height()
       
        self.body.showturtle()           # 显示
        self.next_costume()              # 下一个造型
        
    def next_costume(self):
        """下一个造型"""
        self.image = self.images[self.images_index][self.index]
        self.body.shape(self.image) # 设定造型
        self.index = self.index + 1              # 索引加1
        self.index = self.index % self.amounts   # 对总数求余
        self.move()
        self.body.screen.ontimer(self.next_costume,100) #0.1秒后再次执行
        
    def move(self):
        pass
            
        
if __name__ == "__main__":

    images_r = glob.glob("images_right/*.gif")
    images_l = glob.glob("images_left/*.gif")
    
    width,height = 480,360 

    screen = Screen()
    screen.bgpic("gingerbread.png")
    screen.setup(width,height)
    screen.title("原地踏步的狗")
    
    [screen.addshape(image) for image in images_r]
    [screen.addshape(image) for image in images_l]
    
    dog = Dog(images_r,images_l,(0,-100))

    screen.exitonclick()
