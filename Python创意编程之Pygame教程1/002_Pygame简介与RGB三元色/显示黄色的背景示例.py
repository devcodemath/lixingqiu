"""
   显示黄色的背景示例.py
"""

import turtle

color = (255,255,0)          # 黄色三元组

screen = turtle.getscreen()  # 获取屏幕对象
screen.colormode(255)        # 设定屏幕颜色模式
screen.bgcolor(color)        # 设定屏幕背景颜色
screen.mainloop()            # 进入主循环刷新组件
