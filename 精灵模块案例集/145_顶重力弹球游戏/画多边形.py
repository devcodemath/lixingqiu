from sprites import *

bug = Sprite(pos=(0,-100))
bug.pencolor('red')
bug.fillcolor('blue')
p2 = (200,0)
p3 = (200,100)
p4 = (0,100)
p5 = (-100,0)
item = bug.polygon((p2,p3,p4,p5))
print('多边形编号为:',item)
bug.goto(-100,-200)
item2= bug.arc(100,0,359)
print('饼状图的编号为:',item2)

