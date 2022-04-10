"""
   猫与蟹的对话.py
   
   pip install sprites --user
   
"""

from sprites import *

width,height = 480,360
screen = Screen()    
screen.bgcolor("dodger blue")
screen.bgpic("tree.png")
screen.setup(width,height)
screen.title('猫与蟹的对话')
 
images = ['res/cat1.png','res/cat2.png']
index = 0
cat = Sprite('res/cat1.png')
cat.saycolor('cyan')
cat.saybordercolor('red')
cat.setx(-300)
cat.sety(-100)
cat.play('喵.wav')

def out():
  global index
  screen.onkeypress(None,'space')  
  cat.setx(-300) 
  for x in range(20):
    cat.fd(10)        
    cat.shape(images[index])
    index  = 1 - index
    time.sleep(0.1)
  cat.say('我从Scratch舞台来到了\nPython海龟画图屏幕',10,False)
  screen.onkeypress(out,'space')                      

screen.onkeypress(out,'space')
screen.listen()

im2 = ['crab1.png','crab2.png']
crab = Sprite('crab1.png')
crab.saycolor('yellow')
crab.left(90)
i2 = 0
crab.goto(100,-100)
# 下面每隔100毫秒切换螃蟹的造型
def crabanimation():
    global i2
    crab.shape(im2[i2])
    i2  = 1 - i2
    screen.ontimer(crabanimation,100)
crabanimation()
crab.say("请按空格键",10)

screen.mainloop()
 

    
