# -*- coding: utf-8 -*-
from random import uniform

class Particle:
    def __init__(self,x,y):
        self.raw_x = x             # 记录原始x坐标
        self.raw_y = y             # 记录原始y坐标
        self.x = x
        self.y = y
        self.dx = uniform(-10,10)
        self.dy = uniform(1,10)
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.dy -= 1               
        # 超出边界的需要回到中心点
        if self.y < -500:
            self.x = self.raw_x
            self.y = self.raw_y            
            self.dx = uniform(-10,10)
            self.dy = uniform(1,10)
