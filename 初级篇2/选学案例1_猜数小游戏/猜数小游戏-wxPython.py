import wx
from random import randint

game_title = "猜数小游戏"
random_number = randint(1,100)

def guess_number(event):     # 定义打开文件事件
    try:
        answer = int(answer_text.GetValue())       
        if answer == random_number:
            tip_text.SetValue("猜对了！") 
        if answer < random_number:
            tip_text.SetValue("小了！") 
        if answer > random_number:
            tip_text.SetValue("大了！") 
    except:
        
        tip_text.SetValue("非法输入！")         
         
def explain_game(event):
    tip_text.SetValue("请在上面文本框中输入，然后按'猜猜'按钮猜一下。") 

def reset(event):
    global random_number
    random_number = randint(1,100)
    tip_text.SetValue("请在上面文本框中输入，然后按'猜猜'按钮猜一下。")
    answer_text.SetValue("") 
    
    
app = wx.App()                                                              
frame = wx.Frame(None,title = game_title ,pos = ( 1000,200),size = (300,240))        #相对于屏幕左上角坐标

title_text = wx.StaticText(frame,-1,game_title,(80,30))
title_text.SetForegroundColour('blue')
title_text.SetBackgroundColour('gray')
font = wx.Font(16,wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
title_text.SetFont(font)

answer_text = wx.TextCtrl(frame,pos = (30,90),size = (60,24))                        #创建文本框，文件路径要自己输入


guess_button = wx.Button(frame,label = "猜猜",pos = (110,90),size = (50,24))         #猜猜按钮
guess_button.Bind(wx.EVT_BUTTON,guess_number)                                        #猜猜按钮绑定guess_number函数
 
explain_button = wx.Button(frame,label = "说明",pos = (170,90),size = (50,24))       #说明按钮
explain_button.Bind(wx.EVT_BUTTON,explain_game)                                      #说明按钮绑定explain_game函数
 
reset_button = wx.Button(frame,label = "重来",pos = (230,90),size = (50,24))         #重来按钮
reset_button.Bind(wx.EVT_BUTTON,reset )                                              #重来按钮绑定explain_game函数


tip_text= wx.TextCtrl(frame,pos = (30,140),size = (240,50),style=wx.TE_MULTILINE )
tip_text.SetValue("由计算机随机出一个1到100以内的数，猜猜它是多少？")

 
frame.Show()
app.MainLoop()
