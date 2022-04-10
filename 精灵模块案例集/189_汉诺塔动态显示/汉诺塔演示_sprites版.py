"""
   汉诺塔演示程序.py
   本程序需要sprites模块支持,请用cmd命令打开管理员窗口并且输入以下进行安装:
   pip install sprites
"""
import time
from sprites import Sprite ,Screen,txt2image

__author__ = '李兴球'
__date__ = '2021/12/1'
__blog__ = 'www.lixingqiu.com'

N = 2                                 # n个盘子 
SPEED = 5                             # 全局速度
stack = []
def _custom_setup(self,p=[]):
    if p:
      self.speed(0)
      self.stackid = 0
      self.shapesize(1,p[0])
      self.color('brown','blue')      
Sprite.custom_setup = _custom_setup

def _rise(self):
    """上升"""
    while self.ycor() < 240:self.addy(0.1*SPEED)
    self.wait(0.2*(1/SPEED))    
Sprite.rise = _rise

def _fall(self):
     """下降"""
     if stack[self.stackid]:
           pz = stack[self.stackid][-1]    # 即将下落的stack的最上面的盘子的y坐标
           y = pz.ycor()
     else:
           y = -20
     while self.ycor() > y+20: self.addy(-0.1 * SPEED)
Sprite.fall = _fall

class Stack(list):
    """装盘子的"""
    def __init__(self, values=[],x=0,y=0):
        list.__init__([])
        self.x = x
        self.y = y
        self.extend(values)
        for pz in values:               # 每一个盘子
            pz.goto(x,y)
            y = y + 20
            pz.show()

def hanota(n,a,b,c):
    """把n个盘子从a经过b移到c"""    
    if n>1:       
        hanota(n-1,a,c,b)
        hanota(1,a,b,c)
        hanota(n-1,b,a,c)
    else:
        print(a,'->',c)
        plate = stack[a].pop()
        plate.rise()                      # 盘子升起
        plate.stackid = c                 # 修改盘子所在的stack的id
        plate.slide(stack[c].x,delay=2000*(1/SPEED))   # 设定盘子到所在的stack同一x坐标,平移时y坐标不变
        plate.setx(stack[c].x)             # 校准坐标
        plate.wait(0.2*(1/SPEED))
        plate.fall()                      # 盘子下落
        stack[c].append(plate)            # 把盘子装在编号为c的stack里

def make_plates(n):
    """制作n个盘子放到列表中,不要太多了!!!"""
    plates = []
    for length in range(1,n+1):
        p = Sprite(shape='square',visible=False)
        p.custom_setup([length])
        plates.insert(0,p)               #  要让前面的盘子更大所以用插入0号索引
    return plates

def destory_plates(N):
    global stack
    if len(stack)==0:return   
    for pz in stack[2]: pz.kill()
    stack = []
        
def draw_line():
    # 画一根横线和三根竖线
    dummy = Sprite(visible=False)
    dummy.pensize(2)
    dummy.color('gray')
    dummy.sety(-10)
    dummy.pendown()
    dummy.bk(300)
    dummy.fd(600)
    dummy.bk(150)
    dummy.left(90)
    dummy.fd(220)                       # 升220
    dummy.bk(220)                       # 降220
    dummy.left(90)
    dummy.fd(150)
    dummy.right(90)
    dummy.fd(220)
    dummy.bk(220)
    dummy.left(90)
    dummy.fd(150)
    dummy.right(90)
    dummy.fd(220)

def panzi_zenjia(x,y,pz_n):
    global N
    N = N + 1
    N = min(10,N)
    pz_n.clear()
    pz_n.write(N,font=('',16,'normal'))
    
def panzi_jianshao(x,y,pz_n):
    global N
    N = N - 1
    N = max(1,N)
    pz_n.clear()
    pz_n.write(N,font=('',16,'normal'))

def sd_zenjia(x,y,sd_n):
    global SPEED
    SPEED = SPEED + 1
    SPEED = min(20,SPEED)
    sd_n.clear()
    sd_n.write(SPEED,font=('',16,'normal'))
    
def sd_jianshao(x,y,sd_n):
    global SPEED
    SPEED = SPEED - 1
    SPEED = max(1,SPEED)
    sd_n.clear()
    sd_n.write(SPEED,font=('',16,'normal'))  
    
def display_operation():
    pz_w = Sprite(visible=False,pos=(-200,-100))
    pz_w.write('盘子数:')
    
    pz_n = Sprite(visible=False,pos=(-130,-100))
    pz_n.write(N,font=('',16,'normal'))
    
    txt2image('增加','res/zj.png')
    pz_add = Sprite(shape='res/zj.png',pos=(-80,-90))
    pz_add.onclick(lambda x,y:panzi_zenjia(x,y,pz_n))
    
    txt2image('减少','res/js.png')
    pz_sub = Sprite(shape='res/js.png',pos=(-30,-90))
    pz_sub.onclick(lambda x,y:panzi_jianshao(x,y,pz_n))

    
    sd = Sprite(visible=False,pos=(-220,-150))
    sd.write('全局速度:')    
    
    sd_n = Sprite(visible=False,pos=(-130,-150))
    sd_n.write(SPEED,font=('',16,'normal'))
    
    txt2image('增加','res/zjsd.png')
    sd_add = Sprite(shape='res/zjsd.png',pos=(-80,-140))
    sd_add.onclick(lambda x,y:sd_zenjia(x,y,sd_n))
    
    txt2image('减少','res/jssd.png')
    sd_sub = Sprite(shape='res/jssd.png',pos=(-30,-140))
    sd_sub.onclick(lambda x,y:sd_jianshao(x,y,sd_n))

    txt2image('开始演示','res/begin0.png',fontsize=30)
    txt2image('演 示 中...','res/begin1.png',fontsize=30,color=(128,127,122))
    begin_button = Sprite(shape=['res/begin0.png','res/begin1.png'],pos=(-100,-200))

    addsubbiao = [pz_add,pz_sub,sd_add,sd_sub]
    begin_button.onclick(lambda x,y:start_demo(x,y,begin_button,addsubbiao))

def start_demo(x,y,begin_button,addsubbiao):
    global stack
    
    [b.hide() for b in addsubbiao]
    begin_button.onclick(None)
    begin_button.shape('res/begin1.png')
    
    destory_plates(N)             # 销毁以前的stack3中的N个盘子
    plates = make_plates(N)
    stack1 = Stack(plates,-150)   # 最左边的stack有n个盘子,最下面的是最长的            
    stack2 = Stack([])
    stack3 = Stack([],150)
    stack.extend([stack1,stack2,stack3])
    begin_button.wait(2)
    hanota(N,0,1,2)               # 0,1,2,分别表示3个stack的索引号     
    begin_button.shape('res/begin0.png')
    begin_button.onclick(lambda x,y:start_demo(x,y,begin_button,addsubbiao)) # 重新绑定,可以开始单击了
    [b.show() for b in addsubbiao]
    
def main():
    w = Sprite(visible=False,pos=(0,250))
    w.write("汉诺塔演示程序",align='center',font=('楷体',22,'underline'))
    draw_line()                  # 画线条  
    display_operation()
    w.screen.mainloop()
    
if __name__ == "__main__":

    main()
