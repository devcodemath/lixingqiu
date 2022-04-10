"""
   美人鱼与猫,这是一个动画,美人鱼从水底游出,看见小猫,希望小猫能和她一起游泳。
   
"""
from sprites import *

screen = Screen()           # 新建屏幕
screen.resizable()
screen.setup(480,360)       # 设定宽高
screen.title('美人鱼与猫by lixingqiu')
screen.bgpic('res/Underwater 1.png')

frames = ['res/mermaid-a.png','res/mermaid-b.png',
          'res/mermaid-c.png','res/mermaid-d.png']

girl = Sprite(shape=frames,pos=(-400,-400))
girl.stop = False           # 描述是否要切换造型的
def alt_costume():
    girl.nextcostume()
    if girl.stop == False:
       screen.ontimer(alt_costume,200)
    else:
       girl.shape('res/mermaid-b.png')
alt_costume()
    
girl.slide((400,400))
girl.hide()                 # 隐藏起来
girl.goto(-400,-400)
girl.scale(0.5)             # 一半大小
girl.show()                 # 显示出来 
screen.bgpic('res/Pool.png')
girl.slide((0,-100))
girl.stop = True

# 小猫出现
cats = [f"cats/{i}.png" for i in range(16)]
cat = Sprite(shape=cats,visible=False,pos=(300,0))
cat.scale(0.1)
cat.rotatemode(1)
cat.right(180)
cat.show()
cat.play('喵.wav')
for x in range(30):
    cat.fd(5)
    cat.nextcostume()
    cat.wait(0.1)
cat.shape('cats/9.png')    # 站立造型
girl.saycolor('yellow')
girl.say('可爱的小猫咪,\n过来和我一起游泳吧',5)
cat.play('喵.wav')
cat.saycolor('cyan')
cat.say('可以啊')

screen.mainloop()

