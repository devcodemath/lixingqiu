"""背景图片  背景.png 400x200
   猜猜按钮图片 button_guess.png  100x44
   说明按钮图片 button_explain.png  100x44
   
"""
from tkinter import  messagebox
from tkinter import *
from PIL import ImageTk,Image
from random import randint

def check():
    """单击‘猜猜’按钮运行这个函数。它会获取文本框的字符串，尝试把它转换成数字，再与random_number进行比较"""
    try:        
       answer = int( answer_text.get().strip() )     #获取输入框数字       
    except:
       canvas.itemconfig(tip,text='输入错误！',anchor='w')
       answer_text.delete(0, END)                                    #清空所有文本
       return
    if random_number == answer:
        canvas.itemconfig(tip,text='恭喜你，猜对了。',anchor='w') 
    else:
        if answer < random_number :
           canvas.itemconfig(tip,text='小了。',anchor='w') 
        else:
           canvas.itemconfig(tip,text='大了。',anchor='w')
    answer_text.delete(0, END)                                    #清空所有文本
 
        
def explain():
    """单击‘说明’按钮弹出相关字符串。"""
    messagebox.showinfo(game_title, "Hello,我是计算机，欢迎来到猜数小游戏。\n\n我会生成一个从1到100以内的整数，你猜猜它是多少吧。")

def clear_explain(event):
    """文本框的单击鼠标事件会运行这个函数"""
    answer_text.delete(0, END)                         #清空所有文本
    
    
game_title = "猜数小游戏"

window = Tk()                                           #新建窗口
window.resizable(width=False,height=False)              #设置窗口不能变化大小
window.geometry("400x200")                              #设置窗口的几何尺寸
window.title(game_title)                                #设置窗口的标题
 
canvas = Canvas(window,width=400,height=200,bg="white") #创建画布
canvas.pack(expand=True)                                #放置画布，expand为真

"加载三张图片作为背景图与按钮图"
im1 = Image.open("背景.png")                            #作为背景图的
background = ImageTk.PhotoImage(im1)                    #转换为tkinter能识别的图形对象:取名为 background
im_button = Image.open("button_guess.png")              #猜猜按钮图
button_image_guess = ImageTk.PhotoImage(im_button)      #转换为tk能识别的图
im_button = Image.open("button_explain.png")            #说明按钮图
button_image_explain = ImageTk.PhotoImage(im_button)    #转换为tk能识别的图   

canvas.create_image(0,0,anchor=NW,image=background)     #贴背景图,以左上为0,0
canvas.create_text(200,60,text = game_title,fill='black',font=("Arial", 22, "normal")) #创建文字，写标题 
canvas.create_text(100,100,text = "请在文本框中输入数字：",fill='white',font=("Arial", 12, "bold"),justify = 'left') #提示文字，不要也可以 

"这是输入数字的文本框"
answer_text = Entry(window,width=12,font=('',13,'normal'),relief=RIDGE,bg= 'orange',fg='black') #输入数字的文本框
answer_text.insert(0, "在此输入数字")
answer_text.place(x=30,y=120)                                      #放置
answer_text.bind('<Button-1>', clear_explain)
 
tip = canvas.create_text(30,175,text = " ",fill='cyan',font=("Arial", 13, "normal")) #创建画布上的提示文字

random_number = randint(1,100)                                     #产生随机数         

button_guess = Button(window,width=100 ,command=check,image = button_image_guess)     #在window上新建 猜猜 按钮，命令为check，图形为button_image_guess
button_guess.place(x=160,y=110)                                                       #放置

button_explain = Button(window,width=100,command=explain,image = button_image_explain) #新建说明按钮
button_explain.place(x=280,y=110)

window.mainloop()










