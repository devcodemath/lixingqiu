"""
    ball.py
"""
from random import *

_speeds1 = [random()* 10 for x in range(10)]
_speeds2 = [-10 * random()  for x in range(10)]
_speeds = _speeds1 + _speeds2

class Ball:
    """球类，它是无形的，抽象的球"""
    def __init__(self,x,y,radius,color,sw,sh):
        self._x = x                        # 球的中心点x坐标
        self._y = y                        # 球的中心点y坐标 
        self.radius = radius               # 球的半径
        self.color = color                 # 球的颜色
        self._dx = choice(_speeds)         # 水平速度
        self._dy = choice(_speeds)         # 垂直速度
        self._sw = sw                      # 球所在区域的宽度
        self._sh = sh                      # 球所在区域的高度
        
    def pos(self):
        return self._x,self._y             # 返回坐标(二元组)
    
    def move(self):
        self._x += self._dx                # x坐标增加dx
        self._y += self._dy                # y坐标增加dy 
        
    def bounce_on_edge(self):
        """碰到边缘就反弹"""
        left = self._x - self.radius       # 最左x坐标 
        right = self._x + self.radius      # 最右x坐标
        top = self._y + self.radius        # 最上y坐标 
        bottom = self._y - self.radius     # 最下y坐标
        # 小球最左x坐标小于等于区域的最左x坐标或者
        # 小球最右x坐标大于等于区域的最右x坐标
        if left <= -self._sw//2 or right >= self._sw//2:
            self._dx = -self._dx
        if bottom <= -self._sh//2 or top >= self._sh//2:
            self._dy = -self._dy

if __name__ == "__main__":

    pass
