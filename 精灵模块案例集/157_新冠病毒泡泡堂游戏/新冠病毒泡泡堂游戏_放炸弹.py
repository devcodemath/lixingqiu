from sprites import * 

def draw_frame(obj,margin):
    """用obj角色画边框,margin为边距
       本函数用for循环直接画一个正方形也可以。
    """
    sw = obj.screen.window_width()
    sh = obj.screen.window_height()
    bug.topleft()            # 移到左上角
    bug.addy(-margin)   
    x,y = bug.position()  
    cors = [(x+sw,y),(x+sw,y+margin),(x,y+margin)]
    f1 = bug.polygon(cors)
    
    bug.bottomleft()         # 移到左下角      
    x,y = bug.position()  
    cors = [(x+sw,y),(x+sw,y+margin),(x,y+margin)]
    f2 = bug.polygon(cors)
    
    bug.addy(margin)    
    x,y = bug.position()  
    cors = [(x+margin,y),(x+margin,y+(sh-2*margin)),(x,y+(sh-2*margin))]
    f3 = bug.polygon(cors)

    bug.addx(sw-margin)    
    x,y = bug.position()  
    cors = [(x+margin,y),(x+margin,y+(sh-2*margin)),(x,y+(sh-2*margin))]
    f4 = bug.polygon(cors)
    return [f1,f2,f3,f4]

def draw_cross(obj,length):
    """画十字架"""
    d = length/2
    bug.goto(-d,d)
    x,y = bug.position()
    cors = [(x+length,y),(x+length,y+2*length),(x,y+2*length)] 
    p1 = bug.polygon(cors)

    bug.goto(-d-2*length,-d)
    x,y = bug.position()
    cors = [(x+5*length,y),(x+5*length,y+length),(x,y+length)] 
    p2 = bug.polygon(cors)
    
    bug.goto(-d,-d-2*length)    
    x,y = bug.position()
    cors = [(x+length,y),(x+length,y+2*length),(x,y+2*length)] 
    p3 = bug.polygon(cors)
    return [p1,p2,p3]
    
def draw_squares(obj,length):
    """画4个正方形"""
    items = []
    for _ in range(4):
        i = bug.polygon(4,length)
        items.append(i)
        bug.fd(length*5)
        bug.rt(90)
    return items

width = 800
height = 600
screen = Screen()
screen.bgcolor('black')
screen.setup(width,height)

bomb = Sprite('bombs',visible=False)
bomb.scale(0.5)

w = 100
bug = Sprite(visible=False)
bug.color('pink','pink')
items1 = draw_frame(bug,w/2)      # 画紧挨着屏幕的边框
items2 = draw_cross(bug,w/1.5)    # 画十字架
bug.goto(-w/2 - w,w/3 + w)
items3 = draw_squares(bug,w/1.5)  # 画四个正方形
items1.extend(items2)
items1.extend(items3)
print(items1)                    # items1是障碍物列表的项目编号
bug.goto(100,100)
leftkey = Key('Left')
rightkey = Key('Right')
upkey = Key('Up')
downkey = Key('Down')
spacekey = Key('space')

screen.listen()
clock = Clock()
bug.show()

allow = True
counter = 0
def check_bomb():
    global counter,allow
    if bomb.isvisible():
        if counter == 0 :
            screen.ontimer(check_bomb,1000)
            counter += 1
        elif counter < len(bomb._costumes):
           bomb.nextcostume()          
           if counter < 3:
               screen.ontimer(check_bomb,1000)               
           else:
               screen.ontimer(check_bomb,100)           
           counter += 1
        elif counter == len(bomb._costumes):
           bomb.hide()
           allow = True
           counter = 0
           screen.ontimer(check_bomb,100)
    else:
        screen.ontimer(check_bomb,100)
check_bomb()

while 1:    
    if leftkey.down():
        bug.setheading(180)
        bug.fd(5)
        if bug.overlap_with(items1):bug.bk(5)
    if rightkey.down():
        bug.setheading(0)
        bug.fd(5)
        if bug.overlap_with(items1):bug.bk(5)
    if upkey.down():
        bug.setheading(90)
        bug.fd(5)
        if bug.overlap_with(items1):bug.bk(5)
    if downkey.down():
        bug.setheading(-90)
        bug.fd(5)
        if bug.overlap_with(items1):bug.bk(5)
    if spacekey.down() and allow == True :
        print('放炸弹')
        bomb.goto(bug.position())
        bomb.shapeindex(0)
        bomb.show()
        allow = False
    
 
    
    screen.update()
    clock.tick(60)










