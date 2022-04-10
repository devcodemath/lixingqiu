"""
   趣味正方形.py
   画个正方形后,单击它会移动,并且碰到边缘就反弹。
   这个版本采用画布的move命令让'当前线条项目'移动实现的。
   也可以用纯动画原理实现，还能用自定义造型来实现。
"""
import time
import turtle

sw,sh = 480,360
turtle.shape('turtle')                                # 设定海龟造型
turtle.bgcolor('white')                               # 设定背景颜色 
turtle.color('blue')                                  # 设置海龟颜色
turtle.pensize(2)                                     # 设置画笔尺寸
turtle.setup(sw,sh)                                   # 设置窗口宽高
for _ in range(4):
    turtle.fd(100)
    turtle.lt(90)

square = turtle.getturtle().currentLineItem           # 当前线条项目 
canvas = turtle.getcanvas()                           # 得到画布
turtle.color('red')                                   # 设定海龟颜色
turtle.write('请单击',align='center',font=('',16,'underline'))

def gogogo(event):
    turtle.ht()
    dx = 5
    dy = 5     
    canvas.unbind("<Button-1>")
    while True:
        canvas.move(square,dx,dy)                     # 移动square
        cors =  canvas.coords(square)                 # 获取square每个点坐标 
        xcors = [cors[i] for i in range(len(cors)) if i%2==0]
        ycors = [cors[i] for i in range(len(cors)) if i%2==1]
        min_x = min(xcors)                            # 最小x坐标
        max_x = max(xcors)                            # 最大x坐标
        min_y = min(ycors)                            # 最小y坐标
        max_y = max(ycors)                            # 最大y坐标
        #print(min_x,max_x,min_y,max_y)
        if max_x >= sw//2 or min_x <= -sw//2:dx = -dx # 碰到左右边就反弹
        if max_y >= sh//2 or min_y <= -sh//2:dy = -dy # 碰到上下边就反弹         
        time.sleep(0.01)                              # 等待0.01秒 
        canvas.update()                               # 画布更新 
        
canvas.bind("<Button-1>",gogogo)                      # 绑定左键到gogogo

screen = turtle.getscreen()
screen.mainloop()

    







