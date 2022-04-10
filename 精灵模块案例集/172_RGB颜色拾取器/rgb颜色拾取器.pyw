"""
   RGB颜色拾取器,注意:在标题栏里显示的坐标是相对于计算机屏幕的,
   以左上角为原点的坐标,而不是虫子所在屏幕的坐标。
"""
import pyautogui
from ctypes import *
from sprites import *
from coloradd import *

screen = Screen()
screen.resizable()
screen.colormode(255)

c = (255,0,0)
ft1 = ('黑体',32,'normal')
ft2 = ('宋体',14,'normal')
bug = Sprite(visible=False,pos=(0,150))
bug.write('RGB颜色拾取器',align='center',font=ft1)
bug.goto(0,100)
bug.write('本程序可以全屏幕拾取像素点的RGB值',align='center',font=ft2)
bug.home()
bug.pensize(100)
bug.bk(180)
bug.pendown()
for x in range(360):
    bug.color(c)
    bug.fd(1)
    c = coloradd(c,1/360)
    
def get_color(x, y):
    """得到计算机屏幕x,y坐标某点的RGB颜色值"""
    gdi32 = windll.gdi32
    user32 = windll.user32
    hdc = user32.GetDC(None)  # 获取颜色值
    pixel = gdi32.GetPixel(hdc, x, y)  # 提取RGB值
    r = pixel & 0x0000ff
    g = (pixel & 0x00ff00) >> 8
    b = pixel >> 16
    return (r, g, b)

try:
    while True:
        x, y = pyautogui.position()
        c = get_color(x,y)
        info = "坐标:(" + str(x) + "," + str(y) + "),RGB值" + str(c) 
        screen.title(info)
        screen.update()
except KeyboardInterrupt:
    pass
