"""
   英语单词助记器
   这是一个简单的英语单词记忆小软件。
   可以自己设定单词库，注意词典的key和value返回来也能形成一对一映射的关系！
   程序开始时可以设定是显示英语输入翻译，还是显示汉语输入英语！
"""
from sprites import *

screen = Screen()
screen.setup(480,360)

# 以下可以自己从数据库或文件中加载词典,此处只做demo
汉英词典 ={'红色':'red','橙色':'orange','黄色':'yellow','绿色':'green'}
英汉词典 = {value:key for key,value in 汉英词典.items()}

mode = askyesno('询问','请选择模式,选择"yes"是出中文回答英文,否则相反')
词典 = 汉英词典  if mode else 英汉词典
counter = 0                    # 做题数
rights = 0                     # 正确数
word = ""
def fun(event):
  global word,returnkey,counter,rights
  print(event.keycode)
  if event.keycode == 13 :     # 如果输入回车，那么进行判断，否则继续累加
     counter += 1              # 累计出题目数量
     if word == 词典[w]:
        s.say('答对了',1)
        rights += 1            # 答对的数量                       
     else:
        s.say('错了',1)
     word= ""
     returnkey = True
     dummy2.clear()
     zql = '正确率' + str(int(100 * rights/counter)) + "%"
     dummy2.write(zql,align='center',font=('黑体',16,'normal')) 
  else:
    if event.keycode == 8:     # 如果是退格键
       word = word[:-1]
    else:
       word += event.char
  screen.title(word)
  dummy.clear()      
  dummy.write(word,align='center',font=('黑体',32,'normal'))

screen.onanykey(fun)           # 不要和Key类一起用,本方法不公开,只供专家使用
screen.listen()                # 监听键盘按键

dummy = Sprite(visible=False)
dummy.sety(-100)
dummy.color('dodger blue')
dummy2 = dummy.clone()
dummy2.sety(120)
dummy2.color('orange')

s = Sprite()
returnkey = False              # 逻辑变量用来代表回车键有没有按
while True:
   returnkey = False           # 表示回车键没有按
   w = random.choice(list(词典.keys()))
   s.say(f'请输入{w}的翻译',2000,False)
   # 等待回车键有没有按下
   while not returnkey: screen.update()

