"""家乡的自我介绍.py"""
from turtle import Turtle,Screen
from time import sleep

def init_screen():
    """初始化屏幕对象并返回这个对象。 """
    screen = Screen()                   # 新建屏幕对象
    screen.title("家乡的自我介绍")      # 写上屏幕所在窗口的标题
    screen.setup(960,660)               # 设定屏幕的大小
    screen.bgpic("古风素材--122_.png")  # 设定背景图
    screen.delay(10)                    # 设定绘画延时
    return screen                       # 返回屏幕对象

def make_sprite(image,x,y):
    """显示女孩角色，参数说明：
    image：角色的造型图片,gif
    x,y：坐标
    """
    t = Turtle(visible=False)           # 新建不可见海龟对象
    t.penup()                           # 抬笔
    t.goto(-480,0)                      # 坐标定位
    t.shape(image)                      # 设定形状
    t.showturtle()                      # 显示
    t.goto(x,y)                         # 再次定位
    return t                            # 返回t

def draw_frame():
    """画box框的函数  """
    box_turtle = Turtle(visible=False)   # 画框的海龟对象
    box_turtle.penup()                   # 抬笔
    box_turtle.speed(0)                  # 让海龟的动作速度为最快
    box_turtle.screen.delay(0)           # 屏幕延时为0,为了画得快
    x1,y1 = (-400,-250)                  # 左上角坐标
    x2,y2 = (400,-320)                   # 右下角坐标
    width  = x2 - x1                     # box宽度
    height = y1 - y2                     # box高度
    box_turtle.setheading(0)             # 初始方向
    box_turtle.color("green")            # 颜色
    box_turtle.pensize(8)                # 笔迹宽度
    box_turtle.goto(-400,-250)            # 到左上角
    box_turtle.pendown()                 # 落笔
    for i in range(2):                   # 重复2次
        box_turtle.fd(width)             # 前进width个单位
        box_turtle.rt(90)                # 右转90度
        box_turtle.fd(height)            # 前进height个单位
        box_turtle.rt(90)                # 右转90度
    box_turtle.penup()                   # 抬笔
    box_turtle.screen.delay(10)          # 延时为10毫秒
    return box_turtle                    # 返回海龟对象
def say_sentence(t,sentence):
    """一个一个字的写文字，参数说明：
    t：海龟对象
    startpos：起始位置
    info：要写的文字
    """
    ziti = ("楷体",26,"normal")          # 设定字体样式
    t.goto(-300,-300)
    for word in sentence:                # 遍历字符串的每个字
        sleep(0.1)
        t.write(word,move=True,font=ziti)# 写一个字

if __name__ == "__main__":

    all_sentences = ["Hello，我是女生小黄。"]    
    all_sentences.append("我的家乡在江西的最西部,它的名字叫萍乡。")
    all_sentences.append("我家住在萍乡的安源区凤凰街。")
    all_sentences.append("我的家乡有武功山，孽龙洞等旅游景点。")
    all_sentences.append("我身后的公园叫鹅湖公园")
    all_sentences.append("欢迎到我家来作客,我一定会带你去玩的。")
    
    girl_image = "Fate_stay_night.gif"
    screen = init_screen()               # 新建屏幕对象
    screen.addshape(girl_image)          # 添加girl图形到屏幕

    sleep(1)
    girl = make_sprite(girl_image,0,0)   # 生成人物角色

    sleep(1)
    box_turtle = draw_frame()            # 画矩形框

    writer = Turtle(visible=False)       # 在框内写字的海龟对象
    writer.penup()                       # 抬笔
    writer.color("brown")                # 设定画笔颜色和填充为棕色

    sleep(1)
    for sentence in all_sentences:       # 遍历每句要说的话
        say_sentence(writer,sentence)
        sleep(1)
        writer.clear()
    box_turtle.clear()                   # 清除box框
    
    girl.goto(480,0)                     # 移到这个坐标
    girl.ht()                            # 让女孩消失
    screen.bye()                         # 关闭窗口
    
    
    



    
    
    
    
