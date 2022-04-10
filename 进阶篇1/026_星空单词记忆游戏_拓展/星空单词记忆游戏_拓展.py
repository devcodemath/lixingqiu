"""星空单词记忆游戏.py 本程序是对上一节核心程序进行的拓展,设计了简单的封面,
设计了简易的游戏结束机制,重新设计了提示信息的显示方法,让单词从文件读取等。"""

from turtle import *
from random import choice

def load(filename):
    """加载单词文件,返回字典"""
    words_dict = {}                    # 新建字典
    f = open(filename)                 # 默认以只读模式打开文件
    for line in f:                     # 遍历每一行
        if line.strip() == "":continue # 防止有空行的出现
        word = line.split(":")[0]      # 以冒号隔开,前面是单词
        translate = line.split(":")[-1]# 后面是翻译
        words_dict[word] = translate.strip() # 注意剥去换行符
    f.close()
    return words_dict
        
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
        self.screen.cv.bind("<KeyPress>",self.inputevent)# 绑定到方法        
        self.p_turtle = Turtle(visible=False)       # 显示错误或正确的对象
        self.p_turtle.penup()
        self.p_turtle.color("white")
        self.p_turtle.goto(-10,-80)                 # 定位
        self.p_counter = 0                          # 延时计时器
        self.p_time = 1                             # 总共的擦除延时
        self.score = 0                              # 记录得分
        self.times = 20                             # 总共出题目的次数
        self.counter = 0                            # 出题计数器
        self.pickword()                             # 选单词
        
    def pickword(self):
        """初始化显示,随机挑选一个单词显示出来"""
        if self.counter < self.times:               # 小于出题目次数就出题        
           self.display_counter = 0                    # 显示计数器清零
           self.clear()                                # 清除所显示
           self.input_string = ""                      # 清空所输入的
           self.screen.title(self.input_string)        # 显示标题
           self.word = choice(list(words_list.keys())) # 随机选择一个单词
           self.translate = words_list[self.word]      # 单词对应的翻译
           self.write(self.translate,align='center',font=self.font)
           self.wait()                                 # 进入等待状态
           self.counter +=1                            # 计数器进行统计
        else:
           self.gameover()                             # 游戏结束 
        
        
    def wait(self):
        """倒计时等待，超时或输入正确就会换一个词语。"""
        if self.display_counter < self.display_time:# 小于则继续等待        
            self.display_counter += 1
            info = str(self.display_time - self.display_counter)
            self.c_turtle.clear()                   # 倒计时海龟清除上次所写
            self.c_turtle.write(info,align='center',font=self.font)
            self.screen.ontimer(self.wait,1000)     # 1秒后再次执行
        else:
            self.pickword()                         # 显示完了后重新选择单词显示
            
    def inputevent(self,event):
        """键盘输入事件调用的方法,event是事件响应后所得到的对象。"""        
        if event.keycode == 13 :                # 输入回车键判断是否输入正确
            if self.input_string.strip() == self.word: # 输入正确
                self.score +=10
                self.p_turtle.color("green")
                self.p_turtle.write("✔",font=self.font)
                self.delay_clear()                            
            else:
                self.score -=10
                self.p_turtle.color("red")
                self.p_turtle.write("✘",font=self.font)
                self.delay_clear()
            self.display_counter +=9999         # 用此机制提前结束显示                
        elif event.keycode == 8:                # 输入退格键则删除最后一个字符
            if self.input_string!="":
                self.input_string = self.input_string[:-1]
        else:
            self.input_string += event.char     # 否则累加到输入字符串
        self.screen.title(self.input_string)    # 输入完后在标题显示
        
    def delay_clear(self):
        """延时擦除勾和叉的方法,这里它只会显示一秒"""
        if self.p_counter < self.p_time:
            self.p_counter += 1
            self.screen.ontimer(self.delay_clear,1000)
        else:
            self.p_turtle.clear()
            self.p_counter = 0

    def gameover(self):
        """游戏结束后显示与单击关闭窗口"""
        self.c_turtle.clear()
        self.clear()
        self.font = (None,22,'normal') 
        info = "游戏结束,你的得分是:" + str(self.score)
        self.write(info,align='center',font=self.font)
        self.screen.bgpic("end.png")
        self.screen.exitonclick()      # 单击屏幕任意位置关闭窗口
                
def main():
    """显示封面,生成单词对象"""
    screen.onkeypress(None)            # 取消屏幕的按键绑定
    screen.bgpic("bg.png")             # 显示游戏背景
    wordobj = WordGame()                   # 生成单词对象

if __name__ == "__main__":

    width,height = 480,360
    words_list = load("words.txt")    # 从文件中加载单词
    screen = Screen()         
    screen.setup(width,height)
    screen.title("星空单词记忆游戏")
    screen.bgpic("post.png")          # 显示封面
    screen.onkeypress(main)           # 绑定任意键到main
    screen.listen()                   # 设置焦点监听键盘输入
    screen.mainloop()                 # 屏幕主循环

    
