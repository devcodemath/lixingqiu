"""
   难不倒英语单词助记器.pyw
   简单可视化的英语单词记忆小程序。通过不断地出选择题，过滤出学生不认识的单词。
   然后可以按取消键把不认识的单词挑出来，加强记忆。
"""
import os
import xlrd                        # pip install xlrd
from sprites import *              # pip install sprites  
from playsound import playsound    # pip install playsound

__author__ = '李兴球'
__blog__ = 'www.lixingqiu.com'

filename="中学单词库.xls"
data = xlrd.open_workbook(filename) # 打开xls文件
table = data.sheets()[0]            # 打开第一张表
nrows = table.nrows                 # 获取表的行数
enhandict = {}                      # 英汉词典
hanendict = {}
wrongs = []                         # 选择错误解的英语单词
c = 0
for i in range(nrows):              # 循环逐行
    word = str(table.row_values(i)[1])
    if word.endswith("\xa0"):word = word[:-1]
    yb = table.row_values(i)[2]     # 音标
    fy = table.row_values(i)[3]     # 翻译
    enhandict[word] = (fy,yb)       # 加入到英汉词典
    hanendict[fy] = (word,yb)       # 加入到汉英词典
    c = c + 1

def process(event):
    """按键处理"""
    global inputnumber,returnkey,i
    print(event.keycode)
    if event.keycode == 13:                  # 如果输入回车键
        if inputnumber == str(i):            # 则回答正确
            playsound('star.mp3',False)
            print('回答正确')
            effect((200,200),'正确.png',400) # 显示红勾
        else:
            info = word + " , " + enhandict[word][0] + " , " + enhandict[word][1]
            wrongs.append(info)
            print('回答错误')
            playsound('ling.wav',False)
            effect((200,200),'错误.png',400) # 显示红叉
        returnkey = True
    elif event.keycode == 32 :         # 按空格键也播放当前word音
        play_mp3()
    elif event.keycode == 27:          # 按esc也显示没有做对的题目
        display_wrongs()
        
    elif event.keycode == 8:          # 如果是退格键
       inputnumber = inputnumber[:-1]
    else:
        inputnumber += event.char
    display.clear()
    display.write(inputnumber,align='center',font=ft)

def play_mp3():
    try:                              # 由于这个音标不一定有所以try 
        playsound('audio/' + word + '.mp3',False)
    except:
        pass
    
def display_wrongs():
    filename = "以下是做错的英语单词，请加强记忆.txt"
    s = '\n'.join(wrongs)
    f = open(filename,mode='w',encoding='utf-8')
    f.write(s)
    f.close()
    os.system(filename)
    
screen = Screen()                       # 新建窗口
screen.bgcolor('dodger blue')           # 背景颜色
screen.title('难不倒英语单词助记器_按数字键选择答案')    # 设定标题

screen.onclick(lambda x,y:play_mp3())   # 单击播放当前单词的发音
screen.onclick(lambda x,y:display_wrongs(),3) # 单击右键查看选择错误的单词

ft = ("Arial",32,'bold')              # 字体样式
ft2 = ("楷体",18,'normal')            # 字体样式
ft3 = ("宋体",14,'normal')            # 字体样式
ft4 = ("楷体",16,'normal')            # 字体样式

helpinfo = Sprite(visible=False)
helpinfo.sety(-300)
helpinfo.write('单击左键或按空格重读,单击右键或按ESC键显示没有做正确的题目',
               align = 'center',font=ft4)

display = Sprite(visible=False)         # 显示所输入数字的
display.color('blue')
display.sety(-260)
 
tom = Sprite(visible=False)           # 显示英文词汇的
tom.sety(100)
tom.color('white')
screen.onanykey(process)              # 按任意键输入(不要和Key类一起用)
screen.listen()

wrongs = []
while True:
    inputnumber = ""                  # 所输入数字
    returnkey = False
    display.clear()
    word = random.choice(list(enhandict.keys())) # 随机选择一个单词
    display.write('请选择' + word + '的中文翻译,输入数字再按回车即可',align='center',font=ft3)
    tom.clear()
    tom.goto(0,220)
    tom.write(word,align='center',font=ft)       # 显示出来英语和音标
    play_mp3()                                   # 播放word单词的音频
    tom.addy(-50)
    tom.write(enhandict[word][1],align='center',font=ft2)
    answers = [random.choice(list(enhandict.values())) for _ in range(10)]
    i = random.randint(0,9)                      # 0到9的随机数
    answers[i] = enhandict[word]                 # 换成正确答案(输入的时候应该输入i)
    tom.goto(-300,80)
    for x in range(10):
        info = str(x) + "、" + answers[x][0]
        tom.write(info,font=ft2)
        tom.addy(-30)
    while not returnkey:screen.update()
        
    
    
    
