from turtle import Turtle,Screen
from time import sleep
from random import choice
import sys

def init_screen(width,height,title,picture):
    """新建屏幕对象，参数说明：
    width：宽度
    height：高度
    title：标题
    picture：背景图(png)
    """
    screen = Screen()
    screen.title(title)
    screen.setup(width,height)
    screen.bgpic(picture)
    screen.delay(0)
    return screen

def make_sprite(image,x,y):
    """显示角色，参数说明：
    image：角色的造型图片,gif
    x,y：坐标
    """
    t = Turtle(visible=False)
    t.penup()
    t.shape(image)
    t.goto(x,y)
    t.showturtle()

def draw_frame(t,startpos,endpos,thickness,color):
    """画框，根据起点和终点画一个长方形,参数说明：
    t：海龟对象
    startpos：起始坐标
    endpos：结束坐标
    thickness：比触宽度
    color：颜色
    """
    x1,y1 = startpos
    x2,y2 = endpos
    width  = x2 - x1
    height = y1 - y2
    t.setheading(0)
    t.color(color)
    t.pensize(thickness)
    t.goto(startpos)
    t.pendown()
    for i in range(2):        
        t.fd(width)
        t.rt(90)
        t.fd(height)
        t.rt(90)
    t.penup()
def say_sentence(t,startpos,sentence):
    """写文字，参数说明：
    t：海龟对象
    startpos：起始位置
    info：要写的文字
    """
    t.goto(startpos)
    for word in sentence:
        sleep(0.1)
        t.write(word,move=True,font=("楷体",20,"normal"))

def answer(words):
    
    if "你好" in words : say_sentence(write_turtle,startpos,choice(hellos));return

    if "名字" in words : say_sentence(write_turtle,startpos,choice(answer_names));return

    if "玩" in words : say_sentence(write_turtle,startpos,choice(answer_play));return

    if "qq" in words : say_sentence(write_turtle,startpos,choice(answer_qq));return

    if "微信" in words : say_sentence(write_turtle,startpos,choice(answer_weixin));return
    
    if "飞行" in words : say_sentence(write_turtle,startpos,choice(answer_fly));return

    if "跳" in words : say_sentence(write_turtle,startpos,choice(answer_jump));return
        

    say_sentence(write_turtle,startpos,"不太明白你的意思，宝宝还小嘛");return
    
if __name__ == "__main__":

    hellos = ["你也好","How are you","Hi,我是机器人9号","Hi there！"]
    answer_names = ['My name is whitedog','我的名字是小白','我叫白居易','我是Mr White']    
    answer_play = ['会啊','这是我最拿手的','想玩什么?','好哇']  
    answer_qq = ['qq游戏最好玩了','qq是1234567','qq啊，我玩qq空间。']
    answer_weixin = ['我也常玩微信呢','机器人已经内置微信功能了','微信已经被淘太了。']
    answer_fly = ['这个功能科学家还在开发中。','我不能飞。','你看我这样子像能飞的吗?']    
    answer_jump = ['宝宝不会跳哟。','我不能跳。','你看我这样子像能跳的吗?']
    
    title = "和电脑对话"
    screen_width,screen_height = 800,450
    back_image = "公园背景.png"
    sprite_image = "机器人.gif"
    
    words = sys.argv[1:]
    if words == [] :
        print("用法：play.py 你好")
        sys.exit(0) 

    screen = init_screen(screen_width,screen_height,title,back_image)
    screen.addshape(sprite_image)
    screen.update()

    sleep(0.3)
    make_sprite(sprite_image,-60,-50)                           #生成人物角色

    sleep(0.3)
    frame_turtle = Turtle(visible=False)                        #画框的海龟对象
    frame_turtle.penup()
    draw_frame(frame_turtle,(-350,-150),(350,-200),4,"cyan")    #画矩形，从左上角到右下角，8笔触大小，颜色。

    write_turtle = Turtle(visible=False)                        #在框内写字的海龟对象
    write_turtle.penup()
    write_turtle.color("black")

    sleep(0.3)

    words = words[0]
    startpos = (-320,-190)                                      #起始坐标

    answer(words)                                               #回答
     
    screen.exitonclick()
    
    
    



    
    
    
    
