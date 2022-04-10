from turtle import RawTurtle,TurtleScreenBase,Turtle,Screen

__author__ = '李兴球'
__blog__ = 'www.lixingqiu.com'

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

if __name__ == "__main__":

    tom = Turtle(visible=False)
    tom.write('风火轮编程',angle=45)
    tom.screen.mainloop()
