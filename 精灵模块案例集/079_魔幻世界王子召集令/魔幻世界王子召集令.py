"""
   魔幻世界王子召集令 .
   魔幻世界的王子非常想念他的小老虎们。
   他召集起来，要清点一下它们的数量。
   请按空格键让小老虎们报数吧。
   
"""
from sprites import *

screen = Screen()
screen.bgcolor('dodger blue')
screen.title('魔幻世界王子召集令')

prince = Sprite(shape='王子.png',pos=(250,-100))
prince.saycolor('white')
prince.say("按空格键让我的老虎们报数")

rows = 3
cols = 5
tigers = []
for r in range(rows):
    for c in range(cols):
        x = -280 + c * 100
        y = 150 - r * 200
        s = Sprite(shape='tiger.png',pos=(x,y))
        s.saycolor('yellow')
        tigers.append(s)

def countoff():
    """报数"""
    screen.onkeypress(None,"space")
    for index in range(len(tigers)):
        ti = tigers[index]
        ti.say(str(index+1),1)
    screen.onkeypress(countoff,"space")
        
screen.onkeypress(countoff,"space")

screen.listen()

screen.mainloop()
