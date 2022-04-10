"""在海龟画图中通过canvas画圆形.py"""
from turtle import Screen 
 
width,height = 800,600

screen = Screen()                           # 生成屏幕对象
screen.setup(width,height)
screen.setworldcoordinates(0,height,width,0)# 坐标转换以左上角为原点
screen.delay(0)
 
canvas = screen.cv                          # 获取画布对象 
bbox = (100,100,200,200)                    # 圆形的左上角和右下角坐标
circle_id = canvas.create_oval(bbox,fill='green',outline='green')
screen.onclick(lambda x,y:print(int(x),int(y)))
screen.mainloop()
