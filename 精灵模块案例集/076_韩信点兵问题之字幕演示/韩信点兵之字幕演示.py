"""
   韩信点兵问题演示
"""
from sprites import *

title = '韩信点兵简介'
question = "秦朝末年，楚汉相争。一次，韩信将1500名将士与楚王大将李锋交战。苦战一场，楚军不敌，败退回营，汉军也死伤四五百人，于是韩信整顿兵马 也返回大本营。当行至一山坡，忽有后军来报，说有楚军骑兵追来。只见远方尘土飞扬，杀声震天。汉军本来 己十分疲惫，这时队伍大哗。 韩信兵马到坡顶，见来 敌不足五百骑，便急速点兵迎敌。他命令士兵 3 人一排，结果多出2名；接着命令士兵 5 人一排，结果多出3名；他又命令士兵 7人一排，结果又多出2名。 韩信马上向将士们宣布： 我军有1073名勇士，敌人不足五百，我们居高临下，以众击寡，一定能打败敌人。汉军本来就信服白己的统帅，这一来更相信 韩信是“神仙下凡”、ι神机妙算”。于是士气大振。一时间施旗摇动，鼓声喧天，汉军步步进逼，楚军乱作一团。交战不久，楚军大败而逃。通过编程的方法，计算出韩信部队剩余人数。"

def write_one_by_one(tom,dx,string):
    """
       tom:精灵对象
       dx:水平间距
       string:字符串
    """
    ft = ('楷体',16,'normal')
    for char in string:
        tom.write(char,align='center',font=ft)
        tom.addx(dx)
        if tom.xcor() > 250:
            tom.addy(-30)
            tom.setx(-250)
        tom.wait(0.05)

screen = Screen()
screen.bgcolor('dodger blue')

s = Sprite(visible=False)
s.addy(250)
s.color('yellow')
s.write("韩信点兵问题演示",align='center',font=('黑体',22,'bold'))
s.write(5)
s.color('white')
s.goto(-250,150)

write_one_by_one(s,20,question)

screen.mainloop()
        
    

