"""
  逐渐显图姑娘.py
  本程序会慢慢的把一位姑娘的图形显示出来,然后有箭头指示相关文字。
  但是，这并不是我女朋友哦，图片是从网上下载的。
"""
from sprites import *

PlaySound('faded.wav',SND_ASYNC)

im = Image.open('th.png')
screen = Screen()
screen.colormode(255)
screen.bgpic("1.png")

screen.setup(480,698)
right = im.width/2
left = -im.width/2
top = im.height/2
w = Sprite(visible=False)

for r in range(im.height):
    screen.tracer(0)
    for c in range(im.width):
       pixel = im.getpixel((c,r))
       #print(pixel)
       if len(pixel)==4:
          if pixel[3] == 0 :continue
       x = left + c
       #x = right -c
       y = top - r
       w.goto(x,y)
       w.dot(1,pixel[:3])
    screen.tracer(1)
    time.sleep(0.15)

p = Sprite(shape='pointer',visible=False,pos=(100,100))
p.color('white')
p.setheading(225)
for x in range(6):
    p.show()
    p.write("my girl friend",font=('黑体',14,'normal'))
    p.wait(0.6)
    p.hide()
    p.clear()
    p.wait(0.6)
p.clear()

p.goto(-100,100)
p.setheading(-45)
for x in range(6):
    p.show()
    p.write("今天是你的生日",align='right',font=('黑体',14,'normal'))
    p.wait(0.6)
    p.hide()
    p.clear()
    p.wait(0.6)
p.clear()


p.goto(0,150)
p.setheading(-90)
for x in range(6):
    p.show()
    p.write("祝你生日快乐",align='center',font=('黑体',14,'normal'))
    p.wait(0.6)
    p.hide()
    p.clear()
    p.wait(0.6)
p.clear()
 
w.home()
w.shape('th.png')
w.rotatemode(2)
w.show()
w.clear()
w.setheading(90)
for x in range(8):
    girl = w.stamp()
    
    
while True:
    w.clearstamps(1)
    w.fd(4)
    w.stamp()
    w.bounce_on_edge()
    time.sleep(0.1)
