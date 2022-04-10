from sprites import *

width,height = 470,734
screen = Screen()
screen.tracer(0,0)
screen.title("雪花帘子")
screen.bgpic("girl.png")
screen.setup(width,height)

amounts = 18
snow = Sprite('snow.gif',visible=False)

snows=[snow]
for x in range(amounts-1):
    snows.append(snow.clone())

for i in range(amounts):
    snows[i].goto(-220 + i * 20,400)
    snows[i].show()
    
while 1:
    for snow in snows:
        item = snow.stamp()        
        for st in snow.stampItems:
            snow.stampmove(st,0,-30)
            left,top,right,bottom = snow.bbox(st)
            if bottom < -380: snow.clearstamp(st)
        snow.fd(5)
        if snow.xcor() > 250:snow.setx(-220)
       
    screen.update()
 



