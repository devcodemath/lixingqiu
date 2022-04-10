"""星空单词记忆游戏_核心程序.py 本程序演示了单词记忆游戏的核心代码。"""

from turtle import *
from random import choice

class WordGame(Turtle):
    def __init__(self):
        Turtle.__init__(self,visible=False)         # 初始化不可见对象
        self.penup()                                # 抬笔
        self.color("cyan")                          # 青色
        self.font = (None,32,'normal')              # 字体属性
        self.display_time = 10                      # 显示时间为10秒 
        self.c_turtle = Turtle(visible=False)       # 倒计时海龟对象
        self.c_turtle.penup()                       # 抬笔
        self.c_turtle.color("yellow")               # 它是黄色的
        self.c_turtle.goto(0,100)                   # 定位到(0,100)
        self.pickword()                             # 选单词
        self.screen.cv.bind("<KeyPress>",self.inputevent)# 绑定到方法
        self.screen.listen()                        # 监听键盘
        
    def pickword(self):
        """初始化显示,随机挑选一个单词,显示它的翻译。"""
        self.display_counter = 0                    # 显示计数器清零
        self.clear()                                # 清除所显示
        self.input_string = ""                      # 清空所输入的
        self.screen.title(self.input_string)        # 显示标题
        self.word = choice(list(words_list.keys())) # 随机选择一个单词
        self.translate = words_list[self.word]      # 单词对应的翻译
        self.write(self.translate,align='center',font=self.font)
        self.wait()                                 # 进入等待状态
        
    def wait(self):
        """倒计时等待，超时或输入正确就会换一个词语。"""
        if self.display_counter < self.display_time:# 小于则继续等待        
            self.display_counter += 1
            info = str(self.display_time - self.display_counter)
            self.c_turtle.clear()                   # 倒计时海龟清除上次所写
            self.c_turtle.write(info,align='center',font=self.font)# 写倒计时数字
            self.screen.ontimer(self.wait,1000)     # 1秒后再次执行
        else:
            self.pickword()                         # 显示完了后重新选择单词显示
            
    def inputevent(self,event):
        """键盘输入事件调用的方法,event是事件响应后所得到的对象。"""        
        if event.keycode == 13 :                # 输入回车键判断是否输入正确
            if self.input_string.strip() == self.word: # 输入正确
                print("输入正确")                
            else:
                print("输入错误")               # 否则显示输入错误
            self.display_counter +=9999         # 用此机制提前结束显示                
        elif event.keycode == 8:                # 输入退格键则删除最后一个字符
            if self.input_string!="":
                self.input_string = self.input_string[:-1]
        else:
            self.input_string += event.char     # 否则累加到输入字符串
        self.screen.title(self.input_string)    # 输入完后在标题显示


if __name__ == "__main__":

    width,height = 480,360
    words_list = {'red':'红色','orange':'橙色','yellow':'黄色','green':'绿色','cyan':'青色','blue':'蓝色','purple':'紫色','black':'黑色','white':'白色','gray':'灰色','magenta':'品红'}

    screen = Screen()     
    screen.bgpic("bg.png")
    screen.setup(width,height)
    screen.title("星空单词记忆游戏_核心程序")

    wordobj = WordGame()    
    screen.mainloop()
    
    """
    请按如下方法对本程序进行改进，或者自行创意，把本程序改得更好。
    @、新建单词文件，让words_list的值是从文件读取而来。
    @、让显示输入正确和输入错误的字符串在屏幕显示出来，不要用print语句。
    @、输入正确则加10分，输入错误则减10分。
    @、设计程序结束的逻辑，如显示20次单词后游戏结束，显示得分。
    @、给程序加一个封面，输入回车键开始游戏。
    """

