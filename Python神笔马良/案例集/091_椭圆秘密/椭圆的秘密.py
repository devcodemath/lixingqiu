"""
   椭圆的秘密.py
   本程序给海龟模块添加了oval画椭圆命令，
   并且通过修改_undo命令，还能撤销画椭圆。
"""
import time
import turtle

def _oval(self,pos,radius,width=2):
    """以pos为圆心画椭圆"""
    self.goto(pos)
    cv = turtle.getcanvas()
    # 如果是整数或小数，则认为是画圆
    if isinstance(radius,(float,int)):                      
        x0 = pos[0] - radius
        y0 = -pos[1] - radius
        x1 = pos[0] + radius
        y1 = -pos[1] + radius
    elif isinstance(radius,(tuple,list)):
        a = radius[0]
        b = radius[1]
        x0 = pos[0] - a
        y0 = -pos[1] - b
        x1 = pos[0] + a
        y1 = -pos[1] + b
    # 创建椭圆
    item = cv.create_oval(x0,y0,x1,y1,fill='',width=width,
                                 outline=self._pencolor)
    self.items.append(item)
    if self.undobuffer:
       self.undobuffer.push(("oval", item))  # 放在撤销缓存表中名为oval
    cv.update()
    return item

def _undo(self,action,data):
    """undo命令所执行的操作，最后面的elif是自己扩展的
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
    elif action in ["wri", "dot"]:
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
    elif action =='oval':            # 如果动作是oval那么删除椭圆 
        item = data[0]
        self.screen._delete(item)
        
turtle.RawTurtle.oval = _oval        # 增加画椭圆的方法
turtle.RawTurtle._undo = _undo       # 修改了_undo方法

tom = turtle.Turtle()
tom.speed(0)
tom.screen.delay(0)

for x in range(-100,100):
    tom.clear()
    tom.oval((x,x),(100,50))    
    time.sleep(0.01)

tom.screen.mainloop()
