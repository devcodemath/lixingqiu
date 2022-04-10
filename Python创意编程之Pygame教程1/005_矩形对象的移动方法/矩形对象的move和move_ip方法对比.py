"""
   矩形对象的move和move_ip方法对比.py
"""

import pygame

print()
r1 = pygame.Rect(0,0,100,100)
print("原先的矩形对象：r1 = ",r1)
print()

r2 = r1.move(20,20)
print("r1.move(20,20)之后的r1 = ",r1,",结果是r1并没有改变。")
print("r1.move(20,20)之后返回的矩形r2 = ",r2)
print()

r1.move_ip(100,100)
print("r1.move_ip(100,100)之后的r1 = ",r1,",结果是r1已经改变了。")


