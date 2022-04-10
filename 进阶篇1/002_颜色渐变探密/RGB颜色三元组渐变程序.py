"""RGB颜色三元组渐变程序.py"""

from coloradd import coloradd

color = (255,0,0)
for i in range(0,200):
    color = coloradd(color,0.01)
    print(color,end=" ") 
