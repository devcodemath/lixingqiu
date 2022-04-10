"""
   sprites.py
   
   一、简介：
   
       本模块命令名为精灵模块，或叫角色模块。本模块已经上传到了pypi网站，通过在cmd窗口下输入pip install sprites即可安装使用。
       精灵模块主要提供继承自Turtle的Sprite类。重定义了Turtle模块中的一些方法和属性。
   由于要旋转图形，所以需要PIL模块和numpy模块支持。默认的精灵对象是抬笔的，内置16张图片。 分别是：ball.png，bug.png，
   b1.png,b2.png,cat1.png，cat2.png，bee.png，flower.png，explosion0.png,explosion1.png，fighter.png，
   thunder.png，sky.png，ufo.png,rat1.png,rat2.png。它们存在于_built_in_images列表中。在本模块第一次运行后，这些图片会释放
   到当前工作目录的res文件夹。本模块设计为教育目的，可用来做入门动画与游戏。
 
   二、Sprite类主要提供了以下功能：
   
   1、角色可直接拖动(compound造型不支持)。
   2、提供像Scratch中的三种旋转模式。精灵对象的_rotatemode属性值为0，代表可360度旋转,为1时代表可左右翻转,为2时角色不会旋转。
   3、rotatemode：返回或设置旋转模式。   
   4、addx：x坐标增加,方便编程。
   5、addy：y坐标增加,方便编程。
   6、scale：缩放角色造型，只有一个参数。
   7、gotorandom：到随机位置。这个命令提供了5个别名,randompos、randomposition 、random_pos、random_position、goto_random 
   8、heading：重定义了这个方法，不带参数能获取当前朝向值。带参数参让角色朝向某对象或坐标,也就是能设置方向了。
   9、show：显示对象，带参数时让角色显示一定的时间后又会隐藏，异步执行。
   10、hide：隐藏对象，带参数时让角色隐藏一定的时间后又显示，异步执行。
   11、move：在水平和垂直方向上移动角色的命令。
   12、collide：和另一个角色或图章的碰撞方法，采用的是矩形碰撞，可以有scale参数，表示缩放绑定盒子，如scale=0.5时，绑定盒宽高各缩一半。
   13、collidemouse：检测角色有没有碰到鼠标指针,别名是collide_mouse。
   14、collide_edge：检测角色有没有碰到边缘检测。
   15、bounce_on_edge：碰到边缘就反弹，适合于用fd命令让角色前进后再使用。
   16、bbox：获取角色绑定盒，通过指定id号,也可获取图章的绑定盒。
   17、randomcolor：设定角色为随机一种较鲜艳的颜色。
   18、randomheading：设定角色为随机一个方向。
   19、remove：移除方法,把自己从屏幕的_turtles列表中删除，并根据item号删除自己在画布上的形状，清除说话泡泡对象,别名是kill和destroy。
   20、stamp：重定义了Turtle类的图章方法，新增的参数可以让图章在一定时间后自动被清除，异步执行。
   21、stampmove：移动图章的命令,角色可根据图章编号来在水平和垂直方向上移动图章，这样方便了制作动态背景。
   22、stampgoto：可以让图章到指定坐标的命令。
   23、stampcors：根据图章编号,获取图章的坐标。
   24、stampbbox：根据图章编号,获取图章的绑定盒。
   25、stampcollide：图章和另一个图章或精灵对象的碰撞检测。   
   26、play：播放方法，目前只支持播放无损压缩的wav音频文件，支持显示歌词。
   27、setalpha：设置透明度方法。参数为从0到255的数值。0代表完全透明，255代表不透明，128代表半透明。
       对于polygon和compound造型来说，0代表透明，非0代表不透明。对于image来说，设置角色的透明度从0到255的值就会产生从透明到不透明的渐变效果。
   28、getalpha：得到透明度，返回从0到255的整数。
   29、set_tag：设置角色的标签。它是一个字符串，用于分组,方便一些游戏的编程。
   30、get_tag：获取角色的标签。
   31、say：说话方法，会在角色上面显示说话气泡。默认时间为2秒，默认会阻塞进程。
   32、saycolor：返回或设置说话的字的颜色。
   33、saybordercolor：返回或设置说话泡泡的边框颜色。   
   34、write：重定义写方法，增加angle参数，可以写斜字，默认为黑体，12号。
   35、reborn：“重生”方法，让角色隐藏后在另一坐标重新显示。复用角色之用，可加delay参数，意为在一定的时间后才显示，异步执行。
   36、nextcostume：下一个造型，别名是nextshape。
   37、previouscostume：上一个造型，别名是previousshape。
   38、costumeindex：指定造型编号，别名是shapeindex。
   39、update：单独更新(重绘)角色,(屏幕也有这个方法,但会重绘所有角色。)
   40、wait：方法，等待一定的时间，以秒为单位,默认等待0.01秒。在等的过程中会不断刷新屏幕。
   41、slide：滑行命令，在一定时间滑行到某坐标，别名是glide。
   42、draw_grid：指定格子宽度和高度画格子命令，它会在屏幕上铺满格子。
   43、draw_grid2：画格子2命令，指定行数、列数、格子宽度、格子高度画格子。
   44、draw_grid3：画格子3命令，指定行数、列数、格子宽度、格子高度、是否盖图章，并且角色当前方向来画格子的方法。
   45、stampslide：图章滑行命令，别名为stampglide
   46、hidestamp：隐藏图章命令，别名为stamphide。
   47、showstamp：显示图章命令，别名为stampshow。
   48、stampishide：判断图章是否隐藏命令。
   49、wander： 在屏幕内漫游，它是gotorandom的慢版。
   50、ishide：返回角色是否是隐藏的。
   51、write2：用来写有阴影的字，有前景bg和fg参数，默认为中间对齐，宋体16号字。
   52、find_overlapping：查找重叠命令。本命令用来查找有无和角色的矩形重叠的项目(包括画笔线条，圆点，多边形，圆弧，填充区域，图章，其它角色)，可以有一个参数，叫排除参数。本命令返回找到的项目编号集合。
   53、overlap_with：重叠命令。本命令有一个参数，它会查找和这个参数对应的项目有无重叠。（包括线条，圆点，多边形，圆弧，图章，填充区域，其它角色)。它的参数可以是序列、整数与角色或字符串，返回重叠的所有项目编号。
   54、topleft：到左上角，返回坐标。
   55、topright：到右上角，返回坐标。
   56、bottomleft：到左下角，返回坐标。
   57、bottomright：到右下角，返回坐标。
   58、arc：画圆弧，实际上是一个派形图。参数为radius半径，start起始角，extent结束角，width线宽，fill填充颜色与outline边框颜色 ，返回项目编号。
   59、polygon：画多边形，以角色所在坐标为第一个点画多边形，参数为其它坐标列表，width线宽，fill填充颜色与outline边框颜色 ，返回项目编号。
   60、contained：返回完全包含在角色最小矩形内的所有项目编号集合。
   61、contain：判断角色完全包括另一个角色或项目编号，返回真或假。
   62、oval：产生椭形的方法，它会根据当前角色的方向而产生，即可产生斜的椭圆。
   63、oval2：产生椭圆的方法，不会根据当前角色的方向产生，即总是“正的”。
   64、setleft：设置角色的最左x坐标。
   65、setright：设置角色的最右x坐标。
   66、settop：设置角色的最上y坐标。
   67、setbottom：设置角色的最下y坐标。
   68、getleft：获取角色或项目编号的最左x坐标。
   69、getright：获取角色或项目编号的最右x坐标。
   70、gettop：获取角色或项目编号的最顶y坐标。
   71、getbottom：获取角色或项目编号的最底y坐标。
   72、pixelcollide：像素碰撞方法。用于两个角色之间的像素级别碰撞。返回碰撞点的坐标及两个角色在这个点的像素值及重叠区域矩形。
   73、draggable：设置角色为可拖放。要取消只要设置ondrag方法的值为None即可。
   74、saveshape：保存当前造型为图片，只支持image类型的角色。
   75、coloroverlap：角色造型图片上的颜色重叠检测命令，属于像素级碰撞命令。
   76、collidecolor：碰到颜色命令
   
   三、screen新增命令：
   
   在海龟画图中，屏幕的本质是继承自框架内的画布和滚动条。sprites模块中也一样，但是把屏幕放在了名为displayframe的框架中。
   当使用Screen()命令时,不加参数或参数1,则窗口还是和原来一样。displayframe组件就是tk组件(即窗口组件)。
   当使用Screen(2)时，新建的窗口会分为左右两大区，名称分别为leftframe和rightframe框架区。displayframe在leftframe区上面。
   当使用Screen(3)时，新建的窗口会分为上下两大区，名称分别为topframe和bottomframe区。displayframe在topframe区的左边。

   在sprites模块中，为了方便横版或竖版游戏的制作，让背景也能移动。
   
   以下是给屏幕增加的方法。   
   1、resizable：sprites模块默认窗口是不可变大小的，用这个命令能让窗口重新可缩放。
   2、onmousemove：即鼠标移动事件，需要定义一个函数绑定这个事件。
   3、onscreenrelease：鼠标松开事件，需要定义一个函数绑定它。
   4、move：在水平和垂直方向上移动背景图片。
   5、setx：设置背景图片的x坐标。
   6、sety：设置背景图片的y坐标。
   7、xcor：获取背景图片的x坐标。
   8、ycor：获取背景图片的y坐标。
   9、goto：设定背景图片的x,y坐标
   10、save：截屏，保存屏幕为图形对象或者为图片，屏幕需在最前面显示(不要最小化)。
   11、titlebar：是否要标题栏的命令，参数为False，不显示标题栏，反之显示。
   12、draggable：让窗口按住鼠标中键时可拖动。在没有标题栏时最好这样，要不然不方便了。
   13、addpopup：绑定右键菜单
   14、removepopup：移除绑定右键菜单
   
   四、给_Root类增加的方法
   1、position：获取窗体在计算机桌面上的x,y坐标，没有参数。
   2、goto：设置窗体在计算机桌面上的坐标，参数为x,y整数值。
   3、move：相对移动窗体，参数为dx,dy整数值，分别为水平与垂直单位移动距离。
   
   五、单独函数：

   1、makecolors：
   默认产生128种鲜艳的颜色，导入本模块后它会运行一次，产生一个_colorlist列表。

   2、mouse_pos：
   获取鼠标指针的坐标，和屏幕的xscale和yscale无关。
   它有5个别名,mouse_position、mouseposition、mousepos、getmousepos、getmouseposition。

   3、explode：
   产生爆炸效果的函数。需要传递坐标和序列帧图。它的别名是effect。

   4、txt2image：
   方便文字转图像的实用函数，这样就能把角色的造型设置成一个文字了。

   5、txt3image：把多行文本转换成图像文件或图形对象。
   
   6、txt4image：把文本文件转换成图像文件或图形对象。

   7、rect_overlap：返回两个矩形相交区域与面积。

   六、单独类：
   
   1、Key类：用来新建某个按键的实例，用于在循环中进行键盘按键检测。
   2、Mouse类：用来新建鼠标按键的实例，用于在循环中进行鼠标按键检测。
   3、Clock类：用来固定帧的时钟类，有tick方法和getfps方法。前者用来设置帧率，后者获取帧率。
   4、Group类：用来给角色分组的一个类，在实例化时需要加标签为参数。

   七、其它：
   新增屏幕的_focus属性，用来跟踪屏幕是否激活。
   
   注意以下问题：
   1、不支持复合图形的拖动。   
   2、tilt倾斜等变形命令不会对图形进行变形。
   3、如果用屏幕的tracer(0,0)关闭了自动渲染角色,那么在移动角色后要马上刷新屏幕,否则会出现意外效果。  
   原因是绑定盒命令得到的是先前没有刷新的角色的坐标，这样获取的不是最新坐标，当然会导致程序出意外。
   4、屏幕的update命令会重新渲染所有的角色，如果角色较多，反而会让程序运行更慢。
   5、本模块给RawTurtle类增加了update方法，这样能单独渲染一个角色。本模块已经把屏幕的自动绘画延时设为0及速度也设为最快了。
   6、其实Turtle模块可以支持png图片,但要像以下这样写:
   screen.addshape('scratch.png',Shape("image", screen._image('scratch.png')))
"""
__author__ = 'lixingqiu'
__date__ = '2021/12/29'
__blog__ = 'www.lixingqiu.com'

import os
import re
import sys
import math
import glob
import time
import base64
import random
import colorsys
import numpy as np
from io import BytesIO
from copy import deepcopy
from tkinter import filedialog
from tkinter import colorchooser
from winsound import PlaySound,SND_ASYNC,SND_LOOP,SND_PURGE
from PIL import ImageTk,ImageOps,Image,ImageGrab,ImageDraw,ImageFont
from turtle import TK,_Root,ScrolledCanvas,_CFG ,TNavigator,Tbuffer,TPen,_Screen,Screen,Turtle,Vec2D, RawTurtle,TurtleScreenBase,Shape,TurtleScreen,_TurtleImage,TurtleGraphicsError 

_VERSION = 1.44    # 1.44版修复了新建Screen时在某些计算机找不到cv的小错误,还有就是shapesize函数加了一行if,slide增加了if语句,增加了custom_setup方法.txt2image增加了bg参数
_CFG['delay'] = 0
# 定义资源文件夹
_resfld = os.path.join(os.getcwd(),'res')
if not os.path.exists(_resfld):os.mkdir(_resfld)

def _makerandomfilename(ext):
    """生成随机文件名"""
    s = 'abcdefghijklmnopqrstuvwxyz0123456789'
    t = time.localtime()
    year = str(t.tm_year)
    mon = str(t.tm_mon)
    day = str(t.tm_mday)
    minu = str(t.tm_min)
    sec = str(t.tm_sec)
    shijian = [year,mon,day,minu,sec]
    r = [random.choice(s) for _ in range(4)]
    shijian.extend(r)
    s = os.getcwd() + os.sep + "".join(shijian) + ext
    return s    
    
def _set_im_alpha(im,alpha):
    """im是用Image.open打开的转换成RGBA的图形对象。
       本函数设置im的透明度，但不像putalpha那样眉毛胡子一把抓似地
       把所有像素的透明度都设为alpha值(结果会有黑底)，而是只有不透明像素才设置。
       黑边问题待解决！
    """
    array = np.array(im)   
    a =  array[:,:,3:]        # 提取透明通道所有值
    a = np.where(a>0,alpha,0) # 如果透明度大于0,则设为alpha,否则为0    
    array[:,:,3:] = a         # 把array的透明度全部改为a
    return Image.fromarray(array)

# 重定义Tpen类的_reset方法,让精灵实例化时不落笔
def TPen_reset(self, pencolor=_CFG["pencolor"],
                 fillcolor=_CFG["fillcolor"]):
    self._pensize = 1
    self._shown = False
    self._pencolor = pencolor
    self._fillcolor = fillcolor
    self._drawing = False
    self._speed = 0
    self._stretchfactor = (1., 1.)
    self._shearfactor = 0.
    self._tilt = 0.
    self._shapetrafo = (1., 0., 0., 1.)
    self._outlinewidth = 1
TPen._reset = TPen_reset
        
# 重定义 Screen函数
def Screen(layout=1):
    """返回单一的屏幕对象，如果不存在，则建一个，最后返回这个对象"""
    if layout < 1 : layout = 1
    if Turtle._screen is None:
        Turtle._screen = _Screen(layout)
    return Turtle._screen

# 重定义Turtle类的初始化方法
def Turtle__init__(self,shape=_CFG["shape"],
                   undobuffersize=_CFG["undobuffersize"],
                   visible=_CFG["visible"]):
        if Turtle._screen is None:
            Turtle._screen = Screen(1)
        RawTurtle.__init__(self, Turtle._screen,shape=shape,
                           undobuffersize=undobuffersize,visible=visible)
Turtle.__init__ = Turtle__init__

# 重定义_Root类的初始化方法
def _Rootinit(self,layout=1):
    TK.Tk.__init__(self)
    self.layout = layout
    self.resizable(0,0)          # 关闭缩放
    if layout == 1 :             # 如果是布局1,直接把self.displayframe等于self
      self.displayframe = self
    elif layout ==2 :            # 左右布局模式
        self.leftframe = TK.Frame()                 # 左边的框架
        self.leftframe.pack(side=TK.LEFT,expand=1,fill='both')
        self.rightframe = TK.Frame()                 # 右边的框架
        self.rightframe.pack(side=TK.RIGHT,fill='both') # 新的组件可放在这框架中       
        self.displayframe = TK.Frame(self.leftframe)
        self.displayframe.pack(side=TK.TOP,expand=1,fill='both')
        self.bottomframe = TK.Frame(self.leftframe)
        self.bottomframe.pack(side=TK.BOTTOM)                    # 新的组件可放在这框架中
    elif layout ==3 :            # 上下布局模式
        self.topframe = TK.Frame()                   # 上边的框架
        self.topframe.pack(side=TK.TOP,expand=1,fill='both')
        self.bottomframe = TK.Frame()                 # 下边的框架
        self.bottomframe.pack(side=TK.BOTTOM,fill='both') # 新的组件可放在这框架中       
        self.displayframe = TK.Frame(self.topframe)
        self.displayframe.pack(side=TK.LEFT,expand=1,fill='both')
        self.rightframe = TK.Frame(self.topframe)
        self.rightframe.pack(side=TK.RIGHT)                    # 新的组件可放在这框架中
    
_Root.__init__ = _Rootinit

# 重定义setupcanvas,为的是不让当铺新的组件时,新的组件不在下面,而在它的右边。
def _redef_setupcanvas(self, width, height, cwidth, cheight):
    self._canvas = ScrolledCanvas(self.displayframe, width, height, cwidth, cheight)
    self._canvas.pack(side=TK.LEFT,expand=1,fill='both')
_Root.setupcanvas = _redef_setupcanvas

# 给root增加position获取坐标方法,注意坐标系是右下为正的
def _Rootposition(self):
    string = self.geometry()
    info = string.split('+')
    left = int(info[1])
    top = int(info[2])
    return left,top
_Root.position= _Rootposition

# 给root增加goto坐标定位方法,注意坐标系是右下为正的
def _Rootgoto(self,x,y):
    string = "+" + str(x) + "+" + str(y)    
    self.geometry(string)
_Root.goto = _Rootgoto
  
# 给root增加move方法,
def _Rootmove(self,dx,dy=0):
    """窗口的移动方法,注意坐标系是右下为正的"""
    left,top = self.position()   # 获取坐标    
    left = left + dx    
    top = top + dy    
    string = "+" + str(left) + "+" + str(top)    
    self.geometry(string)
_Root.move = _Rootmove

# 重定义原生海龟的初始化方法
def RawTurtle__init__(self, canvas=None,
             shape=_CFG["shape"],
             undobuffersize=_CFG["undobuffersize"],
             visible=_CFG["visible"]):
    if isinstance(canvas, _Screen):
        self.screen = canvas
    elif isinstance(canvas, TurtleScreen):
        if canvas not in RawTurtle.screens:
            RawTurtle.screens.append(canvas)
        self.screen = canvas
    elif isinstance(canvas, (ScrolledCanvas, Canvas)):
        for screen in RawTurtle.screens:
            if screen.cv == canvas:
                self.screen = screen
                break
        else:
            self.screen = TurtleScreen(canvas)
            RawTurtle.screens.append(self.screen)
    else:
        raise TurtleGraphicsError("bad canvas argument %s" % canvas)

    screen = self.screen
    TNavigator.__init__(self, screen.mode())
    TPen.__init__(self)
    screen._turtles.append(self)
    self.drawingLineItem = screen._createline()
    self.turtle = _TurtleImage(screen, shape)
    self._poly = None
    self._creatingPoly = False
    self._fillitem = self._fillpath = None
    self._shown = visible
    self._hidden_from_screen = False
    self.currentLineItem = screen._createline()
    self.currentLine = [self._position]
    self.items = [self.currentLineItem]
    self.stampItems = []
    self._undobuffersize = undobuffersize
    self.undobuffer = Tbuffer(undobuffersize)
    self._tag = 'turtle'       # 增加的属性,贴一个标签
    # 对于多边形和复合图形来说大于0的数都是不透明
    # 对于图像来说则是透明度,0为透明,255为不透明
    self._alpha = 255                  #  初始为不透明
    self._update()
    
RawTurtle.__init__ = RawTurtle__init__

# 给原生海龟增加slide，别名glide方法
def RawTurtle_slide(self,pos,delay=2000):
    """pos：x,y坐标,元组或者列表,如果不是这两个,则先处理一下
       delay：以毫秒为单位的滑行总时间
       在规定的时间内滑动到坐标，无返回值。
    """
    # 处理pos不是列表或者元组的情况
    if not isinstance(pos,(tuple,list)):# 不是列表或者元组,当成当一的x值
        pos = (pos,self.ycor())
    
    old_delay = self.screen.delay()     # 获取当前绘画延时时间
    self.screen.delay(0)
    delay = abs(delay)    
    if delay > 10:
      delay = int(delay)     
      h_distance = pos[0] - self._position[0]
      v_distance = pos[1] - self._position[1]
      dx = 10 * h_distance/delay              # 每毫秒在水平方向移动的距离
      dy = 10 * v_distance/delay              # 每毫秒在垂直方向移动的距离  
      for _ in range(delay//10):
        start = time.time()
        self.move(dx,dy)
        splent_time  = time.time() - start
        waited_time = 0.01 - splent_time
        if waited_time > 0: time.sleep(waited_time)      
    else:
        self.goto(pos)
    self.screen.delay(old_delay)
    
RawTurtle.slide = RawTurtle_slide
RawTurtle.glide = RawTurtle_slide

# 给原生海龟增加update方法，为的是能单独渲染一个角色
def RawTurtle_update(self):
    """重画自己"""
    tracing = self.screen._tracing
    self.screen._tracing = True
    self._update_data()
    self._drawturtle()
    self.screen._update()
    self.screen._tracing = tracing
RawTurtle.update = RawTurtle_update

# 重定义原生海龟的_drawturtle方法
def RawTurtle_drawturtle(self):
    """根据倾斜角度，伸展因子，重调模式等重新渲染海龟对象的外形。"""
    screen = self.screen
    shape = screen._shapes[self.turtle.shapeIndex]
    ttype = shape._type
    titem = self.turtle._item
    if self._shown and screen._updatecounter == 0 and screen._tracing > 0:
        self._hidden_from_screen = False
        tshape = shape._data
        if ttype == "polygon":
            if self._resizemode == "noresize": w = 1
            elif self._resizemode == "auto": w = self._pensize
            else: w =self._outlinewidth
            shape = self._polytrafo(self._getshapepoly(tshape))
            fc, oc = self._fillcolor, self._pencolor
            # 如果alpha值，即透明度为0，则没有填充颜色和线宽，这样就看不到海龟的外形了。
            # 但又把它“画”了出来，这样绑定盒命令就能获取正确的值。如果隐藏，就获取不到了。
            if self._alpha == 0 :
               fc = ""
               w = 0
               oc = ""
            screen._drawpoly(titem, shape, fill=fc, outline=oc,
                                                  width=w, top=True)
        elif ttype == "image":
            screen._drawimage(titem, self._position, tshape)
        elif ttype == "compound":
            for item, (poly, fc, oc) in zip(titem, tshape):
                poly = self._polytrafo(self._getshapepoly(poly, True))
                # 如果alpha值即透明度为0，则无填充颜色和线宽，这样就看不到海龟的外形了。
                if self._alpha == 0 :
                    screen._drawpoly(item, poly, fill="",
                                 outline=0, width=0, top=True)
                else:                  
                    screen._drawpoly(item, poly, fill=self._cc(fc),
                                 outline=self._cc(oc), width=self._outlinewidth, top=True)
    else:
        if self._hidden_from_screen:
            return
        if ttype == "polygon":
            screen._drawpoly(titem, ((0, 0), (0, 0), (0, 0)), "", "")
        elif ttype == "image":
            screen._drawimage(titem, self._position,
                                      screen._shapes["blank"]._data)
        elif ttype == "compound":
            for item in titem:
                screen._drawpoly(item, ((0, 0), (0, 0), (0, 0)), "", "")
        self._hidden_from_screen = True
RawTurtle._drawturtle = RawTurtle_drawturtle
            
# 给原生海龟对象增加move方法
def _move(self,dx=0,dy=0):
    """移动水平dx,垂直dy的距离"""
    x = self.xcor() + dx
    y = self.ycor() + dy
    self.goto(x,y)
    self._update()
RawTurtle.move = _move

# 给原生海龟增加stop方法,用于停止播放音乐
def RawTurtle_stop(self):
    """让正在播放的所有音乐停止"""
    PlaySound(None,SND_PURGE)
RawTurtle.stop = RawTurtle_stop

# 给原生海龟对象增加play方法
def RawTurtle_play(self,song_file,lrc_file=None,fontstyle=("",24,"normal"),loop=False ):
    """在海龟屏幕显示歌词并播放歌曲，本函数只支持无损wav文件。
       self：海龟对象或其子类的实例
       song_file：歌曲文件
       lrc_file：歌词文件，诸如：[00:00.00]月满西楼
                                 [01:00.12]红藕香残 玉簟秋
       上面这样的歌词文件。
       fontstyle为三元组，表示用write写字时的字体风格。
       loop:为假示不循环播放,为True表示循环播放
    """
    if loop == True:
        PlaySound(song_file, SND_ASYNC|SND_LOOP)# 异步循环播放音效
    else:
        PlaySound(song_file, SND_ASYNC)         # 异步播放音效
    if lrc_file==None:return                    # 无歌词文件则返回

    if not os.path.exists(lrc_file):
       print("歌词文件没有找到!")
       return
    f = open(lrc_file)                          # 打开歌词文件
    words_=f.readlines()                        # 读取歌词文件
    f.close()                                   # 关闭文件
    
    # 正则表达式检测歌词文件内容
    reg='\[\d\d:\d\d\.\d\d\]'
    result = re.findall(reg,"".join(words_))   # 如果有[00:00.33]这样的则会返回非空列表
    if not result:
       print("歌词文件貌似有问题!")
       return
     
    x,y = self.position()              # 歌词中央坐标
    fgcolor = self.pencolor()          # 歌词前景色 
    bgcolor = self.fillcolor()         # 歌词背景色
   
    words_list=[]                      # 歌词列表
    words_index=0                      # 歌词索引

    words_list=[ line.strip() for line in words_ if len(line)>1]
    words_lines=len(words_list)        

    def get_time_axis(index):
        """获取时间轴"""
        songtime=words_list[index]
        songtime=songtime.split("]")[0]
        songtime=songtime.split(":")
        songtimef=songtime[0][1:3]
        songtimef=int(songtimef)*60    
        songtimem=float(songtime[1])
        return int((songtimef+songtimem)*1000)
    
    words_index=0
    begin_time=time.time()
    def display_subtitle():
        """随着音乐显示歌词函数"""
        nonlocal words_index            # 歌词索引号
        nonlocal words_lines            # 歌词line数          
        current_time=time.time()
        running_time=(current_time-begin_time)*1000
        # 如果逝去的时间大于歌词文件中那个时间点就换歌词
        if running_time > get_time_axis(words_index):
            self.clear()
            display_words_=words_list[words_index].split("]")[1]
            self.goto(x,y)
            self.color(bgcolor)
            # 在左上一个单位印字
            self.write(display_words_,align='center',font=fontstyle)
            self.goto(x-1,y+1)
            self.color(fgcolor)
            self.write(display_words_,align='center',font=fontstyle)    
            words_index=words_index+1            
        if words_index < words_lines:        
            self.screen.ontimer(display_subtitle,100)
    # 调用显示标题的函数
    display_subtitle()
RawTurtle.play = RawTurtle_play

# 在turtle.py模块中,屏幕基类的_dot没有定义,这里把它定义完整
def TurtleScreenBase__dot(self,pos,size,color):
    """画点的屏幕基类方法"""
    radius = size/2
    x,y = pos
    x0,y0 = x - radius,-(y + radius)
    x1,y1 = x + radius, radius - y
    item = self.cv.create_oval(x0,y0,x1,y1,fill=color,width=0)
    return item
TurtleScreenBase._dot = TurtleScreenBase__dot

def __write(self, pos, txt, align, font, pencolor,angle):
    """
       用指定的颜色和字体在画布上写文本。返回文本项目和其绑定盒的右x-1坐标。
    """
    x, y = pos
    x = x * self.xscale
    y = y * self.yscale
    anchor = {"left":"sw", "center":"s", "right":"se" }
    item = self.cv.create_text(x-1, -y, text=txt, anchor=anchor[align],
                               fill= pencolor, font=font,angle=angle)
    x0, y0, x1, y1 = self.cv.bbox(item)
    self.cv.update()
    return item, x1-1
TurtleScreenBase._write = __write

def _write(self,txt,align,font,angle=0):
    """海龟的write的预定义方法
    """
    item, end = self.screen._write(self._position, txt,
                                   align, font,self._pencolor,angle)
    self.items.append(item)
    if self.undobuffer:
        self.undobuffer.push(("wri", item))
    return item,end                 # 本来只返回end,这里增加了item

def _writea(self, arg, move=False, align="left", font=("黑体",12,"normal"),angle=0):
    """在海龟的当前坐标写文本。
    参数:
    arg -- 要写在海龟画图屏幕上的信息,
    move (可选) -- True/False,
    align (可选) -- 左，中，右( "left", "center" or right"),
    font (可选) -- 三元组 (字体名称, 字体大小,字体类型),
    angle (可选) -- 角度值,如90,180

    根据对齐方式和给定的字体样式在屏幕写文本。
    如果move为真，那么海龟(画笔)会移到文本的右下角，缺省为假。

    举例 (假设有一个海龟实例为turtle):
    >>> turtle.write('风火轮编程 ', True, align="center")
    >>> turtle.write((0,0), True)
    """
    if self.undobuffer:
        self.undobuffer.push(["seq"])
        self.undobuffer.cumulate = True
    item,end = self._write(str(arg), align.lower(), font,angle)
    if move:
        x, y = self.pos()
        self.setpos(end, y)
    if self.undobuffer:
        self.undobuffer.cumulate = False
    return item                   # 这里本来不返回item

RawTurtle._write = _write         # 重定义_write
RawTurtle.write = _writea         # 重定义write

# 给TurtleScreen添加_convertcolor方法
def TurtleScreen_convertcolor(self,color):
    """本方法把fillcolor和pencolor返回的颜色转换成从0到255整数的r,g,b三元组。"""
    if not isinstance(color,str):
        r, g, b = color
        if self._colormode == 1.0:
            color = [int(255.0*x) for x in (r, g, b)]
        else:       
            color = [int(x) for x in (r, g, b)]
        r,g,b = color 
        return "#%02x%02x%02x" % (r, g, b)
    else:
        return color
TurtleScreen._convertcolor = TurtleScreen_convertcolor

# 给TurtleScreen添加设置透明度方法 2020/2/26
def TurtleScreen_setalpha(self,alpha=0.8):
    """
       设置屏幕所在窗口的透明度,alpha为从0到1.0的浮点数据
    """
    self._root.wm_attributes('-alpha',alpha)
TurtleScreen.setalpha = TurtleScreen_setalpha

# 给TurtleScreen添加finditems方法
def TurtleScreen_finditems(self):
    """查找所有可用于碰撞检测的items,包括线条lineitem,_fillitem,polyitem"""
    rs = [None,(-3, -3, 3, 3),(-1, -1, 1, 1),(0, 0, 1, 1)]
    items = self.cv.find_all()       # 所有items    
    items = list(items)
    
    items.remove(1)                  # 1是背景图的item编号
    
    # 把说话泡泡的items也去掉
    tbitems = []                     # 保存所有说话泡泡的items
    tbs = [tu._draw_bubble_turtle for tu in self._turtles if tu._tag=='sprite']
    [tbitems.extend(tb.items) for tb in tbs]   
    [items.remove(item) for item in tbitems]

    # 下面是把一些预定义的item去掉
    for item in items[:]:
      bbox = self.cv.bbox(item)
      if bbox in rs:items.remove(item)
    
    return items
TurtleScreen._finditems = TurtleScreen_finditems
    
# 给TurtleScreen添加setcover方法
def TurtleScreen_setcover(self):
    """ 去除标题栏等"""
    bgcolor= self._root._canvas._canvas["bg"]
    self._root.overrideredirect(1)               # 去除标题栏
    self._root._canvas._canvas.configure(highlightthickness=0)
    self._root._canvas._canvas.configure(borderwidth=0)
    # 下面这个_canvas是继承自frame的一个组件
    self._root._canvas.configure(bg=bgcolor)
    self._root._canvas.configure(highlightthickness=0)

TurtleScreen.setcover = TurtleScreen_setcover

# 给TurtleScreen添加unsetcover方法
def TurtleScreen_unsetcover(self):
    """恢复有标题栏的样子"""
    self._root.overrideredirect(0)               # 恢复标题栏
    self._root._canvas._canvas.configure(highlightthickness=2)
    self._root._canvas._canvas.configure(borderwidth=2)
    # 下面这个_canvas是继承自frame的一个组件
    self._root._canvas.configure(bg='SystemButtonFace')
    self._root._canvas.configure(highlightthickness=2)

TurtleScreen.unsetcover = TurtleScreen_unsetcover  
# 重定义TurtleScreen的监听
def TurtleScreen_listen(self, xdummy=None, ydummy=None):
        """为了收集按键事件而在海龟屏幕上设置焦点。_focus是跟踪屏幕是否在最前面的逻辑变量。
        """
        self._focus = True
        self._listen()
TurtleScreen.listen = TurtleScreen_listen

# 以下相当于定义setcover和unsetcover的别名
def TurtleScreen_titlebar(self,status):
    """显示或者不显示标题栏,
       这相当于setcover和unsetcover的别名
    """
    if status:           # 为真则显示标题栏
      self.unsetcover()
    else:                # 否则不显示标题栏
      self.setcover()
TurtleScreen.titlebar = TurtleScreen_titlebar

# 新增onanykey,屏幕的按任意键方法
def TurtleScreen_onanykey(self, eventfun):
   if eventfun is None:
      self.cv.unbind("<KeyPress>", None)
   else:
      self.cv.bind("<KeyPress>", eventfun)
TurtleScreen.onanykey = TurtleScreen_onanykey

# 新增屏幕保存方法,保存的是截取的图形
def TurtleScreen_save(self,filename=None,size=None,margin=5,full=False):
    """ 截屏命令，能截精灵所在的窗口的屏幕或者电脑桌面全屏与指定矩形区域。
        filename:截屏后要保存的图像文件名,推荐用png,不写文件名则返回im图形对象。      
        size:截屏区域,四元组,表示左上角和右下角坐标，如果指定了size，那么margin参数不起作用。
        margin:左上角与右下角边距。
        full: 表示是否全屏截取，如果指定了full为True，那么size和margin参数不起作用。
        
    """
    if full == True:
       im = ImageGrab.grab()
    else:
       if size == None:
         c = Turtle._screen._root._canvas  # 获取画布对象
         x0 = c.winfo_rootx() + margin     # 画布左上角x坐标
         y0 = c.winfo_rooty() + margin     # 画布左上角y坐标
         width = c.winfo_width() - margin
         if width <=0 : width = 1
         height = c.winfo_height() - margin
         if height <=0 : height = 1       
         x1 = x0 + width - margin                  
         y1 = y0 + height - margin
         if x1 > x0 and y1 > y0 :
            size = (x0,y0,x1,y1)
         else:
            size = (x0,y0,x0+1,y0+1)          
       im = ImageGrab.grab(size)
    if filename == None:
       return im
    else:
       im.save(filename)
      
TurtleScreen.save = TurtleScreen_save
  
def _Screen__init__(self,layout):
      """新建一个窗口,如果存则,什么也不干,layout是新增的布局参数"""
      if _Screen._root is None:
          # 下面这样做的原因是在实际开发中如果在程序中重定义Root类,
          # 如果没有参数那会出错,为了兼容,所以用了try
          try:
             _Screen._root = self._root = _Root(layout)
          except:
             _Screen._root = self._root = _Root()
          self._root.title(_Screen._title)
          self._root.ondestroy(self._destroy)
      if _Screen._canvas is None:
          width = _CFG["width"]
          height = _CFG["height"]
          canvwidth = _CFG["canvwidth"]
          canvheight = _CFG["canvheight"]
          leftright = _CFG["leftright"]
          topbottom = _CFG["topbottom"]
          self._root.setupcanvas(width, height, canvwidth, canvheight)
          _Screen._canvas = self._root._getcanvas()
          _Screen.cv = _Screen._canvas
          TurtleScreen.__init__(self, _Screen._canvas)
          self.setup(width, height, leftright, topbottom)
          
      # 屏幕的_groups属性是保存组名的
      self._groups = []               # 这里给screen增加了_groups属性
      self._focus = True              # 描述窗口是否失去焦点的逻辑属性      
      self._ontimer_call_times = 25   # 定时器最多调用次数
      self._ontimer_call_counter = 0  # 定时器调用次数跟踪器
      self._root.bind("<FocusIn>", self.got_focus)
      self._root.bind("<FocusOut>", self.lost_focus)

      # 让屏幕可拖动而新增的属性
      self._oldx = 0
      self._oldy = 0
      
def _got_focus(self, event):
    """得到焦点而发生的事件"""
    #self.cv.config(background="red")
    self._focus = True

def _lost_focus(self, event):
    """失去焦点而发生的事件"""
    #self.cv.config(background="grey")    
    self._focus = False
    
def _startmove(self,event):    
    self._oldx = event.x
    self._oldy = event.y
def _stopmove(self,event):    
    self._oldx = 0
    self._oldy = 0        
def _movewindow(self,event):
    dx = event.x - self._oldx
    dy = event.y - self._oldy
    self._root.move(dx,dy)
    
def _draggable(self,default=True,key=2):
    """默认按鼠标中键拖动窗口的方法,取消用 screen.dragable(False)
       如果用鼠标右键拖动,那么用screen.draggable(True,3),取消则要screen.draggable(False,3)
       如果用鼠标左键拖动(不建议),那么用screen.draggable(True,1),取消则要screen.draggable(False,1)
    """
    if default :
        self.cv.bind("<ButtonPress-" + str(key) + ">", self._startmove)
        self.cv.bind("<ButtonRelease-" + str(key) + ">", self._stopmove)
        self.cv.bind("<B" + str(key) +"-Motion>",self._movewindow)
    else:
       self.cv.unbind("<ButtonPress-" + str(key) + ">")
       self.cv.unbind("<ButtonRelease-" + str(key) + ">")
       self.cv.unbind("<B" + str(key) +"-Motion>")
    
_Screen.__init__ =  _Screen__init__  
_Screen.got_focus = _got_focus
_Screen.lost_focus = _lost_focus
_Screen._title = 'Python Sprites Module' # 默认标题
_Screen._startmove = _startmove
_Screen._stopmove = _stopmove
_Screen._movewindow = _movewindow
_Screen.draggable = _draggable

@staticmethod
def _image(filename):
    return ImageTk.PhotoImage(file=filename)

TurtleScreenBase._image = _image

# 以下重定义TurtleScreen的初始化方法
def TurtleScreen__init__(self, cv, mode=_CFG["mode"],
             colormode=_CFG["colormode"], delay=_CFG["delay"]):
    self._shapes = {
                "dot":Shape("polygon",((0,1),(1,0),(0,-1),(-1,0))),
                "line":  Shape("polygon",((0,0),(0,100))),
                "pointer": Shape("polygon",((0,0),(5,0),(5,50),(10,50),(0,60),(-10,50),(-5,50),(-5,0))),

                "star":  Shape("polygon",((24.270509831248425, 17.633557568774194),
                                         (4.873795443493595, 14.999999999999998),
                                         (-9.27050983124842, 28.53169548885461),
                                         (-12.759762125280597, 9.270509831248424),
                                         (-30.0, 3.67394039744206e-15),
                                         (-12.759762125280599, -9.27050983124842),
                                         (-9.270509831248427, -28.531695488854606),
                                         (4.8737954434935915, -15.0),
                                         (24.27050983124842, -17.6335575687742),
                                         (15.771933363574007, -3.863009542013251e-15))),
               "arrow" : Shape("polygon", ((-10,0), (10,0), (0,10))),
              "turtle" : Shape("polygon", ((0,16), (-2,14), (-1,10), (-4,7),
                          (-7,9), (-9,8), (-6,5), (-7,1), (-5,-3), (-8,-6),
                          (-6,-8), (-4,-5), (0,-7), (4,-5), (6,-8), (8,-6),
                          (5,-3), (7,1), (6,5), (9,8), (7,9), (4,7), (1,10),
                          (2,14))),
              "circle" : Shape("polygon", ((10,0), (9.51,3.09), (8.09,5.88),
                          (5.88,8.09), (3.09,9.51), (0,10), (-3.09,9.51),
                          (-5.88,8.09), (-8.09,5.88), (-9.51,3.09), (-10,0),
                          (-9.51,-3.09), (-8.09,-5.88), (-5.88,-8.09),
                          (-3.09,-9.51), (-0.00,-10.00), (3.09,-9.51),
                          (5.88,-8.09), (8.09,-5.88), (9.51,-3.09))),
              "square" : Shape("polygon", ((10,-10), (10,10), (-10,10),
                          (-10,-10))),
            "triangle" : Shape("polygon", ((10,-5.77), (0,11.55),
                          (-10,-5.77))),
              "classic": Shape("polygon", ((0,0),(-5,-9),(0,-7),(5,-9))),
               "blank" : Shape("image", self._blankimage())
              }

    self._bgpics = {"nopic" : ""}

    TurtleScreenBase.__init__(self, cv)
    self._mode = mode
    self._delayvalue = delay
    self._colormode = _CFG["colormode"]
    self._keys = []
    self.clear()
    """给屏幕增加简易右键菜单,修改右键菜单按tkinter的方法即可,
      删除一项菜单:delete( startindex [, endindex ]),根据起始和结束索引号删除菜单项目
      修改菜单项目:entryconfig( index, options ),根据菜单项目索引号修改
      增加一项菜单:add_command()
    """    
    self.popup = TK.Menu(self._root, tearoff=0)
    self.popup.add_command(label="关于本程序",command=lambda:showinfo('关于','本程序由精灵模块开发'))
    #self.popup.add_command(label="打开主页",command=lambda:os.system('explorer http://www.lixingqiu.com'))
    self.popup.add_command(label="截取本窗口屏幕",command=self._capture)
    self.popup.add_command(label="退出本程序",command=lambda:self.bye())
   
    if sys.platform == 'darwin':
        rootwindow = cv.winfo_toplevel()
        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
        rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
TurtleScreen.__init__ = TurtleScreen__init__

# 给TurtleScreen类增加_capture方法
def TurtleScreen_capture(self):
    """ 生成一个随机文件名然后截屏"""
    filename =  _makerandomfilename(".png")
    self.save(filename)    
    if os.path.isfile(filename):
      showinfo("恭喜",'成功截屏到\n\n' + filename)
    else:
      showwarning('出错','截屏不成功,请自行检测是什么原因')
TurtleScreen._capture =TurtleScreen_capture
    
# 给TurtleScreen类增加右键弹出菜单方法
def _do_popup(self,event):
    """显示弹出菜单"""
    try:
        self.popup.tk_popup(event.x_root, event.y_root + 10, 0)
    finally:
        # 确保释放按键
        self.popup.grab_release()
TurtleScreen._do_popup =_do_popup

# 增加右键菜单
def _add_popup(self):
   """绑定右键菜单"""
   self.cv.bind("<Button-3>", self._do_popup)   # 画布绑定鼠标右键
TurtleScreen.addpopup = _add_popup
# 移去右键菜单
def _remove_popup(self):
  """移除右键菜单绑定"""
  self.cv.unbind("<Button-3>")   # 取消画布绑定鼠标右键
TurtleScreen.removepopup =_remove_popup

# 重定义TurtleScreen类里面的register_shape方法
# 目的是让它支持png等图片
def _register_shape(self, name, shape=None):
    if shape is None:
        shape = Shape("image", self._image(name))
    elif isinstance(shape, tuple) or isinstance(shape,list):
        shape = Shape("polygon", shape)
    self._shapes[name] = shape

TurtleScreen.register_shape = _register_shape
TurtleScreen.addshape = _register_shape

# 让窗口可以支持自定义缩放,默认是不支持的
def _resizable(self,width=True,height=True):
        self._root.resizable(width,height)

TurtleScreen.resizable = _resizable

# 重定义Shape类的初始化方法
def _shape__init__(self, type_, data=None):
    self._type = type_

    if type_ == "polygon":
        if isinstance(data, list):
            data = tuple(data)
    elif type_ == "image":
        if isinstance(data, str):
            if isfile(data):
                data = TurtleScreen._image(data) 
    elif type_ == "compound":
        data = []
    else:
        raise TurtleGraphicsError("无此形状 %s" % type_)
    self._data = data
Shape.__init__ = _shape__init__

# 给Shape类增加save方法,用来把角色当前的造型保存为图片
def _shape_save_(self,imgname,x=1,y=1):
    """保存形状为PGM,PPM,GIF,PNG图片
       imgname：图像文件名,x横向缩放系数，y纵向缩放系数       
    """
    if self._type == 'image':        # 暂时只支持图像
       photo = self._data._PhotoImage__photo.zoom(x,y)
       photo.write(imgname)
    else:
       print("只支持造型为图像的角色。")
Shape.save = _shape_save_

if not os.path.isfile(os.path.join(_resfld,'rat1.png')):
    __rat1 = b'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'
    __rat1 = BytesIO(base64.b64decode(__rat1))
    __rat1 = Image.open(__rat1)
    __rat1.save(os.path.join(_resfld,'rat1.png'))
    __rat1.close()

if not os.path.isfile(os.path.join(_resfld,'rat2.png')):
    __rat2 = b'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'
    __rat2 = BytesIO(base64.b64decode(__rat2))
    __rat2 = Image.open(__rat2)
    __rat2.save(os.path.join(_resfld,'rat2.png'))
    __rat2.close()

if not os.path.isfile(os.path.join(_resfld,'explosion0.png')):
    __explosion0 = b'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'
    __explosion0 = BytesIO(base64.b64decode(__explosion0))
    __explosion0 = Image.open(__explosion0)
    __explosion0.save(os.path.join(_resfld,'explosion0.png'))
    __explosion0.close()

if not os.path.isfile(os.path.join(_resfld,'explosion1.png')):
    __explosion1 = b'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'
    __explosion1 = BytesIO(base64.b64decode(__explosion1))
    __explosion1 = Image.open(__explosion1)
    __explosion1.save(os.path.join(_resfld,'explosion1.png'))
    __explosion1.close()

if not os.path.isfile(os.path.join(_resfld,'ufo.png')):
    __ufo = b'iVBORw0KGgoAAAANSUhEUgAAAGQAAAAvCAYAAAAVfW/7AAAABGdBTUEAAK/INwWK6QAAABl0RVh0U29mdHdhcmUAQWRvYmUgSW1hZ2VSZWFkeXHJZTwAABxgSURBVHjazI+xDYNAFEPt43JHQRGksAEl+6+QKeioaCgSKShw3/lKlIINsGXpSXZjSsJZNK8vTI8ntveG4g65RkwZcjd1PmwNsS2o+i8ChVJH2aAQ7gJ30sYgW/i/R89OkA4Xg/nvZAm3CFyrX30GfQQQ42CIEJALngEj487H9wwsTMzASGBjgLkLSDJ9+/FL8c+3n3bCQkI27Lzcf38z/OcHBqEp438mKWiEgAAwWBnYgPgHWB/j/1eMDP8uM/37u4qR4f9Zhv9Mt4B6fsPsZALFy19mhj9AhijTPwYxFqZBESEAATTgEfIPaP39Lz8Z3v76xsDOgkinQHcxvfn21eHD338NTP/YrKSFhZnZOVkZ/oCzAzD0/0MwTo9BIxqC/zMw/2M8zvKHYQUT87+tjMx/7wEj6T9yguD4z8ggy8rCwDLAeQUggAY0QkBJ+/aHLwzvvn0GplhGaEAyMvz488v45d/f9V8YmX15WdgYFITEGDhZmRl+/0cULcDwY8Dnciagv5iANgDjFWzqX6b/oHINpP8HUOQp8///zWx/mRciRwoXUI0MKyirDVykAATQgEUIKGece/ea4cufX+DIAJXtv//84f3861/re0aW3F9ANUKMzAzKIqIM/9mBcoygQGaCBBWoHAM7Ho/5wGLoH+M/sB4gh4Hn/18GIWCW+sPIxPDpHyPDV6C/Wf8zzQXGQQnQsA/IOUsVWPixDlCcAATQgETIb2Bs3Pz4leHvf3CKBeeKDz+/Wj//+XPRJ2Z2JVDq5mD6yyAnLsbAy8QKzkr/GCnLiQJA/TLACGEFxiYwPzK8+/eb4TPIXAbWd6y//7gCs9I5WE5hBqpV5WBlYBmASAEIILpHyO+//xguv/gIjwxQmv/E8Dfu0e9f838zsTMxAitZtr/fgJEhwsDNwcEATOQMTP8gSZcSlzIBW20CQFqEmZmBDWjQL2D2evfvH8P7P0AZRsZPwOq9ioXpz1R4pACxCgs73esUgACia4T8Btp1/fMPYGRAigZQUfX2y7fsZz9+TPzFxsjMCCxamP78ZxAX4mKQ5ONjAJYywFYQAwMLtHamJJf8ZfoHrleE/jEziLGCiqt/wOKLmeHNn78M74ER8xMUUQx/E5j//V/4HylnKbKwMPAx0q8FBhBATPQspm68/sbw7zuwf/ED2IP4+Y/h3adPCff//Jjyi4WZGRgQDEzABq0AGwuDCC8vMDL+ozSLKU55QPgH2KT+AAzmz8AIALW8WP79ZRBmZgIWi0A2kP+LiXXBXybGUnADDJSDgfjx79/ghEQvABBAdIuQex8+Mfz69x3o7Z/A0PnJ8OnXN2Cd8Wvmf2AuAVe8/9mBQcbOICrIz8AGFAPXxeCKHBIh/ygsOYDNXiAGJgxgPfIZWGz+BOYOYCcS3KJiYmQFV/yg4vEPE0stE8N/LaY/fxiYgfgfED/++YNuEQIQQCz0sOTNz18MT3//ZGBmgvYO/v8Xev7n57yvbMA2LVCMEVw2AXMHNxcDN7Cv8Q+YW/4z0qbs/gcsfj4Ca21QvcQPatkBnfMNnAMYwcXoXwZG3p8srLtYGFltQV0kkJ6PIAxUw89I+/oEIIBoXod8AhZD939+ZWCCVY5A6x69+zz31V/mJAYmFqA4uKsHrCf+MSiLSzJws7CC6xhggsXbrCV5NADaKGCE1l+swEgH1U2g5vRvcG5khPZfIPLAjLSE5c+fdCDzG6w+kWdjZuBlpm2kAAQQzXPIy2/fGF5++QpsQkJS4K///5Le/fufBMwaDP+BZTgo4EFltCA3N7DzByzJoS0qansbFreg3j0jOJMyMnwHV/bAJjY444IKU0ZwhLCAizaGmL9sTM/Z//wrg5XtD4ENAHlgUcfLRLtIAQggmtYhP//+ZXj58QcD+x9mBhZgMmQF4g+/GL2/A3MBM7CY+sv8m+EPMIQYgcWIABcvpEcNa95SOeOCApoJ2lL7C/T1L6C9TEAsDmTLAVM9CHP/hww6/mMCNclBFT9TNrAhIP0XGAkw/J/GzWCAAKJphDz9+h08eMfMAowQYPPxJxODxwdWxiA2YIgwAmttUNuGAVjB8rAyM3CxszHQqzEDHvgFViKs/34xSAFLTF5gGcnJ+IeBj/kvqOkLLt9A7gYq4WL791+XExg5HEAMoj/+/UdTtwEEoMWMdQAEYSDagqKObn6gH+UnOpGog0QqeMhGXBwYboceuXu0miEXDm5PXEJ1oCYDtbRHnnVAWOGZOnA/Rf3+DcahJ5M6g/MWthSXon/6iq8mpMjUdKg8/ADeAnag0fImKwK5UscI8+JYJg/DBNrI03pLNUMeAUSzOuQ90MNcwM4dE3So++vPX3pf33335QQXS8A2PzOkKcrEDKzEgY2tT7/+gpudjLCWDLhG/wfmgwMWNviI1tLBJo4rIiDqIDQb0O7/wFz7DOhAXkjzi+ETA0gMXJ0A3cwMbnoDI0seWHRZMv37tx7cwYSONtMKAAQQzSLk1ddPDDc+fmFgZYJW5gz/zf6x/AOGA7BtDxoe+Q8ZMwLJvfnwnuENtLKFhSQjAyKgYYENahHC+IywAUaYPOM/SKMVmo0grSlgUDIxokYWsL4CjRCAWn1MsBiCmsGEHNmgeRlQjgEqYv79Vfrf+w9gdSAnfgHSItJyDOzM1A8+gACierP39/c/DHf2P4D0tCGtF8aff9n+v5cVmPeR5X8iKPmB7AR59C8TajnCiFHSQ/ot2JzI+B+p4od3bxiR+uXAtMz4B2+r6z9a2c30H7W/wvwP2CcCR92PX5pMnCGMH77u+P3/729Q5IH6Stz8bAzqJqJUDT+AAKJqhPz99Y/h+Y1PwLIZYiZoCOjZ5fd5H+//r/zNyiLE9J+djRE0RPIfs0gBt4JgRRYjrOX/D4/DQZniP1KTFlInIfod/8EYvdn7H5ogmIH2gPC//wzw2UlkN4Er/b+gHMHGAMrVbMAGwDfhr1cVzCSdWFlZX4H0/AMmOgl1YGdWkHo5BSCAqJrnQCn07ydW8KAgZPQQ2LZ/yp3E/YlD4jc7sMoEFsqg9MYMVAdrfiJSJAOiyQtO7iyE2xwoiQmUI/4igvU/Wg4ARcL/f2ijW5BRXXCEgCIQLYGAYosRpAfUs//DzsD57r/az2fvBf+xQSPkDxDLs1A1GAECiKoR8uMPsB3/5S+k5gOXOP+Z2P/9B8bDT2BaB42S/AR7+g9yvQ1zCJDNhpJZ/2Dt2JHStGVE0gwqgv4ywscLwJGPqJwZUcpAyLQAC8M/ZlhxxsjwkxVUz/CBUhzj/7//IOOPwBzyh8qtYIAAokqEfAa67umPnwzvvvxh4Gb+B/cjsMj4/5WF8T87I6h1D+xYMTHBgwkWGYxITZ8//5EFsY3XktAv/49kB3gYhhFjDh5cdCLNCePukIJiFBg7oKGefyzgZju4JQbMQU9+/mV49+c3gwiwEcDPRHkvAiAAq9ayAyAIwxwJClf///M8G+MFTSaz4yHGo3oehEEphZVPgOzIagJtl8iQPU5HiNc7rlyGh6zE0L8N29FDW+JNA6gtWOki6R1M3S81vCwODWxoApujDtR+QSg5TPUtTam8yyMHEENY48G5GGyf25EyBCjP6qkgrpbzONhUhHw7hVMAkRUhIH+8AEbA858/GJjZucAjdFyM7AwMQOZXU4iHvjD9MX/381PYe1Z2xV8fgVmc+S+knId6mBXUF2BmAvfgWdnYGFiYmMDzD/9hzVukiGJAqpAJFlWwJjIoQv7+g0cIqN5iBnUG0SsXeCsNEimQSp8BM1H8/c3AwcF27IUxGzc/P7MksLp6DjOGE5Q4f/8B9+JBWAiYWySZIGuSSAUAAURyKws0VP0YmCK+/P7L8OnLF3DZDC8CgN2Lz39+BT39+avg7e+/pj//MzP9Bw0YMoPmG/4Ci4i/wB45CwMvNxeDAA8HAyuwtw7pR8CarYiEy8RA3QFGbC07UvUD676/v//9Zub9+/sTB8O/hdysLNs4/jDt+fvv3x9YQuVgYWZgZWEFtrhBK1j+M/CSWIwBBBDREQJS9RoYCY///gbPIfz7h+gEMDH8E3z14VPY/W/fMl+wMOgz/mdjYAUPxv2HtLz+/QOnFiEeHgZ+Xh4GDlZmsIF/IdkBHCmgVtY/9EoZX5VCYFSXgcoRCmsFgjD7Xwbw0COonS788/cp/v//ZrAw/d8OzJYvYG5gA/qfCxgxYsBUKsJKfEEEEEBERQiosHkCDK0XX74zMLP8R8oRjCzPv37Pvfbxc8n7//+kgJLA1hILAzuw1/cb6JDfTP/BuYKbg41BWICfgQtYvoL7D38QHsQoOpD7GTQagid30I8JPHHGAF+G9A86lwJMnQx8f34/FGb428vHwb6GhZn5OSxYQYlMCEjKMhK3XhUggIiKkDvAlsSzr5/hvQLQEMOP/4zGtz6873j8968LIyMXuLxiBE80MTJ8AzYRQc13DmDAiwjwMojwcYM98hdUaf/7Dy2WGFGmZRnResrUBvAJKgoikxEaxP8YoZ1bUO4HBjRo/gQ0bP+L9S8Dz/9/32X/MRXzs7BMh1kGihRBoLwMEZNbAAGENUJAHZ5fP4BlPrB+uP73B8PLPz/gq/lYmJnYX3//3nz108+8X0xs7CzQCgB9JSEj4z8GcRFBBgFOLgbm39DszkSg3zB41n2TURlD/AdqzXEBGzwif/4uFeFgzAUKvf8PLWVEgJEnx8qK1xyAAEKJkJ8f/zC8f/yD4ce3fwwffv5kYDARZmBkhoQ0KFd8/PJZ7eKHdwue/mG2ZAZW1ExIpT4iQoCtGWDrSUKYj4EHWFSBh0r+geRAqhlxDocTrDPITNqM1KxM/qO5BSkFMUJHH0Cj2OCcDiwi+P/83CbJwJAowMHx6h9kCJmB4csvBu5bnxmEBQUZmIQYGdj5UVMpQADBI+Tbsz8MLy59ZPj59w8DqxQ3wzdNHngzEzTm8+Tnl4yLL99M+MbADqwJmBn+Adv0yHUALELA40TApiw7MxO01iYcpv+hvWHYMDsjFg3/ob02RmydlP8MiNYaekQzYu/XIPo9hKMU3vyGLoYAuxc08cbMjFQq/AXPoYASHjAEINPATMAym/HXZx0G5kg+Rtat4MVHwGDh/MHIIHeVjeEzaBmSKgcDrwwzAzMbxCUAAQSOkN/v/zE8P/2F4S+oBQVsqn025GL4zQEZ0QZFxotvP1NOffo4+z9oSBpYaf9l+gX2Cnj5DlKEIA+Rg5MLVP4flGRk+AcPZfQynZEBc/QW12AINFwgShiR9KPPx8MilxHRCWX4/x8eucilNSPYR/8R/R34ICcjopuCVs0zIo0u/we2VP4z/gaGCbBw/w+JKNCSI5Cb+H/9/GggKhgsxcez9+8/SKSwfAY2iS8B+za8wPBk/sMgrsvJwMLKxAAQQIyg8Zj3938zfPj4EzzEALb933/G188/sP9iYvnxXYbN7/yfH4u/sHHwsTIiChgmYsr8/zg6btD4+odzMQMjvAOHSOGwwUOIuX+ZYGu1GBHxBwthWKJAyhow+3Dl2P/ghuw/RMJgYoRGAjSHMDCgLmf9D2mgwOz4j0gPUO2M8NwO6qTw/v79wY6P35mbne0cqPgC55T3DAyir5gY3r//wiAgxcAgpiXEABBAjKcX34J7kpWdhfvPb+bIzx//RLN+/KcErNZ/f2RlEWP4z8ELTj3MfxFeIRAZkNXniNFXRqTsD0lRaBHy/z88sv/DZgnBMcIELab+QSehGODLSuEJFOxBhD6UqUGkHPwXNv2LpWwDLWz4j7TdipERkVX/w8xjYsQx0gwx/x9yRIM6hMxMcP5PICHw9885yT+/5v7994NVlE/0zl9OlsNM3IyfYJ1idi4mBoAAYmEC1foQ/6p/evhnFdNbbj0mRg6GPyy/wVmPH4iZGX6DFmICLWVBc8R/eLGEXuP9BwcgC4FeG0w/bG0O0jDwf7QAYWAHMtmgxR5sgokRWswwIhn/H2uNhWhWYx03gdY3/xFzMP8Z0XIQqk4wnwnRIoGtroS55z/GYCcTsPXFavSHkcXoMwcHw6e/XxnYeBmeiqqwt7HzME0DDfX8+M7AABCAbWvJQRAGosNACo3EBJe6cuUVvYJnMt7BvWsTNyYmGlBpB9+0JCAadoV0+pm+N9PhJef9jbzzq9PxcuA62+RuSTVpYvck6w1ZeLlkjRb7xy7ZE/gMXnANhOzaChm5o8zUYWIs5h/wTiqECA6SBgFJgT4McfqIAhspsXrv7yv4TpU0+t5GaOl1HyLAbIw1VS1IgJ0iFqrQRiOOm0Jk1z+JYn+7CLZZ1XBdGfvnBgfS/HDksI8txgInwXckNhI6o83PYf4euIRlsKb5CiPySjEPYf1FtYBtrJVevK7zXVq9tuoLHwEItbbVhIEgelbXbNQomqoVRfSt4A/2qR/jB4mPfW0KpUUUa0hMorsbj1FsFUo/YIaZM2cuuzPy024QvaUv6rv+JMo+G9EW/mgBz98gDX32lymk6dHA+Hrdd6aEpEIabWp0ZovmYI6Se0D8NYaOeqx/2T/noKYIoHBiqEbIeVEhCxV1ElAZXljl/OwoisDxgclSaAh2zqmj1g7gtdfIkiqS1RA66UOoFUVa5+wU9u+2xkCYtAPhfkDWAwLE3MuaKEl9oZtzW6Lus+r0c3yochCyxV5ElEkIeZKJCLIqiGV/rZAFSZfLNfSePtgE1l0i3z9A2Qp27/r5sZO/dife7CiAWHiZ+dXfvWUOYQYWXX9+/2eQM9/BoGh5HBgo38G59/kZN4bbRxyBqYcbZUqVCZzigAHD+o1Byfo0g7jOfmAYfGH4+VqH4cYRHYYP9y3BTUPslQ2wh/uXg4Ff4QCDmvVFBk7RWwz/gPyXl+0Y7p4wA7YUxYFqWCGpD9a6AuWYP/ygBjrQxB8M8mZ7GRT0rzAw8z4CRqYAw9tHigw39oYCI4UPmFu+QwMfd4CCxtc4ZfYxqJpdZOAV+sDw/Ss3w8PzRgzv7qsB9XMCPceFZ04eGGV/BBgYOe8zSChfY+Dm/cfw8eNvhtc3naGLJ0DFPRtSrmKE+OUPMOdzPmaQ0jrPwCf/gOH3V1mGl1cEGX4+NmN4d+df9W/GN2sAAoi5KLAq+MtjlrC/wCzGK3mVQcNzBTC2f4LHZxhY3zLwir9k+PhCnOHbOyVgLvmD0g76+4uXQcJwF4O83Uqg5X/Ba0tY+O4DHQhsKl83ATqKBWtTDLQeio3nJYOu9wYGLukLwMj/wMDExsTAJ/eM4fdnboaPT0WA9SETSsXMCCwWQOr+/gF2OtWuMqg7b2Zg4nwOSSOsH4Dm3GNg5vjJ8Pq2AWKPII4cCrKfhfsbg77fJgZ+peMMzOzfGThE7zAIyz9nePdEjuE30K/MzF/B/QnsBgBtANqp6bKFQc5iLwO//CUGMdUnQFvZGD48VgImpb+QdiJ8JJwRUgf/YWZQtNnGoOi4mYFL+BWwVLnEICT1luHdAzWGH5/ZhMXV+A4ABKDbDFoTBoIo/DTajUYakxglGMGCFIQc/fG9F0rvpYeCEUQkAcGD0DRr3MSXJRdre86Gnc3b981k2WnLb+mVkNS0gGX/oC0yfdNCmRtiwaeyAg/2gfqo25iYX1r8QE5Qt+c98jkt302pyZiTpRDDnV74nxUY2W/5CcxRjEo6mvyKTIWRwpsd6ayOPra5O+JUA26KM4LoTaOhqvg/ZJw0HqoshBOuKXTSdF31fs/aBE6UEDPe0yesCZ1ZCJTGEaroo2NvETzHuJQ5K3/j3/drTLnzL4yid0Ze5xLJ8Rmmqxeui/grrDtHlcxHprvHZPlBYep7B6x56UrhJhhHr8wvOU6HfHEVgG2z2UEQBoLwlrYQJBpNOHjwYKLv/1geNEqQP9sgdXYlYtAb9MCm7Xa+2XSJFrk+SVcFJtqe9zQ0O7G3yh+g71cK3Ya6yxEZM3MtXBw+l1QXCA6+KOSFwjvrv6u21Df5Xw3/VBl9KgtMphTnpJQXZnjnxyIvm8mdlsXQdqDYRiInrMsck0+iim545n88mENfNct0xKabFuVgPsCpuJTvBuFhDSaskQyouG31BvbfviO+LXzAojqJwckbmCdQFQ0emrQDwLFJlPzYYm7P1Ml9bKjJkMAtxgqyYUUGPLEmdi8B2DaX1YSBKAz/mVxUqnipDVgourBdVIrQTXHXx/YRRLALwY1IsMWglmDaGGNsbj1zEKTa7Sxm5tw/hn9EqXbVz+VTS48NeJsKrMELMp+og+ZDSsGwhk/wl/c0uJOLA4R2wGryjO3sFVIZKhE6Cxt4f2sh2sts/j8gUuTsrevYTHvkiBsepKoeInY6sMddMqZAJOKdoavClBUdqC3YD+zXjA2X5RCzSuL7o4ufXZGo0JefOc+S9ITnilDh2m3EbocrUaVqF3KP/S2c+R20tEzr6eVz8bFShNDhfV4jCarUWiOeefwCvmojcKrUOSSAGH/uLiiBQ7cCf/FI4PHFQjwlR+ATmHDnTSTGNiqbpdGvAGJOTyv8+ufvT6YfLxg9mNl+M3x8rMXwFlgOf3ikwvDgeBjD2zv6wJj7xgCZkmFBbYYCK6p/3ySBZaAsw7cPrEC9hkA9Lgwf7hkDHcqJmUqRm/7ASvz9cy5g65EX2LqRAjpUmeHOIXOgGRbgCAJXgv/ZkHr4P8FNUlDgf/nIzsAr+JOBU+gduCxnYBRk+PLYmOHWIQuGv98lGcCpA1x//cU6LMsIbIL+ABYXP7/9YuAHmsPM/Ivhz0dthvtn1BleXbMG+pIb3KpErUMQfSRQhH7/AtT/A1jvCfwARsBbYGSoM9w+4Mzw7aUxsD78DEkkcP2QrUD/gcXjR2BEcnKwM7BwfGP49VaN4e5BR4YXd00ZOKR+HxWS5+gACEC21eUQDAThaW23IdUWiRcSHMIRPDuoe/DgCkTigQQhRJtaFt9M/VRcYHdnZ/b7mU6d9Zh7WNZbTvej28YbKgST4TAWXkA54AkXB0a2+XBckc7HSPE3D1xQaSs9LWMi4PkZiUDaIF0fgKDHDw7/WiuuwLvlITQEziLiGop3UXj2LKVlPzf9enxe71YXiLPYT4HQm90VVeI9pccG7RYMky1iU8ucwpBa7J3dZR7MvCStLwiUwbrr+ACOnJE9dSDzI1KuzmexJF7712B5/6PL61jIXV2+kFedkzn2IHJ03h2XewEcFl6JwwXMA7ViNsDVAWRvUgMVhmRCk7T7/iCo6slTADE+3PUJ2lH/x/ns/pum34/Z8oAdNdCeWGjPFrFshwltShNlyhWplw3t9+JYGoo28AfelgAKLGBkM71n+A1scv4BLX8G5gjG/4wYPWpYm+UfuFP4F5JIgJ5lAhUBoLKcATq+9B/ZPlAwsDBw/P/K8AfoqV/AHMD7+ydkLRkTZIkPC7gz+Bc6RANdFUNougo0iAheEsQEKZ7h9RQD6igneKjnH3h4Bro+CphhQCuH2Rh+c315zKf5J4mDj2UPKB0ABBDj2dXPUPzMzcJh8f7Jp+wPbz78Z2IEWsXEhLoIGd5SgmxuIX6dFCukBw1bJYQ2LM70F5QAQJECLOqAlSqwlGZg+8PJ8B/HoNk/YMfvL7gI/QetqKGrWuARxwJZSwUdomEEdsDY/39n+MbCwvCNiZ+B8+93sJv+AjuRLH8hi7X/IHUE0RMg1ilIpCEbgidLoAxuAptAf/8wMvJ/YmTWZGj/8+/vNZgMQIABAEAIgqp+e8DpAAAAAElFTkSuQmCC'
    __ufo = BytesIO(base64.b64decode(__ufo))
    __ufo = Image.open(__ufo)
    __ufo.save(os.path.join(_resfld,'ufo.png'))
    __ufo.close()

if not os.path.isfile(os.path.join(_resfld,'fighter.png')):
    __fighter = b'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'
    __fighter = BytesIO(base64.b64decode(__fighter))
    __fighter = Image.open(__fighter)
    __fighter.save(os.path.join(_resfld,'fighter.png'))
    __fighter.close()

if not os.path.isfile(os.path.join(_resfld,'thunder.png')):
    __thunder = b'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'
    __thunder = BytesIO(base64.b64decode(__thunder))
    __thunder = Image.open(__thunder)
    __thunder.save(os.path.join(_resfld,'thunder.png'))
    __thunder.close()
     
if not os.path.isfile(os.path.join(_resfld,'bug.png')):
    __bug = b'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'
    __bug = BytesIO(base64.b64decode(__bug))
    __bug = Image.open(__bug)
    __bug.save(os.path.join(_resfld,'bug.png'))
    __bug.close()

# 以下是小猫的朝右造型
if not os.path.isfile(os.path.join(_resfld,'cat1.png')):
    __cat1 = b'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'
    __cat1 = BytesIO(base64.b64decode(__cat1))
    __cat1 = Image.open(__cat1)
    __cat1.save(os.path.join(_resfld,'cat1.png'))
    __cat1.close()
    
if not os.path.isfile(os.path.join(_resfld,'cat2.png')):
    __cat2 = b'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'
    __cat2 = BytesIO(base64.b64decode(__cat2))
    __cat2 = Image.open(__cat2)
    __cat2.save(os.path.join(_resfld,'cat2.png'))
    __cat2.close()

# 小蜜蜂造型
if not os.path.isfile(os.path.join(_resfld,'bee.png')):
    __bee = b'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'
    __bee = BytesIO(base64.b64decode(__bee))
    __bee = Image.open(__bee)
    __bee.save(os.path.join(_resfld,'bee.png'))
    __bee.close()
    
# 花儿造型
if not os.path.isfile(os.path.join(_resfld,'flower.png')):
    __flower = b'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'
    __flower = BytesIO(base64.b64decode(__flower))
    __flower = Image.open(__flower)
    __flower.save(os.path.join(_resfld,'flower.png'))
    __flower.close()

if not os.path.isfile(os.path.join(_resfld,'ball.png')):
    __ball = b'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'
    __ball = BytesIO(base64.b64decode(__ball))
    __ball = Image.open(__ball)
    __ball.save(os.path.join(_resfld,'ball.png'))
    __ball.close()
    
if not os.path.isfile(os.path.join(_resfld,'sky.png')):
    __sky = b'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'
    __sky = BytesIO(base64.b64decode(__sky))
    __sky = Image.open(__sky)
    __sky.save(os.path.join(_resfld,'sky.png'))
    __sky.close()
    
if not os.path.isfile(os.path.join(_resfld,'b1.png')):
    __b1 = b'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'
    __b1 = BytesIO(base64.b64decode(__b1))
    __b1 = Image.open(__b1)
    __b1.save(os.path.join(_resfld,'b1.png'))
    __b1.close()

if not os.path.isfile(os.path.join(_resfld,'b2.png')):
    __b2 =b'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'
    __b2 = BytesIO(base64.b64decode(__b2))
    __b2 = Image.open(__b2)
    __b2.save(os.path.join(_resfld,'b2.png'))
    __b2.close()


# 以下定义屏幕的鼠标移动事件
def __onmousemove(self, fun, add=None):
    """绑定鼠标移动事件"""
    
    if fun is None:
        self.cv.unbind("<Motion>" )
    else:
        def eventfun(event):
            x, y = (self.cv.canvasx(event.x)/self.xscale,
                    -self.cv.canvasy(event.y)/self.yscale)
            fun(x, y)
        self.cv.bind("<Motion>", eventfun, add)

def _onmousemove(self,fun,add=None):
    """绑定鼠标移动事件"""
    self.__onmousemove(fun,add)

TurtleScreenBase.__onmousemove = __onmousemove
TurtleScreenBase.onmousemove = _onmousemove

# 重定义_drawimage方法
def _drawimage(self, item, pos, image):
    """在画布x,y坐标重新配置image
    """
    x, y = pos
    self.cv.coords(item, (x * self.xscale, -y * self.yscale))
    self.cv.itemconfig(item, image=image)
    self.cv.tag_raise(item)
TurtleScreenBase._drawimage = _drawimage

def txt2image(txt,filename=None,fontfile="msyh.ttf",fontsize=18,color=(25,0,255,255),bg=0):
    """
        文本转图像实用小程序,只支持单行文本,默认为微软雅黑字体,
        txt：文本
        filename：要写入的文件名，如果为空则不写入，并且返回图形对象
        fontfile:ttf字体文件
        fontsize:字体大小
        color:颜色,通过写alpha值可支持半透明图形。
        bg:背景颜色
    """    
    windowsdir = os.environ.get('WINDIR')
    try:
       fnt = ImageFont.truetype(fontfile,fontsize)
    except:
       fontfile = 'msyh.ttc'                      # win10的微软雅黑为ttc
       fnt = ImageFont.truetype(windowsdir + os.sep + 'fonts' + os.sep + fontfile,fontsize)
    
    size = fnt.getsize(txt)
    pic = Image.new('RGBA', size,color=bg)
    
    d = ImageDraw.Draw(pic)
    d.text((0,0),txt,font=fnt,fill=color)
    if filename!=None:
        pic.save(filename)
        return size
    else:
        return pic
      
def txt3image(txt,filename=None,fontfile='msyh.ttf',fontsize=18,color=(25,0,255,255),bg=0):
    """多行文本转换成图像的命令
    txt：待转换所多行文本
    filename：输出文件名
    fontfile：ttf字体文件
    fontsize：字体大小
    color：字体颜色
    bg:背景颜色
    """
    lines = txt.split("\n")    
    images = []                      # 存储单行图像对象 
    sizes = []                       # 每个图形对象的宽高
    width = 0                        # 所生成的图像文件宽度
    height = 0                       # 所生成的图像文件高度    
    for line in lines:               # 文件中的每一行
      info = line
      if info =='':info="\n"
      im = txt2image(info,fontfile=fontfile,fontsize=fontsize,color=color,bg=bg)
      images.append(im)
      w,h = im.size                  # 单行文本转换成图形对象后的宽高      
      if w > width : width = w       # 记录最大宽度
      height += h                    # 记录总高度
      sizes.append((w,h))
    pic = Image.new('RGBA', (width,height))
    index = 0
    height = 0
    for im in images:                # 刚才按行生成的每个图形对象
      box = (0,height)
      pic.paste(im,box)              # 把im贴在pic上，坐标为box 
      w,h = sizes[index]             # 取出宽高
      height = height + h
      index = index + 1
      
    if filename==None:               # 如果文件名为空则返回图像对象
       return pic
    else:                            # 否则直接保存为图像，并且返回宽高 
       pic.save(filename)
       return pic.size 


def txt4image(txtfile=None,filename=None,fontfile="msyh.ttf",fontsize=18,color=(25,0,255,255),bg=0):
    """把文本文件转换成图像的函数
      txtfile：文本文件名，为空则读取程序文件本身。
      filename：要转换所图像文件名，为空则返回im图像对象。
      fontfile：ttf字体文件，
      fontsize：字体大小
      color：字体颜色
      bg:背景颜色
    """
    if txtfile==None:txtfile=sys.argv[0]
    try:
      f = open(txtfile,encoding='utf-8')
      c = f.read()
      f.close()
    except:
      f = open(txtfile)
      c = f.read()
      f.close()      
    if filename==None:
       return txt3image(c,fontfile=fontfile,fontsize=fontsize,color=color,bg=bg)
    else:
       size = txt3image(c,filename=filename,fontfile=fontfile,fontsize=fontsize,color=color,bg=bg)
       return size

def _convertpos(x,y):
    """把x,y坐标转换回以左上角为原点的x,y坐标，和屏幕的缩放参数scale无关。"""
    if Turtle._screen is None:return
    screen = Screen()            # 返回屏幕对象
    x =  x + screen.window_width() //2
    y =  screen.window_height() //2 - y
    return x,y
  
def _cut_sub_rect(sprite,rect):
    """返回相对于sprite所在矩形的子矩形，当然，只适合于图像造型
       这个子矩形的左上角坐标以sprite左上角坐标为原点的。    
    """         
    left,top,right,bottom = sprite.bbox()
    left1,top1 = _convertpos(left,top)
    left2,top2,right2,bottom2 = rect
    left2,top2 = _convertpos(left2,top2)
    right2,bottom2 = _convertpos(right2,bottom2)
    dleft = int(left2 - left1)
    dtop = int(top2 - top1)
    dright = int(right2 - left1)
    dbottom = int(bottom2 - top1)
    return dleft,dtop,dright,dbottom
  
def _make_mask(sprite,rect,threshold=127):
    """
    sprite：角色，rect：重叠区域矩形(相对于整个屏幕坐标系)
    坐标系以左上角为原点的，截取角色子矩形区域的alpha形成mask
    最后形成的mask是一个numpy二维数组，1代表不透明区域，0代表透明区域。
    threshold是域值，大于这个值，则认为是不透明的，否则为透明。
    """
    im = np.array(sprite._current_im)       # 角色当前的图形对象转换成numpy数组
    
    alpha = im[:, :, 3]                     # 提取所有透明通道的alpha值
    left,top,right,bottom = _cut_sub_rect(sprite,rect) # 相对于角色左上角的子矩形
    
    alpha = alpha[top:bottom,left:right]    # 子矩形的alpha通道所有值
    
    mask = alpha > threshold                # 大于threshold的认为不透明
    mask.dtype=np.uint8                     # 转换成整数
    return (mask,(left,top,right,bottom))   # 返回遮罩和以左上角为原点的相对矩形
  
def mouse_pos():
    """获取相对于海龟屏幕的鼠标指针坐标，和屏幕的缩放参数scale无关。"""    
    if Turtle._screen is None:return
    screen = Screen()            # 返回屏幕对象
    _root = screen._root
    abs_coord_x = _root.winfo_pointerx() - _root.winfo_rootx()
    abs_coord_y = _root.winfo_pointery() - _root.winfo_rooty()
    x =  abs_coord_x - screen.window_width() //2
    y =  screen.window_height() //2 - abs_coord_y
    screen.cv.update()
    return (x-3),(y+3)

mouse_position = mouse_pos
mouseposition = mouse_pos
mousepos = mouse_pos
getmousepos = mouse_pos
getmouseposition = mouse_pos

# 给背景增加坐标定位方法
def _bg_goto(self,x,y):
    """背景坐标定位"""
    self.cv.coords(self._bgpic,(x,-y))    
TurtleScreen.goto = _bg_goto

# 给背景增加获取x坐标方法
def _bg_xcor(self):
    """背景x坐标"""
    p = self.cv.coords(self._bgpic)
    return p[0]
TurtleScreen.xcor = _bg_xcor

# 给背景增加获取y坐标的方法
def _bg_ycor(self):
    """背景y坐标"""    
    p = self.cv.coords(self._bgpic)
    return -p[1]
TurtleScreen.ycor = _bg_ycor

# 给背景增加设定x坐标的方法
def _bg_setx(self,x):
    """设定背景x坐标"""  
    p = self.cv.coords(self._bgpic)
    self.cv.coords(self._bgpic,(x,p[1]))
TurtleScreen.setx = _bg_setx

# 给背景增加设定y坐标的方法    
def _bg_sety(self,y):
    """设定背景y坐标"""        
    p = self.cv.coords(self._bgpic)
    self.cv.coords(self._bgpic,(p[0],-y))
TurtleScreen.sety = _bg_sety
    
# 给背景增加水平移动dx和垂直移动dy的方法  
def _bg_move(self,dx,dy):
    """用于在水平和垂直方向上移动背景,如果dy为0那么只是在水平方向上移动背景"""
    self.cv.move(self._bgpic,dx,-dy)
TurtleScreen.move = _bg_move

# 给背景增加获取绑定盒子的方法
def _bg_bbox(self):
    """获取背景的绑定盒子"""
    b = self.cv.bbox(self._bgpic) # left,top,right,bottom
    return b[0],-b[1],b[2],-b[3]
TurtleScreen.bbox = _bg_bbox


# 以下定义屏幕的鼠标松开事件
def __onscreenrelease(self, fun, num=1, add=None):
    """绑定鼠标的松开事件，默认为鼠标左键，即num为1。
 
    """
    if fun is None:
        self.cv.unbind("<ButtonRelease-%s>" % num)
    else:
        def eventfun(event):
            x, y = (self.cv.canvasx(event.x)/self.xscale,
                    -self.cv.canvasy(event.y)/self.yscale)
            fun(x, y)
        self.cv.bind("<ButtonRelease-%s>" % num, eventfun, add)

def _onscreenrelease(self, fun, btn=1, add=None):
    """绑定鼠标的松开事件，默认为鼠标左键，即num为1。
    """
    self.__onscreenrelease(fun, btn, add)

TurtleScreenBase.__onscreenrelease = __onscreenrelease
TurtleScreenBase.onscreenrelease = _onscreenrelease
 

# 以下重定义TurtleScreen的reset方法
def __TSreset(self):
    """重置除了说话泡泡海龟外的对象到初始状态。    
    """
    for turtle in self._turtles:      
        if turtle.tag != 'bubble':
           turtle._setmode(self._mode)
           turtle.reset()
TurtleScreen.reset = __TSreset

# 缩放矩形函数
def _scale_rect(sourcerect,scale):
    """缩放矩形，按比例对源矩形进行放大或缩小
       sourcerect：源矩形，4元组，左上角和右下角坐标
       scale：比例
    """
    left,top,right,bottom = sourcerect
    width = right - left
    height = top -bottom
    x0 = left + width/2
    y0 = bottom + height/2
    
    x1 = x0 - 0.5 * width * scale
    y1 = y0 + 0.5 * height * scale
    x2 = x0 + 0.5 * width * scale
    y2 = y0 - 0.5 * height * scale

    return x1,y1,x2,y2
  
# 产生一个颜色表，里面的颜色较鲜艳
def makecolors(n=128):
        
    """产生颜色表，饱和度和亮度最高，所以很鲜艳"""
    cs = []
    for y in range(n):
        x = random.random()
        r,g,b = colorsys.hsv_to_rgb(x,1,1)
        r,g,b = int(r*255),int(g*255),int(b*255)
        cs.append((r,g,b))
    cs = ["#{:02x}{:02x}{:02x}".format(r,g,b) for r,g,b in cs]
    cs = list(set(cs))
    return cs
_colorlist = makecolors()     # 产生一个颜色表

class Group(set):
  """组类,继承自集合。取同样标签的对象形成一个集合。"""
  def __init__(self,tag):
    self._tag = tag
    if Turtle._screen  is None:
      self.screen = Screen()        # 如果没有窗口则新建一个窗口
    else:
      self.screen = Turtle._screen      
    self.screen._groups.append(self) # 注意把组添加到了_groups列表中
    self.rebuild()
      
  def rebuild(self):
    """重建标签为self.tag的组"""   
    self.clear()
    [self.add(b) for b in Turtle._screen.turtles() if b._tag==self._tag]

    
class Clock:
    """控制fps的时钟Clock类"""
    def __init__(self):
       self._old_start_time = time.perf_counter()
       self._start_time = time.perf_counter()

    def tick(self,fps=0):
        """返回每帧逝去的时间，如果fps不为0，则会等待直到时间大于1/fps"""
        end_time = time.perf_counter()
        elapsed_time = end_time - self._start_time

        if fps!=0:
            step = 1/fps
            if elapsed_time < step:  # 如果逝去的时间小于step则等待
               time.sleep(step - elapsed_time)
            
        self._old_start_time = self._start_time
        self._start_time = time.perf_counter()
        return time.perf_counter() - self._old_start_time
    
    def getfps(self):
        """得到fps"""
        t = time.perf_counter() - self._old_start_time
        return round(1/t,2)

def rect_overlap(rect1,rect2):
    """
        rect1：矩形1，四元组，左上角坐标和右下角坐标
        rect2：矩形2，四元组，左上角坐标和右下角坐标
        本函数返回矩形相交区域的矩形及面积
    """
    (x11,y11,x12,y12) = rect1     # 矩形1左上角(x11,y11)和右下角(x12,y12) 
    (x21,y21,x22,y22) = rect2     # 矩形2左上角(x21,y21)和右下角(x22,y22)
    
    # 下面求最小的外包矩形
    startx = min(x11,x21)         # 外包矩形在x轴上左边界
    endx = max(x12,x22)           # 外包矩形在x轴上右边界
    starty = min(y12,y22)         # 外包矩形在y轴上上边界
    endy = max(y11,y21)           # 外包矩形在y轴上下边界
    # 想像一下两个矩形隔得比较远，那么外包矩形的宽度是不是肯定大于两个矩形的宽度和呢？
    # 所以，两个矩形相交，它们的宽度和必然大于最小外包矩形的宽度，它们的高度和也是必然大于外包矩形的高度
    width = (x12-x11) + (x22-x21) - (endx-startx)      # (endx-startx)表示外包矩形的宽度
    height = (y11-y12) + (y21-y22) - (endy-starty)   # (endy-starty)表示外包矩形的高度

    if width<=0 or height<=0:    # 不相交
        return tuple()
    else:                        # 相交
        X1 = max(x11,x21)        # 有相交则相交区域位置
        Y1 = min(y11,y21)
        X2 = min(x12,x22)
        Y2 = max(y12,y22)
    
    area = width * height        # 相交区域面积
    return (X1,Y1,X2,Y2,area)
      
# 产生爆炸效果的函数，需要传递图像帧
def explode(pos,frames,interval=100,times=1):
    """
       本函数新建海龟对象，然后把它的造型依次显示为frames中的图形。
       pos：坐标位置二元组或列表，也可以是一个Turtle或它的子类Sprite对象
       frames：序列帧图，
       interval：每帧显示时间
       times：爆炸次数
    """  
    if Turtle._screen is None:return
    if not isinstance(pos,(list,tuple)):
        if isinstance(pos,Turtle):pos = pos.pos()
    if isinstance(frames,str):frames=[frames]
    screen = Screen()                # 返回屏幕对象
    [screen.addshape(im) for im in frames]  # 没有注册此形状则注册
    t = Sprite(visible=False)        # 实例化一个对象    
    t.goto(pos)                      # 坐标定位置
    t.st()                           # 显示出来
    t.index = 0                      # 表示造型索引
    t.frames = frames                # 所有造型
    t.amounts = len(frames)          # 造型数量
    counter = times
    def animation():                 # 切换动画函数   
        nonlocal counter         
        if t.index < t.amounts:            
            t.shape(t.frames[t.index])
            t.index = t.index + 1
            t.screen.ontimer(animation,interval)
        else:
            counter -= 1               # 爆炸次数减一
            if counter > 0:
                t.index = 0
                animation()
            else:
                t.remove()
    animation()

effect = explode                   # 给爆炸效果函数名定义别名

_built_in_images = ["bug.png","ball.png",'cat1.png','cat2.png','bee.png','flower.png',
              'b1.png','b2.png','fighter.png','thunder.png','ufo.png','explosion0.png',
              'explosion1.png','sky.png','rat1.png','rat2.png']
_built_in_images = [os.path.join(_resfld,cms) for cms in _built_in_images]

def _findframes(foldername):
    """本函数返回文件夹下面序列帧图,要求这些图片的文件名形式为
       0.png,1.png,2.png,3.png......
       返回所有图片列表。
    """
    exts = ['.png','.gif','.jpg','.jpeg']
    
    for ext in exts:
        files = glob.glob(foldername + os.sep + '*' + ext)
        if files == []:continue
        frames = []
        for index in range(len(files)):
            file = foldername + os.sep + str(index) + ext
            if os.path.exists(file):
                frames.append(file)

        if frames!=[]:break
    return frames

class Pointer:
    """用于辅助的Pointer类,它能像海龟一样移动"""
    def __init__(self,pos=(0,0),angle=0):
        """
           初始化方法，pos:坐标,angle:角度
        """
        self._angle = angle        # 朝向,也就是和x轴的夹角angle
        self._pos = pos            # 初始坐标               
        
    def setheading(self,angle):
        """设置朝向"""
        self._angle = angle
        
    def heading(self):
        """返回朝向"""
        return self._angle
    
    def right(self,dangle):
        """右转dangle度"""
        self._angle -= dangle
        self.setheading(self._angle)

    def left(self,dangle):
        """左转dangle度"""
        self.right(-dangle)        

    def position(self):
        """返回坐标"""
        return self._pos
    
    def goto(self,x,y=None):
        """到某坐标"""
        if y == None:
            self._pos = x[0],x[1]
        else:
            self._pos = x,y
        
    def forward(self,distance):
        """前进distance距离"""        
        r = math.radians(self._angle)
        dx = distance * math.cos(r)
        dy = distance * math.sin(r)
        x,y = self._pos
        x = x + dx
        y = y + dy
        self._pos = x,y
        
class Sprite(Turtle):
    """
       继承自Turtle的角色类。
       
    """      
    def __init__(self,shape=os.path.join(_resfld,'bug.png'),
                 pos=(0,0) ,visible=True,
                 undobuffersize=_CFG["undobuffersize"],tag='sprite'):
        """
           shape：造型图像(int或str)，pos：起始坐标，visible：可见性，undobuffersize：可撤销次数,tag:标签。
           新建一个精灵，默认为小虫子，在屏幕中央。
        """
        self._id = str(id(self))                        # 唯一标识
        self._initend = False                           # 表示初始化开始
        Turtle.__init__(self,visible=False,undobuffersize=undobuffersize,shape='blank')
        self._stampcors = { }                           # 记录每个图章坐标的字典，键为图章编号 
        self._rotatemode = 0                            # 设定旋转模式，0:360度旋转,1:左右翻转,2:不旋转
        self._im = None                                 # 存储当前原始图形的im属性
        self._imflag = None
        self._current_im = None
        self._shape_raw_name_dict = {}                  # 存储图像文件左右im造型图对象的字典
        self._shapeimsdict = {}                         # 这个字典是存储造型名字和对应的im的
        self._costumes = [ ]                            # 角色自己的造型列表(区别于整个屏幕的) 
        if isinstance(shape,int):
           shape = min(len(_built_in_images)-1, max(0, shape))
           shape = _built_in_images[shape]              # 到这里shape已经变成一个文件名了
           self._costumes = [shape] 
        elif isinstance(shape,str):
             if os.path.isdir(shape):                  # 如果是个文件夹
                self._costumes = _findframes(shape)    # 查看有无0.png,1.png,返回列表
                if self._costumes == []:self._costumes.append('turtle') # 这是补救措施,如果没找到0.png,1.png这样的文件则用turtle造型
             else:                                     # 如果不是文件夹,则认为是文件或者已内置造型
                 if shape not in self.screen._shapes and not os.path.isfile(shape): shape='turtle'
                 self._costumes = [shape] 
        elif isinstance(shape,tuple) or isinstance(shape,list): # 如果传入的是序列
             self._costumes.extend(shape)                              
            
        shape = self._costumes[0]
        self._costumes_amounts = len(self._costumes)    # 造型数量
        self._costume_index = 0                         # 角色的初始造型索引号
        self._position = Vec2D(*pos)
        
        self.shape(shape)        
        
        if visible :
           self.st()
        # 之所以加下面的是由于在隐藏状态下不会在新坐标重画造型
        # 即当实例化Sprite(visible=False,pos=(100,100))时，角色不会到pos的坐标
        # 只是由于它是隐藏的,_drawturtle方法由于_shown是False,就不会在新坐标重画
        # 加下面的代码首先把_shown打开，然后让它为透明状态。这样会在新坐标重渲染
        # 最后改回_shown的False状态。
        else:           
           self._shown = True                          
           self._rotate(0)           
           self._shown = False
           
        self.draggable()                                 # 设置角色为可拖动       
    
        self._sayend = True                              # 初始状态的说话结束 
        self._saycolor = "#303030"                       # 说话的字的颜色
        self._saybordercolor = "#CCCCCC"                 # 说话的字的泡泡边框的颜色        
        self._draw_bubble_turtle = Turtle(visible=False) # 用来画框写字的龟
        self.screen._turtles.remove(self._draw_bubble_turtle) # 又从总表中移除
        self._draw_bubble_turtle.up()                    # 抬起笔来        
        self._draw_bubble_turtle.speed(0)                # 速度最快        
        self._draw_bubble_turtle.pensize(3)        
        self._draw_bubble_turtle._tag = 'bubble'         # 标志为说话泡泡海龟
        self.set_tag(tag)                                # 设置标签
        self._initend = True                             # 表示初始化结束
        self.custom_setup()
        
    def custom_setup(self,p=[]):
        """only user rewrite by lixingqiu @2021/12/1"""
        if p:pass                                     # when rewrite ,replace pass
        
    def draggable(self):
        """设置对象为可拖动的
           如果要设置角色为不可拖动，则设置ondrag为None即可，假设有名为bug的角色，
           那么bug.ondrag(None)，则让角色不可拖动。
        """                  
        self.onclick(self._store, 1)    
        self.ondrag(self.drag,1)
        
    def set_alpha(self,alpha,delay=None):
         """设置alpha值，它是从0到255的值。
            表示图像的透明度，如果不是图像，0代表透明，非0代表不透明。
            如果delay被设置，那么角色在相应时间又会恢复原来的透明度。
          """
         self._oldalpha = self._alpha                   # 记录当前透明度
         alpha = int(min(255, max(0, alpha)))
         self._alpha = alpha
         self._rotate(0)
         # 下面设置当delay有数值的时候让角色过一段时间又恢复原来的透明度
         if delay!=None:            
            if self.screen._ontimer_call_counter < self.screen._ontimer_call_times :
               self.screen._ontimer_call_counter += 1      # 限定ontimer最多调用次数
               self.screen.ontimer(lambda:self.set_alpha(self._oldalpha),int(abs(delay)*1000))
            else:
               print('超过最大异步执行次数，本次延时恢复透明度无效！')
         else:
            self.screen._ontimer_call_counter -= 1

    def get_alpha(self):
         """得到alpha值，它是从0到255的值。"""
         return self._alpha
         
    def set_tag(self,tag=None):
        """给精灵设置标签,并添加到相应的分表"""
        self._tag = tag
        [group.add(self) for group in self.screen._groups
         if self._tag == group._tag]               # 实例化时自动添加到相应组         
          
    def get_tag(self):
        """返回角色的标签""" 
        return self._tag
    
    def rotatemode(self,mode=None):
      """设定旋转模式，无参时返回当前旋转模式。
         0:360度旋转,1:左右翻转,2:不旋转
      """
      if mode == None:
        return self._rotatemode
      if mode <= 0 :
        self._rotatemode = 0
      elif mode >= 2:
        self._rotatemode = 2
      else:
        self._rotatemode = 1      
      
    def collidemouse(self):
      """碰到鼠标指针的检测"""
      left,top,right,bottom = self.bbox()
      xscale = self.screen.xscale
      yscale = self.screen.yscale
      left,top,right,bottom = left*xscale,top*yscale,right*xscale,bottom*yscale
      mx,my = mouse_pos()
      c = mx<= right and mx >= left and my <= top and my >= bottom
      return c

    def pixelcollide(self,other,threshold=127):
      """
        像素级碰撞检测方法，self是主碰方，other是另一个角色，为被碰方。
        本方法用self去碰撞other，other为相对不动的，只适合于图形角色。
        threshold是一个阈值。我们认为超过阈值的为不透明的地方，否则为透明的。
        返回重叠的第一个坐标点，重叠区域矩形，self在此点的像素值,other在此点的像素值。
      """
      t1 = self.screen.cv.type(self.turtle._item)
      if t1!='image' :
        print('本角色不是图形角色！本方法只适合于造型为image的角色')
        return
      t2 = self.screen.cv.type(other.turtle._item)
      if t2!='image':
        print('所碰对象非图形角色，本方法只适合于造型为image的角色')
        return
      bbox1 = self.bbox()                        # 主碰方的绑定盒
      bbox2 = other.bbox()                       # 被碰方的绑定盒
      # 下面ret的值是(left,top,right,bottom,重叠区域面积)
      ret = rect_overlap(bbox1,bbox2)            # 求两矩形的重叠区域(中心为原点)
      if ret:
        mask1,sub_rect1 =  _make_mask(self,ret[:-1],threshold)   # 主碰方的mask和rect1(相对于自己左上角的矩形)
        mask2,sub_rect2 =  _make_mask(other,ret[:-1],threshold)  # 被碰方(相对不动的)
        mask = mask1  + mask2
        array = np.argwhere(mask == 2)           # 所有碰撞点的行列号
        if array.size > 0:
          top,left = array[0]                    # 第一个点的行列号
          top,left = int(top),int(left)
          left1,top1,right1,bottom1 = sub_rect1      #          
          _x1 =  left1 + left                    # 图像以左上角为原点
          _y1 =  top1 + top
          # _x1,_y1是self图形上的坐标点，可以取到它的像素值
          pixel1 = self._current_im.getpixel((_x1,_y1))[:-1]

          left2,top2,right2,bottom2 = sub_rect2
          _x2 =  left2 + left
          _y2 =  top2 + top          
          # _x2,_y2是other图像上在坐标点，可以取到像素值
          pixel2 = other._current_im.getpixel((_x2,_y2))[:-1]
          
          # 下面的hitx,hity是第一个碰撞点的坐标，注意坐标系又变成了以中心为原点
          hitx,hity = ret[0] +left ,ret[1] -top
          return ((hitx,hity),pixel1,pixel2,ret)
      else:
          return None
        
    def coloroverlap(self,color1,color2,sps=[],threshold=127):
        """角色上的某种颜色碰到其它角色上的某颜色碰撞方法,
           color1：三元组,角色上面的一个颜色点
           color2：三元组,表示一种颜色,(这种颜色要是在角色上的,在背景或图章及所画的图形上的颜色就碰不到)
           sps：一些角色，如果列表为空，是默认为对所碰到的所有角色进行检测。
           本程序对背景颜色,图章及所画的各种图形颜色无效,只对角色身上的颜色有效。
        """        
        if sps == []:
            sps = self.find_overlapping_sprites()       # 查找所有和self有矩形重叠的角色
            sps = [s for s in sps if s.screen.cv.type(s.turtle._item) == 'image']
            
        collideflag = False
        for other in sps:              
            bbox1 = self.bbox()                          # 主碰方的绑定盒
            bbox2 = other.bbox()                         # 被碰方的绑定盒
            # 下面ret的值是(left,top,right,bottom,重叠区域面积)
            ret = rect_overlap(bbox1,bbox2)              # 求两矩形的重叠区域(中心为原点)
            if ret:
              mask1,sub_rect1 =  _make_mask(self,ret[:-1],threshold)   # 主碰方的mask和rect1(相对于自己左上角的矩形)
              mask2,sub_rect2 =  _make_mask(other,ret[:-1],threshold)  # 被碰方(相对不动的)
              mask = mask1  + mask2
              array = np.argwhere(mask == 2)             # 所有碰撞点的行列号
              #print(array,array.size)
              for index in range(array.size//2):                 
                 top,left = array[index]                  # 第index个点的行列号
                 top,left = int(top),int(left)
                 left1,top1,right1,bottom1 = sub_rect1      #          
                 _x1 =  left1 + left                      # 图像以左上角为原点
                 _y1 =  top1 + top
                 # _x1,_y1是self图形上的坐标点，可以取到它的像素值
                 pixel1 = self._current_im.getpixel((_x1,_y1))[:-1]

                 left2,top2,right2,bottom2 = sub_rect2
                 _x2 =  left2 + left
                 _y2 =  top2 + top          
                 # _x2,_y2是other图像上在坐标点，可以取到像素值
                 pixel2 = other._current_im.getpixel((_x2,_y2))[:-1]
                
                 # 下面的hitx,hity是第index个碰撞点的坐标，注意坐标系又变成了以中心为原点
                 hitx,hity = ret[0] +left ,ret[1] -top
                 if pixel1 == color1 and pixel2 == color2:
                    collideflag = True
                    break
              if collideflag == True: return (hitx,hity)


    def collidecolor(self,color,sps=[],threshold=127):
        """角色碰到其它角色上的某颜色碰撞方法,           
           color：三元组,表示一种颜色,(这种颜色要是在角色上的,在背景或图章及所画的图形上的颜色就碰不到)
           sps：一些角色，如果列表为空，是默认为对所碰到的所有角色进行检测。
           本程序对背景颜色,图章及所画的各种图形颜色无效,只对角色身上的颜色有效。
        """        
        if sps == []:
            sps = self.find_overlapping_sprites()       # 查找所有和self有矩形重叠的角色             
            sps = [s for s in sps if s.screen.cv.type(s.turtle._item) == 'image']

        collideflag = False
        for other in sps:              
            bbox1 = self.bbox()                          # 主碰方的绑定盒
            bbox2 = other.bbox()                         # 被碰方的绑定盒
            # 下面ret的值是(left,top,right,bottom,重叠区域面积),所以ret[:-1]就是表示一个矩形
            ret = rect_overlap(bbox1,bbox2)              # 求两矩形的重叠区域(中心为原点)             
            if ret:
              mask1,sub_rect1 =  _make_mask(self,ret[:-1],threshold)   # 主碰方的mask和rect1(相对于自己左上角的矩形)
              mask2,sub_rect2 =  _make_mask(other,ret[:-1],threshold)  # 被碰方(相对不动的)
              
              mask = mask1  + mask2
              array = np.argwhere(mask == 2)             # 所有碰撞点的行列号
              for index in range(array.size//2):                 
                 top,left = array[index]                  # 第index个点的行列号
                 top,left = int(top),int(left)
                 left2,top2,right2,bottom2 = sub_rect2
                 _x2 =  left2 + left
                 _y2 =  top2 + top          
                 # _x2,_y2是other图像上在坐标点，可以取到像素值
                 pixel2 = other._current_im.getpixel((_x2,_y2))[:-1]
                 if  pixel2 == color:
                    collideflag = True
                    break
              if collideflag == True: break
        return collideflag
                
    def _store(self,x,y):
        self.clickpos = Vec2D(x,y)
        
    def drag(self,x,y):
        """拖动自己到鼠标指针的坐标"""

        self.ondrag(None)
        neu = Vec2D(x,y)
        self.goto(self.pos() + (neu-self.clickpos))
        self.clickpos = neu
        self.screen.cv.tag_raise(self.turtle._item)
        self.ondrag(self.drag,1)                      
        
    def reset(self):
        if self._initend:old_shown = self._shown
        Turtle.reset(self)
        if self._initend:
           if old_shown: self._shown = True
        self._alpha = 255
        self._rotate(0)
        
    def _loadim(self,image):
        # 原始图形,最好面向右
        self._costumebasename = image
        # self._shape_raw_name_dict  图像文件名对应内存中左右im图形对象的字典
        if self._costumebasename not in self._shape_raw_name_dict:   # 不在这个字典中则第一次加载
            
            self._im = Image.open(image)
            self._im = self._im.convert('RGBA')
            self._imflag = str(self._im).split()[-1][:-1]# 图像内存地址字符串
            self._current_im = self._im            
            # for rotatemode 
            im_mirror = ImageOps.mirror(self._im)        # 镜像造形
            self.rightleftcostume = [self._im,im_mirror] # 左右两个造型表
            self._shape_raw_name_dict[self._costumebasename] = [self._im,im_mirror]           
        else:                              # 在这个字典中,则不读文件,直接从字典中取数据
            
            self._im = self._shape_raw_name_dict[self._costumebasename][0]    # 向右造型
            self._imflag = str(self._im).split()[-1][:-1]
            self._current_im = self._im
            im_mirror = self._shape_raw_name_dict[self._costumebasename][1]   # 向左造型
            self.rightleftcostume =  [self._im,im_mirror]                # 向右向左造型            
            
        self._shapeimsdict[image] = self._im
    def _make_shape_name(self,_wid,_len):
         name = "_".join([self._id , _wid,_len, str(self._orient), str(self._alpha) ,self._costumebasename])
         return name
        
    def shape(self,name=None):
        """重定义shape方法"""
        # 如果名字为空,则返回形状的名称
        if name==None:return Turtle.shape(self,name)

        # 如果是整数，则从内置列表中选择一个 
        if isinstance(name,int):
           name = min(len(_built_in_images)-1, max(0, name))
           name = _built_in_images[name]
           self._loadim(name)

        # 如果名字在形状字典中,而且不是文件.
        if name in self.screen._shapes and not os.path.isfile(name):
            Turtle.shape(self,name)                                                
            self._current_im = self._shapeimsdict.get(name)   # 取出当前im图形对象,_shapeimsdict是造型名字对应im对象字典
            return        
        
        if os.path.isfile(name) : self._loadim(name)
            
        heading = self.heading()           
        stretch_wid,stretch_len ,w = Turtle.shapesize(self)   # 获取缩放值
        new_name = self._make_shape_name(str(stretch_wid),str(stretch_len))
        if os.path.isfile(name):name=new_name
        
        if  new_name==name :
            
            if new_name not in self.screen._shapes:
                #print(name)
                newwidth = max(1,int(self._im.width * stretch_len))
                newheight = max(1,int(self._im.height * stretch_wid))                
                im = self._im.resize((newwidth,newheight),Image.ANTIALIAS)
                
                if self._rotatemode == 0:                    # 360度旋转
                   im = im.rotate(heading,expand=1)                   
                elif self._rotatemode == 2 :                 # 不旋转
                   pass
                elif self._rotatemode == 1:                  # 左右翻转
                     m = self.screen.mode()
                     if m == 'standard' or m == 'world':
                        if heading < 270 and heading > 90:
                           index = 1
                        else:
                           index = 0
                     else:
                        if heading < 180 and heading > 0:
                           index = 0
                        else:
                           index = 1                   
                     im = self.rightleftcostume[index]
                     im = im.resize((newwidth,newheight),Image.ANTIALIAS)
                     
                # 根据透明度进行再次修改图形对象
                if self._alpha != 255:
                   im = _set_im_alpha(im,self._alpha)
                self._shapeimsdict[name] = im               # 把im存入字典(造型名字和im对应的字典) 
                self._current_im = im 
                shape = Shape('image',ImageTk.PhotoImage(im))
                self.screen.addshape(new_name,shape)
                
            Turtle.shape(self,new_name)                       

    def _go(self, distance):
        """重定义_go方法,移动指定距离"""
        ende = self._position + self._orient * distance
        self._goto(ende)
        
    def _rotate(self,angle):
        """seth,right,left最终都要调用它，所以重写它就行了"""
        
        Turtle._rotate(self,angle)         # 调用父类的同名方法
        if self.turtle._type in ['polygon','compound']: return
        if self.shape() == 'blank':return        
                 
        stretch_wid,stretch_len ,w = Turtle.shapesize(self)   # 获取缩放值       
        new_name = self._make_shape_name(str(stretch_wid),str(stretch_len))
        self.shape(new_name)        

    def shapesize(self,stretch_wid=None, stretch_len=None, outline=None):
        """重定义缩放形状方法"""
        x = Turtle.shapesize(self,stretch_wid,stretch_len,outline)
        if hasattr(self,'_im') and self.turtle._type == 'image':
           if stretch_wid != None and stretch_len==None:  stretch_len= stretch_wid
           new_name = self._make_shape_name(str(stretch_wid),str(stretch_len))
           self.shape(new_name)
        return x
    
    def addx(self,dx):
        """横向坐标增加dx"""
        self._goto(Vec2D(self._position[0] + dx, self._position[1]))
         
    def addy(self,dy):
        """纵向坐标增加dy"""
        self._goto(Vec2D(self._position[0], self._position[1] + dy))
        
    def scale(self,s=None):
        """按比例缩放角色的造型"""
        if s == None:
           return self.shapesize()
        else:
           self.shapesize(s,s)

    def gotorandom(self,left=None,right=None,bottom=None,top=None,step=0):
        """到随机坐标,可以包括范围
           left：最左x坐标
           right：最右x坐标
           bottom：最下y坐标
           top：最上y坐标
           step：在矩形范围内定位后再随机确定一个方向前进的步数
        """
        sw = self.screen.window_width()
        sh = self.screen.window_height()
        if left == None:left = -sw//2
        if right == None:right = sw//2
        if right < left : left,right = right,left
        if bottom == None:bottom = -sh//2
        if top == None:top = sh//2
        if top < bottom:top,bottom = bottom,top
        x = random.randint(left,right)
        y = random.randint(bottom,top)
        self.goto(x,y)
        if step!=0:
            angle = self.towards(0,0)
            self.setheading(180+angle)
            self.fd(step)
        
    def wander(self,left=None,right=None,bottom=None,top=None,step=0,speed=1):
      """在窗口的屏幕中漫游,和gotorandom不同的时,这个速度是最慢的
         left:最左x坐标
         right:最右x坐标
         bottom:最下y坐标
         top:最上y坐标
         step:在矩形范围内定位后再随机确定一个方向前进的步数
         speed:移动速度
      """
      oldspeed = self.speed()
      olddelay = self.screen.delay()
      self.speed(speed)
      self.screen.delay(10)
      self.gotorandom(left,right,bottom,top,step)
      self.speed(oldspeed)
      self.screen.delay(olddelay)
      
    def setleft(self,value):
      """设置角色最左x坐标
         value：浮点数据         
      """
      left,top,right,bottom = self.bbox()
      self.setx(value + (right-left)/2)

    def setright(self,value):
      """设置角色最右x坐标
         value：浮点数据
      """
      left,top,right,bottom = self.bbox()
      self.setx(value - (right-left)/2)
      
    def setbottom(self,value):
      """设置角色的最下y坐标
         value：浮点数据
      """
      left,top,right,bottom = self.bbox()
      self.sety(value + (top-bottom)/2)

    def settop(self,value):
      """设置角色的最上y坐标
         value：浮点数据
      """
      left,top,right,bottom = self.bbox()
      self.sety(value - (top - bottom)/2)
      
    def bbox(self,item=None,scale=1):
        """获取画布上对象item的绑定盒
           item：画布上的一个项目(整数或元组)
           scale：缩放系数
        """
        # 如果自己已经被'删除'了直接返回
        sc = self.screen
        if self not in sc._turtles:return
        
        # 如果item为空,则是获取自己的绑定盒
        if item == None: item = self.turtle._item

        xscale = self.screen.xscale
        yscale = self.screen.yscale
        
        if isinstance(item,int):
          box = self.screen.cv.bbox(item)
          if box == None :return
          x0,y0,x1,y1 = box
          left,top,right,bottom = x0/xscale,-y0/yscale,x1/xscale,-y1/yscale
          
        else:                  # 否则就是复合图形
          box = []
          for i in item:
            b = self.screen.cv.bbox(i)
            if b == None : return
            x0,y0,x1,y1 = b
            x0,y0,x1,y1 = x0/xscale,-y0/yscale,x1/xscale,-y1/yscale         
            box.append((x0,y0,x1,y1))
            left = min( [a for a,b,c,d in box] )
            top = max( [b for a,b,c,d in box] )
            right = max( [c for a,b,c,d in box] )
            bottom = min( [d for a,b,c,d in box] )
            
        rect1 = left,top,right,bottom
        if scale!=1:               # 如果缩放系数不是1，那么对矩形进行缩放          
           rect1 = _scale_rect(rect1,scale)
        return rect1
      
    def getleft(self,item=None):
      """获取项目编号或角色的最左x坐标"""
      if item == None: item = self.turtle._item
      left,top,right,bottom = self.bbox(item)
      return left
    
    def getright(self,item=None):
      """获取项目编号或角色的最右x坐标"""
      if item == None: item = self.turtle._item
      left,top,right,bottom = self.bbox(item)
      return right
        
    def getbottom(self,item=None):
      """获取项目编号或角色的最下y坐标"""
      if item == None: item = self.turtle._item
      left,top,right,bottom = self.bbox(item)
      return bottom

    def gettop(self,item=None):
      """获取项目编号或角色的最上y坐标"""
      if item == None: item = self.turtle._item
      left,top,right,bottom = self.bbox(item)
      return top    
    
    def collide(self,other,scale=1):
        """和其它对象的矩形碰撞检测，
           other：是海龟对象或者一个项目item编号，如图章编号。
           scale：other绑定盒的缩放系数
           
        """        
        # 自己的左上右下值
        x0,y0,x1,y1 = self.bbox()
        _left0 = x0
        _top0 = y0
        _right0 = x1
        _bottom0 = y1

        # other要么是其它海龟对象，也可以是个图章！
        if isinstance(other,Turtle):                   
           if other not in self.screen._turtles:return
           item = other.turtle._item
        else:
           item = other

        box = self.bbox(item,scale=scale)
        if box == None :return
        _left1,_top1,_right1,_bottom1 = box

        nocollide = _right0 <= _left1 or _left0 >= _right1 or \
                    _bottom0 >= _top1 or _top0 <= _bottom1
        return not nocollide
      
    def stampcollide(self,item,other,scale=1):
        """
           图章item和other对象的碰撞检测
           item：图章编号
           other：其它图章或精灵对象，如果other是其它图章的编号，
           那么它可能是一个整数或元组，否则它是一个精灵实例。
           scale：other的绑定盒的缩放系数
        """
        if item == other : return True
        
        box = self.bbox(item)   # 图章的绑定盒
        if box == None :return
        _left0,_top0,_right0,_bottom0 = box

        if isinstance(other,int) or isinstance(other,tuple): # 如果other是图章
           item = other
        else:                                                # 否则是一个精灵对象
           item = other.turtle._item
          
        box = self.bbox(item,scale=scale)
        if box == None :return
        _left1,_top1,_right1,_bottom1 = box

        nocollide = _right0 <= _left1 or _left0 >= _right1 or \
                    _bottom0 >= _top1 or _top0 <= _bottom1
        
        return not nocollide        
        
    def heading(self,other=None):
        """获取朝向，或者朝向某个对象与坐标位置。"""
        if other == None :
            return Turtle.heading(self)
        if isinstance(other,Turtle):   # 如果other是海龟对象
            x1,y1 = other.position()   # 获取它的坐标
        elif isinstance(other,tuple) or isinstance(other,list):
            x1,y1 = other
        self.setheading(self.towards(x1,y1))
        
    def topleft(self):
        """到左上角坐标"""
        w = self.screen._window_size()[0]
        h = self.screen._window_size()[1]
        self.goto(-w/2,h/2)
        return self._position

    def topright(self):
        """到右上角坐标"""
        w = self.screen._window_size()[0]
        h = self.screen._window_size()[1]
        self.goto(w/2,h/2)
        return self._position
        
    def bottomleft(self):
        """到左下角坐标"""
        w = self.screen._window_size()[0]
        h = self.screen._window_size()[1]
        self.goto(-w/2,-h/2)
        return self._position

    def bottomright(self):
        """到右下角坐标"""
        w = self.screen._window_size()[0]
        h = self.screen._window_size()[1]
        self.goto(w/2,-h/2)
        return self._position
            
    def arc(self,radius,start=0,extent=45,width=None,fill=None,outline=None):
        """画饼状图
           radius：弧所在圆形的半径
           start：起始角
           extent：角度
           width：边框值
           fill：填充颜色，如果为空字符串，则是没有颜色
           outline：边框颜色，如果为空字符串，则是没有颜色
        """
        if width == None:width = self.pensize()
        if fill == None:fill = self.screen._convertcolor(self.fillcolor())
        if outline == None:outline = self.screen._convertcolor(self.pencolor())
        x,y = self.pos()
        x0,y0 = x - radius,-(y + radius)
        x1,y1 = x + radius, radius - y
        coord = (x0,y0,x1,y1)
        item = self.screen.cv.create_arc(coord, start=start, extent=extent,
                                         fill=fill,width=width,outline=outline)
        self.items.append(item)
        self.screen.cv.tag_raise(self.turtle._item)
        if self.undobuffer:
            self.undobuffer.push(("arc", item))
            
        return item
      
    def polygon(self,coords=None,width=None,fill=None,outline=None):
        """连点画多边形
           coords：多边形顶点坐标,如果是简单二元组,那第一个数值代表边数,第二个数值代表边长
           width：边框值
           fill：填充颜色，如果为空字符串，则是没有颜色
           outline：边框颜色，如果为空字符串，则是没有颜色           
        """
        if width == None:width = self.pensize()
        if fill == None:fill = self.screen._convertcolor(self.fillcolor())
        if outline == None:outline = self.screen._convertcolor(self.pencolor())
        if coords == None:coords = (random.randint(3,12),random.randint(10,50))
        # 如果用户写成polygon(4,100)这样的形式的一种纠正代码
        if isinstance(coords,int):     # 如果coords只是个整数
           coords = (coords,width)
           width = self.pensize()
           
        x,y = self.pos()
        if len(coords) == 2:           # 如果是简单的2元组,用Pointer类实例化算出各个顶点坐标
           n = coords[0]               # 边数
           if isinstance(n,(int,float)):
              length = coords[1]        # 边长
              x,y = self.position()     # 正多边形第一个点坐标
              angle = self.heading()    # 斜度
              t = Pointer((x,y),angle)  # 新建t用来记录个各顶点
              cors = []
              for _ in range(n):
                x, y = t.position()
                cors.append((x,-y))
                t.forward(length)
                t.left(360/n)
           else:
                cors = [x,-y]
                for x, y in coords:
                   cors.append(x )
                   cors.append(-y)
        else:            
            cors = [x,-y]
            for x, y in coords:
               cors.append(x )
               cors.append(-y)
            
        item = self.screen.cv.create_polygon(cors, fill=fill,width=width,outline=outline)
        self.items.append(item)
        self.screen.cv.tag_raise(self.turtle._item)
        if self.undobuffer:
            self.undobuffer.push(("polygon", item))
        return item
      
    def oval2(self,a,b=None,width=None,fill=None,outline=None):
        """ 以角色为中心点画椭圆,这个方法不会根据角色的方向对椭圆进行倾斜,所以速度快.
            a:长半轴,b:短半轴,
            width:边框像素值 
            fill:填充颜色,如果为空字符串,则无颜色
            outline:边框颜色,如果为空字符串,则无颜色            
        """
        if b == None : b = a
        if width == None:width = self.pensize()
        if fill == None:fill = self.screen._convertcolor(self.fillcolor())
        if outline == None:outline = self.screen._convertcolor(self.pencolor())
        x,y = self.pos()
        x0,y0 = x-a,-y-b
        x1,y1 = x+a,b-y
        item = self.screen.cv.create_oval(x0,y0,x1,y1,fill=fill,width=width,outline=outline)
        self.screen.cv.tag_raise(self.turtle._item)
        self.items.append(item)
        if self.undobuffer:
            self.undobuffer.push(("oval2", item))
        return item
      
    def oval(self,a,b=None,width=None,fill=None,outline=None):
        """以角色为中心点画椭圆,这个方法会根据角色的方向对椭圆进行倾斜,所以速度慢
            a:长半轴,b:短半轴,
            width:边框像素值 
            fill:填充颜色,如果为空字符串,则无颜色
            outline:边框颜色,如果为空字符串,则无颜色
        """
        if b == None : b = a
        if width == None:width = self.pensize()
        if fill == None:fill = self.screen._convertcolor(self.fillcolor())
        if outline == None:outline = self.screen._convertcolor(self.pencolor())
        
        cx,cy = self.pos()                 # 中心点坐标
        cors = []                          # 多边形坐标点
        k = math.radians(self.heading())   # 椭圆的倾斜角度
        for t in range(361):
          j= math.radians(t) 
          x = cx + a*math.cos(j)*math.cos(k)-b*math.sin(j)*math.sin(k) 
          y = cy + a*math.cos(j)*math.sin(k)+b*math.sin(j)*math.cos(k)
          cors.append(x)
          cors.append(-y)
        item = self.screen.cv.create_polygon(cors, fill=fill,width=width,outline=outline)
        self.items.append(item)
        self.screen.cv.tag_raise(self.turtle._item)
        if self.undobuffer:
            self.undobuffer.push(("oval", item))
        return item      
          
    def dot(self,size=None,*color):
        """打圆点命令(这是重定义的，原turtle.py没有定义screen._dot，本程序定义了这个方法也重定义一下dot,返回item号。
        可选参数:
        size -- 整数 >= 1 (if given)，代表圆点直径。
        color -- 颜色字符串或三元组
        """
        if not color:
            
            if isinstance(size, (str, tuple)):                
                color = self._colorstr(size)                
                size = self._pensize + max(self._pensize, 4)
            else:
                color = self._pencolor
                if not size:
                    size = self._pensize + max(self._pensize, 4)
        else:
            if size is None:
                size = self._pensize + max(self._pensize, 4)
            color = self._colorstr(color)

        item = self.screen._dot(self._position, size, color)
        self.items.append(item)
        self.screen.cv.tag_raise(self.turtle._item)
        if self.undobuffer:
            self.undobuffer.push(("dot", item))
            
        return item
      
    def _undo(self, action, data):
        """undo()命令实际执行的代码
        """
        if self.undobuffer is None:
            return
        if action == "rot":
            angle, degPAU = data
            self._rotate(-angle*degPAU/self._degreesPerAU)
            dummy = self.undobuffer.pop()
        elif action == "stamp":
            stitem = data[0]
            self.clearstamp(stitem)
        elif action == "go":
            self._undogoto(data)
        elif action in ["wri", "dot","arc","polygon","oval","oval2"]:
            item = data[0]
            self.screen._delete(item)
            self.items.remove(item)
        elif action == "dofill":
            item = data[0]
            self.screen._drawpoly(item, ((0, 0),(0, 0),(0, 0)),
                                  fill="", outline="")
        elif action == "beginfill":
            item = data[0]
            self._fillitem = self._fillpath = None
            if item in self.items:
                self.screen._delete(item)
                self.items.remove(item)
        elif action == "pen":
            TPen.pen(self, data[0])
            self.undobuffer.pop()
            
    def randomcolor(self):
        """设定随机颜色"""        
        c = random.choice(_colorlist)        
        self.color(c)

    def randomheading(self):
        """设定随机方向"""
        fx = random.randint(1,360)
        self.setheading(fx)
        
    def _display_bubble(self,item):      
        """画说话泡泡"""
        margin = 10
        r = 10
        rect = self.bbox(item)
        if rect == None : return
        left,top,right,bottom = rect
        mode = self.screen.mode()
        if mode=='standard':
          pass
        else:
          self._draw_bubble_turtle.setheading(90)
        
        left = left - margin
        right = right + margin
        top = top + margin
        bottom = bottom - margin
        self._draw_bubble_turtle.color(self._saybordercolor)
        width = right - left
        centerx = left + width//2
        self._draw_bubble_turtle.goto(left+r,top)    # 1 左上角右偏r点
        self._draw_bubble_turtle.pendown()
        self._draw_bubble_turtle.goto(right-r,top)   # 2 右上角左偏r点
        self._draw_bubble_turtle.circle(-r,90)       # 右上角圆角，方向变为向下
        self._draw_bubble_turtle.goto(right,bottom+r)# 3 右下角上偏r点
        self._draw_bubble_turtle.circle(-r,90)       # 右下角圆角，方向变为向左
        self._draw_bubble_turtle.goto(centerx + r*2,bottom) # 4 中下 右偏2r点
        
        self._draw_bubble_turtle.circle(2*r,90)      # 方向变为向下
        self._draw_bubble_turtle.right(180)
        self._draw_bubble_turtle.circle(2*r,90)      # 方向为向左了 
        
        self._draw_bubble_turtle.goto(left+r,bottom) # 5 左下角 右偏r点
        self._draw_bubble_turtle.circle(-r,90)       # 向右画1/4圆，方向为向上了 
        self._draw_bubble_turtle.goto(left,top-r)    # 6 左上角 下偏r点
        self._draw_bubble_turtle.circle(-r,90)       # 向右画1/4圆，方向为向右了
        
        self._draw_bubble_turtle.up()

    def _redraw_say(self):
        """重画字和说话泡泡"""
        # 如果自己已经被'删除'了直接返回
        sc = self.screen
        if self not in sc._turtles:return

        self._draw_bubble_turtle.clear()      # 擦除以前所说的话
        self.screen.tracer(False)
        left,top,right,bottom = self.bbox()   # 自己的绑定盒子 
        centerx = left + (right - left)//2
        top = top + 40
        self._draw_bubble_turtle.goto(centerx,top)        
        self._draw_bubble_turtle.color(self._saycolor)   # 要说的话的背景色          
        item = self._draw_bubble_turtle.write(self._sayinfo,align='center')
        
        self._display_bubble(item)           # 画说话泡泡框
        self.screen.tracer(True)        
      
    def _wait_say(self):        
        """不断地判断是否改变了坐标,变了就得重画,否则干等"""
        # 如果自己已经被'删除'了直接返回
        sc = self.screen
        if self not in sc._turtles:return
        
        if self._sayend == True : return
        if time.time() -  self._begin_bubble_time < self._saytime:
           # 如果坐标改变了,那么重画说话泡泡和字
           if abs(self.xcor() - self._oldsay_x) > 0 or \
              abs(self.ycor() - self._oldsay_y) > 0 or \
              self.bbox() != self._oldbox :  
              self._oldsay_x = self.xcor()
              self._oldsay_y = self.ycor()
              self._oldbox = self.bbox()
              self._redraw_say()
           self.screen.ontimer(self._wait_say,100)
        else:           
           self._sayend = True
           self._sayinfo = ""
           self._draw_bubble_turtle.clear()
           
    def say(self,info='你好',delay=2,wait=True):
        """在头顶上显示要说的话 ,默认为阻塞进程。"""
        if len(info)<6:info = "  " + info + "  "
        if self._sayend == False:     # 如果上次还没说完又调用了say,(说明wait为False)
           self._sayend = True
           self._sayinfo = info
           self._saytime = delay
           self._begin_bubble_time = time.time()
           #  用于改变位置了才重画的三个变量
           self._oldsay_x = self.xcor()
           self._oldsay_y = self.ycor()
           self._oldbox = self.bbox()   # 绑定盒变了也要重画
           self._redraw_say()
           self._sayend = False          # 描述说话是否结束
           self._wait_say()
           if wait :               
             while time.time() - self._begin_bubble_time < self._saytime:
                print
                self.screen.update()
           return
        self._sayend = False          # 描述说话是否结束
        self._sayinfo = info
        self._saytime = delay
        self._begin_bubble_time = time.time()
        #  用于改变位置了才重画的三个变量
        self._oldsay_x = self.xcor()
        self._oldsay_y = self.ycor()
        self._oldbox = self.bbox()   # 绑定盒变了也要重画
        self._redraw_say()
        self._wait_say()
        # 如果wait为真，则阻塞程序的运行
        if wait :               
           while time.time() - self._begin_bubble_time < self._saytime:
              print
              self.screen.update()
              
    def saycolor(self,color=None):
        """说话的颜色，如果无参数，则返回当前说话的字的颜色"""
        if color == None:return self._saycolor
        self._saycolor = color
        if not self._sayend: self._redraw_say()

    def saybordercolor(self,color=None):
        """说话泡泡边框的颜色，如果无参数，则返回当前说话泡泡边框的颜色"""
        if color == None:return self._saybordercolor
        self._saybordercolor = color
        if not self._sayend: self._redraw_say()   
      
    def remove(self):
        """从海龟列表_turtles和其相应的组中移除"""
        self.hideturtle()
        self.reset()
        
        sc = self.screen
        if self not in sc._turtles:return
        self.screen.cv.delete(self.drawingLineItem)
        self.screen.cv.delete(self.currentLineItem)
        for _ in self.items:
          self.screen.cv.delete(_)
        self.clearstamps()
        self._poly = None
        self._creatingPoly = False
        self._fillitem = self._fillpath = None
        self.currentLineItem = None
        self.currentLine = None
        self.items = None
        self.stampItems = None
        self._stampcors = None
        self._undobuffersize = None
        self.undobuffer = None       
        self.rightleftcostume = None
        self._im = None
        self._current_im = None
        
        # 在造型字典中删除这个角色所有存在过的造型
        if  self._imflag is not None:
           [self.screen._shapes.pop(sp) for sp in self.screen._shapes.copy()  if self._imflag in sp]
        
        self._draw_bubble_turtle.reset()
        self.screen.cv.delete(self._draw_bubble_turtle.drawingLineItem)
        self.screen.cv.delete(self._draw_bubble_turtle.currentLineItem)
        for _ in self._draw_bubble_turtle.items:
          self.screen.cv.delete(_)
        for _ in self._draw_bubble_turtle.stampItems:
          self.screen.cv.delete(_)          
        self._draw_bubble_turtle.drawingLineItem = None        
        self._draw_bubble_turtle._poly = None
        self._draw_bubble_turtle._creatingPoly = False
        self._draw_bubble_turtle._fillitem = self._fillpath = None
        self._draw_bubble_turtle.currentLineItem = None
        self._draw_bubble_turtle.currentLine = None
        self._draw_bubble_turtle.items = None
        self._draw_bubble_turtle.stampItems = None
        self._draw_bubble_turtle._undobuffersize = None
        self._draw_bubble_turtle.undobuffer = None

        sc.cv.delete(self._draw_bubble_turtle.turtle._item) # 从画布上删除说话泡泡的形状(虽然它是隐藏的)
        self._draw_bubble_turtle.turtle = None 
        sc.cv.delete(self.turtle._item)                     # 从画布上删除自己的形状
        self.turtle = None
         
        self._tag = None
        sc._turtles.remove(self)                            # 在屏幕的_turtles列表中移除自己
        for group in self.screen._groups:
           if self in group:group.remove(self)
       
    def draw_rect(self,width,height,fill=True):
      """画矩形
         width：矩形宽度，height：矩形高度,fill：是否填充         
      """
      down = self.isdown()                        # 记录先前的画笔是否落笔      
      self.pendown()
      if fill:self.begin_fill()
      for _ in range(2):
        self.fd(width)
        self.left(90)
        self.fd(height)
        self.left(90)      
      if fill:self.end_fill()
      self.penup()      
      if down:self.pendown()                          
       
    def reborn(self,x,y,dx=0,dy=0,delay=None):
        """移到新的坐标，让对象能复用的方法。
           本方法可以和move方法配合，当敌人死时，在新的坐标重生，
           而不是再实例化一个对象。
        """
        self.hide(delay)
        self.dx = dx
        self.dy = dy
        self.goto(x,y)
        if delay==None:self.showturtle()
        
    def stampbbox(self,sitem):
        """返回图章的left,top,right,bottom值"""
        if sitem not in self.stampItems: return
        return self.bbox(sitem)
      
    def stampcors(self,sitem):
        """返回图章的中心点坐标值"""
        if sitem not in self.stampItems: return
        x,y = self._stampcors[sitem]           
        return x,y 
    
    def stampgoto(self,sitem,x,y=None):
        """图章定位到x,y坐标"""
        
        if sitem not in self.stampItems: return
        if y is None:x,y = x
        
        shape = self.screen._shapes[self.turtle.shapeIndex]
        canvas = self.screen.cv
        xscale = self.screen.xscale
        yscale = self.screen.yscale        
        oldx,oldy = self.stampcors(sitem)      # 从_stampcors字典取出老的坐标
        dx = x - oldx                          # 算出相对水平距离
        dy = y - oldy                          # 算出相对垂直距离          
        if shape._type == 'image':                     
           canvas.coords(sitem,(x * xscale, - y * yscale))
        elif shape._type == 'polygon':
          points = self.screen._pointlist(sitem) # 多边形每个顶点
          points = [ (xscale * (x+dx),-yscale * (y+dy)) for (x,y) in points]
          dots = []
          for x0,y0 in points:
             dots.append(x0)
             dots.append(y0)          
          canvas.coords(sitem,dots)         
          
        elif shape._type == 'compound':
          for item in sitem:
              points = self.screen._pointlist(item) # 多边形每个顶点
              points = [ (xscale * (x+dx),-yscale * (y+dy)) for (x,y) in points]
              dots = []
              for x0,y0 in points:
                 dots.append(x0)
                 dots.append(y0)          
              canvas.coords(item,dots)
        self._stampcors[sitem] = x,y
    
    def stampmove(self,sitem,dx,dy):
        """移动图章dx和dy的距离，别名movestamp"""
        if sitem not in self.stampItems: return
        
        xscale = self.screen.xscale
        yscale = self.screen.yscale
        
        if isinstance(sitem,int):   # image和polygon的item号都是整数
            self.screen.cv.move(sitem,xscale * dx,- yscale * dy)
        else:
          # 否则是复合图形
          for item in sitem:
            self.screen.cv.move(item,xscale * dx,- yscale * dy)

        x,y = self._stampcors[sitem]                        # 取出坐标
        self._stampcors[sitem] = x + xscale * dx , y + yscale * dy  # 跟踪坐标

    def stampslide(self,sitem,pos,delay=2000):
        """图章的滑行到指定坐标方法,别名为stampglide
           sitem：图章编号
           pos：坐标
           delay：以毫秒为单位的滑行总时间
           在规定的时间内滑动到坐标，无返回值。
        """
        tracer = self.screen.tracer()
        old_delay = self.screen.delay()     # 获取当前绘画延时时间
        self.screen.delay(0)
        delay = abs(delay)    
        if delay > 0:
          delay = int(delay)
          destx,desty = pos
          sx,sy = self.stampcors(sitem)     # 获取图章的x,y坐标
          h_distance = pos[0] - sx
          v_distance = pos[1] - sy
          dx = h_distance/delay              # 每毫秒在水平方向移动的距离
          dy = v_distance/delay              # 每毫秒在垂直方向移动的距离  
          for _ in range(delay):
            self.movestamp(sitem,dx,dy)            
            if tracer!=0:self.screen.cv.update()            
            time.sleep(0.001)      
        else:
            self.stampgoto(sitem,destx,desty)
        self.screen.delay(old_delay)
        
        
    def stamp(self,delay=None):
        """盖图章，并返回图章编号，它可能是一个整数也可能是个元组。
           如果delay不为None，则会在delay秒后自动清除图章
        """
        stitem = Turtle.stamp(self)
        #self.screen.cv.tag_lower(stitem)
        self._stampcors[stitem] = self.position()    # 初始坐标
        
        if delay != None:                 
               self.screen.ontimer(lambda:self.clearstamp(stitem),int(abs(delay)*1000))         
        return stitem
      
    def clearstamp(self, stampid):
        """根据给定的图章编号删除图章,这是重定义的方法。
        """
        if self not in self.screen._turtles:return # 角色被'删除'了则直接返回   
        self._clearstamp(stampid)
        if stampid in self._stampcors:
           self._stampcors.pop(stampid)   # 加上从记录图章坐标的字典中弹出这个图章
        self._update()
        
    def hidestamp(self,stampid):
        """隐藏图章"""
        self.screen.cv.itemconfigure(stampid, state='hidden')
        
    def showstamp(self,stampid):
        """显示图章"""
        self.screen.cv.itemconfigure(stampid, state='normal')

    def stampishide(self,stampid):
        """图章是否隐藏"""
        status = self.screen.cv.itemconfigure(stampid)['state']
        status = status[4]
        if status=="" or status=='normal':
          return False
        else:
          return True
        
    def collide_edge(self,item=None):
        """检测自己或自己的图章是否碰到边缘"""
        box = self.bbox(item)
        if box == None: return
        left,top,right,bottom = box
        sw = self.screen.window_width()
        sh = self.screen.window_height()
        c1 = left <= -sw//2
        c2 = right >= sw//2
        c3 = top >= sh//2
        c4 = bottom <= -sh//2
        return c1 or c2 or c3 or c4

    def collide_others(self,tag_or_group,scale=1):
       """
       碰到其它的精灵，
       tag_or_group是用于给精灵分组的字符串或组名。
       """
       retlist = []
       if isinstance(tag_or_group,str):
          others = [obj for obj in self.screen.turtles() if obj._tag==tag_or_group]
       elif isinstance(tag_or_group,set):
          others = tag_or_group
          
       for obj in others:
         if self == obj:continue
         if self.collide(obj,scale=scale):
            retlist.append(obj)
       return retlist
      
    def bounce_on_edge(self):
        """当角色用fd命令前进时，配合这个命令让角色自动碰到边缘就反弹"""
        if self not in self.screen._turtles: return
        mode = self.screen.mode()
        hd = self.heading()
        left,top,right,bottom = self.bbox()
        sw = self.screen.window_width()
        sh = self.screen.window_height()
        c1 = left < -sw//2
        c2 = right > sw//2
        
        c3 = top > sh//2
        c4 = bottom < -sh//2
        
        if (c1 or c2) and (c3 or c4): # 同时碰到反转
            self.right(180)
            return
        if c1 or c2:                  # 根据screen模式需要加代码
          self.setheading(180-hd)
          return 
        elif c3 or c4:
          self.setheading(0-hd)
     
    def shapeindex(self,index=0):
      """设定造型编号"""      
      self._costume_index = index % self._costumes_amounts      
      self.shape(self._costumes[self._costume_index])
      return self._costumes[self._costume_index]
    
    def randomshape(self):
      """随机设定一个造型,并且返回造型名称"""      
      self._costume_index = random.randint(0,self._costumes_amounts-1)    
      self.shape(self._costumes[self._costume_index])
      return self._costumes[self._costume_index]
    
    def nextshape(self):
      """下一个造型"""
      self._costume_index += 1
      self._costume_index %= self._costumes_amounts
      self.shape(self._costumes[self._costume_index])
      return self._costumes[self._costume_index]
      
    def previousshape(self):
      """上一个造型"""
      self._costume_index -= 1
      self._costume_index %= self._costumes_amounts
      self.shape(self._costumes[self._costume_index])
      return self._costumes[self._costume_index]
     
    def clone(self):
        """重定义clone方法，无参。
        在同一位置创建并返回属坐标、朝向等属性一致的对象。
        举例 (假设有一个海龟对象叫mick):
        mick = Turtle()
        joe = mick.clone()
        """
        screen = self.screen
        self._newLine(self._drawing)

        turtle = self.turtle
        self.screen = None
        self.turtle = None  # too make self deepcopy-able

        # added，对象不能深度复制，所以需要先保存，清为None，再deepcopy
        old_draw_bubble_turtle = self._draw_bubble_turtle

        if self._im == None:
            old_im = self._im
            old_current_im = self._current_im
        else:
           if hasattr(self._im,'copy'):
               old_im = self._im.copy()
               old_current_im = self._current_im.copy()
           else:
               old_im = self._im
               old_current_im = self._current_im
        
        self._draw_bubble_turtle = None # too make self deepcopy-able
        self._im = None
        self._current_im = None
        
        q = deepcopy(self)
        # 恢复
        self.screen = screen
        self.turtle = turtle
        # added
        self._draw_bubble_turtle = old_draw_bubble_turtle
        self._im = old_im
        self._current_im = old_current_im
        
        q.screen = screen
        q.turtle = _TurtleImage(screen, self.turtle.shapeIndex)
        
        # added
        if hasattr(old_im,'copy'):
            q._im = old_im.copy()
            q._current_im = old_current_im.copy()
        else:
            q._im = old_im
            q._current_im = old_current_im
         
        q._draw_bubble_turtle = Turtle(visible=False) # 用来画框写字的龟
        screen._turtles.remove(q._draw_bubble_turtle)
        q._draw_bubble_turtle.up()                    # 抬起笔来        
        q._draw_bubble_turtle.speed(0)                # 速度最快        
        q._draw_bubble_turtle.pensize(2)
        # 以下防止在使用screen.mode调用reset时显示出来用的
        q._draw_bubble_turtle._tag = 'bubble'          # 标志为说话泡泡海龟        
       
        screen._turtles.append(q)
        screen.cv.delete(q.turtle._item)
        ttype = screen._shapes[self.turtle.shapeIndex]._type
        if ttype == "polygon":
            q.turtle._item = screen._createpoly()
        elif ttype == "image":
            q.turtle._item = screen._createimage(screen._shapes["blank"]._data)
        elif ttype == "compound":
            q.turtle._item = [screen._createpoly() for item in
                              screen._shapes[self.turtle.shapeIndex]._data]        
        q.drawingLineItem = screen._createline()
        q._id = str(id(q))        
        q.draggable()
        q.set_tag(q._tag)
        q._update()
       
        return q

    def _hidedelay(self):
        """下面的show方法有delay参数时，延时隐藏调用的，请不要单独调用。"""
        self.screen._ontimer_call_counter -= 1
        if self not in self.screen._turtles:return # 角色被'删除'了则直接返回 
        self.hideturtle()        
        
    def show(self,delay=None):
        """显示角色一定的时间。
           delay：以秒为单位的整数，如果为None，则只是显示。
           如果是大于0的数值则有delay秒后隐藏。
        """
        self.showturtle()
        if delay != None:
            if self.screen._ontimer_call_counter < self.screen._ontimer_call_times :
               self.screen._ontimer_call_counter += 1      
               self.screen.ontimer(self._hidedelay,int(abs(delay)*1000))
            else:
               print('超过最大异步执行次数，本次延时隐藏无效！')

    def _showdelay(self):
        """下面的hide方法有delay参数时，延时显示调用的，请不要单独调用。"""
        self.screen._ontimer_call_counter -= 1
        if self not in self.screen._turtles:return # 角色被'删除'了则直接返回 
        self.showturtle()
        
    def ishide(self):
        """返回是否是隐藏"""
        return not self.isvisible()
    
    def hide(self,delay=None):
        """隐藏角色一定的时间
           delay：以秒为单位的整数，如果为None，则只是隐藏。
           如果是大于0的数值则有delay秒后显示。
        """
        self.hideturtle()
        # 清除说话泡泡
        self._sayend = True
        self._sayinfo = ""
        self._draw_bubble_turtle.clear()       
        if delay != None:
            if self.screen._ontimer_call_counter < self.screen._ontimer_call_times :
               self.screen._ontimer_call_counter += 1      
               self.screen.ontimer(self._showdelay,int(abs(delay)*1000))
            else:
               print('超过最大异步执行次数，本次延时显示无效！')
               
    def write2(self, arg, move=False, fg='black',bg='white',dx=1,dy=-1,
               align="center", font=("宋体",16,"normal"),angle=0):
        """写阴影字"""
        
        pencolor,fillcolor = self.color()           # 记录先前颜色
        oldx,oldy = self.position()                 # 记录先前坐标
        self.pencolor(bg)
        self.write(arg,move=move,align=align,font=font,angle=angle)
        self.goto(oldx+dx,oldy+dy)
        self.pencolor(fg)
        self.write(arg,move=move,align=align,font=font,angle=angle)
        self.goto(oldx,oldy)
        self.color(pencolor,fillcolor)        
               
    def wait(self,delay=0.01):
        start_time = time.time()
        while time.time() - start_time < delay:
              print
              try:
                self.screen.update()
              except:
                pass
              
    def contained(self):
        """返回角色矩形内所有的items"""
        self.update()        
        x1, y1, x2, y2 = self.screen.cv.bbox(self.turtle._item)
        tapou = set(self.screen.cv.find_enclosed(x1,y1,x2,y2))  #  角色矩形内所有items
        allitems = set(self.screen._finditems())        
        tapou.remove(self.turtle._item)
        return tapou.intersection(allitems)

    def contain(self,item):
       """判断角色是否包含item,
          item：整数或一个角色，表示项目编号
       """
       if isinstance(item,Turtle):
         item = item.turtle._item
       allitems = self.contained()
       if item in allitems :
         return True
       else:
        return False       
        
    def overlap_with(self,items):
        """查找有没有和items进行矩形重叠
           items是列表或元组或集合或整数或字符串
        """
        self.update()
        #返回所有与限定矩形有重叠的画布对象的item编号
        x1, y1, x2, y2 = self.screen.cv.bbox(self.turtle._item)
        tapou =  set(self.screen.cv.find_overlapping(x1,y1,x2,y2))
        tapou.remove(self.turtle._item)
        if isinstance(items,int):
           allitems = {items}
        elif isinstance(items,(tuple,list,set)):
           #print('items',items)
           items = tuple(items)           
           if len(items)>0:                 # 如果不是空的              
              if isinstance(items[0],(Turtle,Sprite)):                  
                 allitems = {sp.turtle._item for sp in items}                 
              else:
                 allitems = set(items)
           else:
               allitems = set()
        elif isinstance(items,Turtle):
           allitems = {items.turtle._item}
        elif isinstance(items,str):
          allitems = {sp.turtle._item for sp in  self.screen._turtles if sp._tag==items}
            
        return tapou.intersection(allitems)
        
    def find_overlapping(self,exclude=None):
        """查找自己有没有和画布上其它的对象有矩形重叠
           exclude：列表或元组或一个整数或角色，写上要排除的角色或item编号
        """
        self.update()
        allitems = set(self.screen._finditems())
        if exclude!=None:
           exlist = set()                   # 待排除集合
           if isinstance(exclude,int):
               exlist.add(exclude)
           elif isinstance(exclude,tuple) or  isinstance(exclude,list):
               for item in exclude:
                 if isinstance(item,int):       # 如果是整数，直接加到集合
                   exlist.add(item)
                 elif isinstance(item,Turtle):  # 如果是Turtle实例则把它的_item加到集合
                   exlist.add(item.turtle._item)
           elif isinstance(exclude,Turtle):
               exlist.add(exclude.turtle._item)
           elif isinstance(exclude,str):        # 如果是字符串,视为同一类型角色的标签
              exlist = {sp.turtle._item for sp in  self.screen._turtles if sp._tag==exclude}

           allitems = allitems - exlist         # 求差集 
        x1, y1, x2, y2 = self.screen.cv.bbox(self.turtle._item)
        #返回所有与限定矩形有重叠的画布对象的item编号
        tapou =  set(self.screen.cv.find_overlapping(x1,y1,x2,y2))
        tapou.remove(self.turtle._item)
        return tapou.intersection(allitems)
      
    def find_overlapping_sprites(self,exclude=None):
         """查找和self有矩形重叠的角色"""
         items = self.find_overlapping(exclude=exclude) # 找到的是角色和其它item，如图章等。
         sps = [t for t in self.screen._turtles if hasattr(t,"_id")]  # 所有的角色       
         return [sp for sp in sps if sp.turtle._item in items]        # 挑出和self有矩形重叠的角色
        
    def _drawline(self,p1,p2):
        """画线条的方法"""
        isdown = self.isdown()           # 记录先前落笔状态
        self.up()
        self.goto(p1)
        self.down()
        self.goto(p2)
        # 恢复先前落笔状态
        if isdown:
           self.down()
        else:
           self.up()

    def saveshape(self,imgname,x=1,y=1):
        """imgname：图像文件名，x：横向缩放系数，y：纵向缩放系数
           本方法保存角色当前造型图片,只支持image类型角色,并且只能放大。
           支持保存为PGM,PPM,GIF,PNG图像文件格式。
        """
        im = self._current_im
        w,h = im.size
        w = int(w * x)
        h = int(h * y)
        im = im.resize((w,h),Image.ANTIALIAS)
        im.save(imgname) 
      
    def draw_grid(self,dx=100,dy=100):
      """满屏画格子的方法,本方法会在屏幕上画满格子。
      """
      isdown = self.isdown()           # 记录先前落笔状态
      pos = self.pos()                 # 记录先前坐标
      
      width = self.screen.window_width()
      height = self.screen.window_height()
      # 画中横线
      leftcenter = -width/2,0
      rightcenter = width/2,0
      self._drawline(leftcenter,rightcenter)

      # 画中竖线
      bottomcenter = 0,-height/2
      topcenter = 0,height/2
      self._drawline(bottomcenter,topcenter)

      # 画上横线
      for y in range(dy,height//2,dy):
        p1 = -width/2 ,y
        p2 = width/2,y
        self._drawline(p1,p2)
        
      # 画下横线
      for y in range(-dy,-height//2,-dy):
        p1 = -width/2 ,y
        p2 = width/2,y
        self._drawline(p1,p2)
        
      # 画右竖线
      for x in range(dx,width//2,dx):
        p1 = x,-height/2
        p2 = x,height/2
        self._drawline(p1,p2)
      # 画左竖线
      for x in range(-dx,-width//2,-dx):
        p1 = x,-height/2
        p2 = x,height/2
        self._drawline(p1,p2)
      self.penup()        

      # 恢复原来坐标
      self.goto(pos)
      # 恢复先前落笔状态
      if isdown:
        self.down()
      else:
        self.up()

    def draw_grid2(self,rows=8,cols=8,dx=50,dy=50):
       """
          按行数和列数及格子边长画格子的方法。
          rows：行数，cols：列数，dx：格子宽度，dy：格子高度
       """
       grid_width = cols * dx
       grid_height = rows * dy
       isdown = self.isdown()           # 记录先前落笔状态
       pos = self.pos()                 # 记录先前坐标

       self.up()                        # 抬笔
       self.addx(-grid_width/2)         # 到左上角x  
       self.addy(grid_height/2)         # 到左上角y
       
       for _ in range(rows+1):          # 画横线
         self.pendown() 
         self.addx(grid_width)
         self.up()
         self.addx(-grid_width)
         self.addy(-dy)         
       
       self.addy(grid_height+dy)        # 到左上角y
       for _ in range(cols+1):          # 画竖线
         self.pendown() 
         self.addy(-grid_height)
         self.up()
         self.addy(grid_height)
         self.addx(dx)
         
       # 下面只是记录每个格子中心点坐标返回它们 
       self.addx(-grid_width-dx)    # 到左上角y
       startx = self.xcor() + dx/2  # 起始中心点x
       starty = self.ycor() - dy/2  # 起始中心点y
       cors = []
       for r in range(rows):
         rcors = []
         for c in range(cols):
           x = startx + c * dx
           y = starty - r * dy
           rcors.append((x,y))
         cors.append(rcors)     
       
       # 恢复原来坐标
       self.goto(pos)
       # 恢复先前落笔状态
       if isdown:
         self.down()
       else:
         self.up()
       return cors                  # 返回中心点坐标表
      
    def draw_grid3(self,rows=8,cols=8,dx=50,dy=50,stamp=False):
       """按行数和列数及格子边长与海龟当前方向画格子的方法。
          rows：行数，cols：列数，dx：格子宽度，dy：格子高度,stamp:是否盖图章并返回图章id们。
          本方法可以用来画斜格子,以角色当前坐标为起点,当前方向为行的方向来画，画完后又回到起点。
          假设角色方向为45度，位置(100,100)，要求印图章，则为返回行列中心点坐标举例如下：
         [[((170.71,100.00), 14), ((241.42,170.71), 15)],
          [((241.42,29.29), 16), ((312.13,100.00), 17)]]
          如果不要求盖图章，返回的是下面这样的中心点坐标列表，
         [[(170.71,100.00), (241.42,170.71)],
          [(241.42,29.29), (312.13,100.00)]]
       """
       grid_width = cols * dx
       grid_height = rows * dy
       isdown = self.isdown()           # 记录先前落笔状态
       pos = self.pos()                 # 记录先前坐标       

       self.up()                        # 抬笔
       for r in range(rows+1):
          self.down()
          self.fd(grid_width)
          self.up()
          self.bk(grid_width)
          self.right(90)
          self.fd(dy)
          self.left(90)
       self.left(90)
       self.fd(grid_height+dy)
       self.right(180)
       for c in range(cols+1):
          self.down()
          self.fd(grid_height)
          self.up()
          self.bk(grid_height)
          self.right(90)
          self.bk(dx)
          self.left(90)
       self.right(90)
       self.fd(grid_width+dx)
       self.right(180)
       # 第一个中心点
       self.right(90)
       self.fd(dy/2)
       self.left(90)
       self.fd(dx/2)
       cors = []                    # 要返回的中心坐标       
       for r in range(rows):
         rpos = []
         for c in range(cols):
             if stamp== True:            # 如果要盖图章则
                sid = self.stamp()             
                rpos.append((self.position(),sid))
             else:
                rpos.append(self.position())
             self.fd(dx)
         cors.append(rpos)
         self.bk(grid_width)
         self.right(90)
         self.fd(dy)
         self.left(90)
       self.left(90)
       self.fd(grid_height+dy/2)
       self.left(90)
       self.fd(dx/2)
       self.right(180)


       # 恢复先前落笔状态
       if isdown:
         self.down()
       else:
         self.up()
       return cors                  # 返回中心点坐标表
         
    movestamp = stampmove           # 移动图章
    stampglide = stampslide         # 滑行图章到指定坐标
    glidestamp = stampslide
    slidestamp = stampslide
    stamphide = hidestamp           # 隐藏图章
    stampshow = showstamp           # 显示图章
    randompos = gotorandom          # 随机坐标
    randomposition = gotorandom     # 随机坐标
    random_pos = gotorandom         # 随机坐标
    random_position = gotorandom    # 随机坐标 
    goto_random = gotorandom        # 随机坐标
    randomgoto = gotorandom         # 随机坐标
    random_goto = gotorandom        # 随机坐标    
    collide_mouse = collidemouse    # 碰撞鼠标指针
    collide_group = collide_others  # 碰到其它角色
    setalpha = set_alpha            # 设置透明度值
    getalpha = get_alpha            # 获取透明度值
    costumeindex = shapeindex       # 设定造型编号
    randomcostume = randomshape     # 随机设定造型
    nextcostume = nextshape         # 下一个造型
    previouscostume = previousshape # 上一个造型
    drawrect = draw_rect            # 画矩形
    kill = remove
    destroy = remove                 # remove是删除角色自己
    

# 定义类的别名
Js  = Sprite
Juese = Sprite
角色 = Sprite
精灵 = Sprite
    
class Key:
    def __init__(self,key):
        self.screen = Screen()
        self._key = key
        self._down = False
        self.screen.onkeypress(self._press, key)
        self.screen.onkeyrelease(self._release, key)
        
    def _press(self):
        self._down = True

    def _release(self):
        self._down = False

    def down(self):
      return self._down

class Mouse:
    def __init__(self,number=1):
      screen = Screen()
      self._number = number
      self._down = False
      screen.onclick(self._press,number)
      screen.onscreenrelease(self._release,number)

    def _press(self,x,y):
      self._down = True
      
    def _release(self,x,y):
      self._down = False
    
    def down(self):
      return self._down

def askyesno(title=None,message=None):
    """询问yes和no"""
    return  TK.messagebox.askyesno(title,message)
  
def showinfo(title=None,message=None):
    """显示信息"""
    return  TK.messagebox.showinfo(title,message)
  
def showwarning(title=None,message=None):
    """显示警告信息"""
    return  TK.messagebox.showwarning(title,message)
  
def showerror(title=None,message=None):
    """显示错误信息"""
    return  TK.messagebox.showerror(title,message)

def askquestion(title=None,message=None):
    """提问"""
    return  TK.messagebox.askquestion(title,message)

def askokcancel(title=None,message=None):
    """询问ok或取消"""
    return  TK.messagebox.askokcancel(title,message)

def askyesnocancel(title=None,message=None):
    """询问yes或no或取消"""
    return  TK.messagebox.askyesnocancel(title,message)

def askretrycancel(title=None,message=None):
    """询问重试或取消"""
    return  TK.messagebox.askretrycancel(title,message)

def askopenfilename(**options):
    """打开文件名
       options为以下名称:
       -defaultextension, -filetypes, -initialdir,
       -initialfile, -multiple, -parent, -title, or -typevariable
    """
    return filedialog.askopenfilename(**options)

def asksaveasfilename(**options):
    """另存为文件名"""
    return filedialog.asksaveasfilename(**options)

def askopenfilenames(**options):
    """打开很多文件"""
    return filedialog.askopenfilenames(**options)
  
def askdirectory(**options):
    """选择目录"""
    return filedialog.askdirectory(**options)
  
def askcolor():
    """显示颜色对话框"""
    return colorchooser.askcolor()

print("import successful! sprites V" + str(_VERSION) + ",email:406273900@qq.com")

if __name__ == "__main__":  

    width,height = 480,360
    screen = Screen()
    screen.setup(width,height)
    screen.bgcolor('gray')

    red = (255,0,0)
    png = Image.new('RGBA',(50,50),color=red)
    png.save('red.png')

    r = Sprite('red.png')
    for x in range(10):
        r.wander(-100,100,-100,100) # 在left,right,bottom,top范围内移动
        r.wait()                    # 等待一定的时间
        screen.update()
        
    cs = [r]
    for _ in range(5):
        r.gotorandom()               # 到随机坐标
        x = (10 + random.random())/10     
        y = r.clone()                # 克隆一个 
        r.shapesize(x)
        r.update()
        cs.append(y)                 # 添加到列表 
    r.gotorandom()
    
    v1 = Sprite()
    while True:
        v1.goto(mouse_pos())         # 移到鼠标指针的位置
        if v1.collidecolor(red):
            v1.say('碰到',delay=1,wait=False) # 如果碰到红色
        screen.update()

 

