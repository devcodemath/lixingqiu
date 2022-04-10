"""
   淡入淡出.py   
   本程序演示了如何设定角色的透明度。
   需要角色的造型为一张图片。
   
"""
from sprites import * 
    
width,height = 480,360
screen = Screen()
screen.setup(width,height)
screen.bgpic("tree.png")
screen.title("淡入淡出姑娘by李兴球")

filename = '姑娘.png' 

maid = Sprite(visible=False,shape=filename)
screen.onmousemove(maid.goto)     # 角色跟随鼠标指针
maid.show()                       # 显示角色

maid.setalpha(150)                # 0为全透明，255为不透明

while 1:
    for alpha in range(255,-1,-1):
        maid.setalpha(alpha)
    for alpha in range(0,256):
        maid.setalpha(alpha)



