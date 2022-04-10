"""
   小猫的功夫表演操
"""
import glob
from sprites import *

def action_1():
    cat.play('swing1.wav')
    cat.shape(f['出拳'])
    cat.wait(0.3)
    cat.shape(f['走1'])

def action_2():
    cat.say('波',wait=False)
    cat.shape(f['波动拳1'])
    cat.wait(0.2)
    cat.shape(f['波动拳2'])
    cat.wait(0.2)
    cat.play('swing1.wav')
    cat.wait(0.1)
    cat.shape(f['波动拳3'])
    cat.wait(0.1)
    bo.play('swing2.wav')
    bo.goto(cat.pos())
    bo.show()
    while bo.xcor() < bo.screen.window_width()//2:
        bo.addx(5)
        bo.wait(0.01)
    bo.hide()
    cat.wait(0.3)
    cat.shape(f['走1'])       
    
def action_3():
    cat.shape(f['出拳2'])
    cat.wait(0.1)
    cat.addy(35)
    cat.addx(2)
    cat.shape(f['前1'])
    cat.play('swing1.wav')
    cat.wait(0.1)
    cat.addy(20)
    cat.addx(2)
    cat.shape(f['前2'])
    cat.wait(0.1)
    cat.addy(10)
    cat.addx(-10)
    cat.shape(f['前3'])
    cat.wait(0.3)
    cat.dy = 0
    while cat.ycor()>0:
        cat.addy(cat.dy)
        cat.dy -= 0.5
    cat.wait(0.3)
    cat.addx(6)
    cat.sety(0)
    cat.shape(f['走1'])
    
def action_4():    
     cat.play('swing1.wav')
     cat.shape(f['蹲踢'])
     cat.wait(0.1)
     cat.shape(f['蹲下'])
     cat.wait(0.3)
     cat.shape(f['走1'])
     
def action_5():    
     cat.play('swing1.wav')
     cat.shape(f['投1'])
     cat.wait(0.1)
     cat.shape(f['投2'])
     cat.wait(0.1)
     cat.shape(f['投3'])
     cat.wait(0.3)
     cat.shape(f['走1'])     
    
def action_6():    
     cat.play('swing1.wav')
     cat.shape(f['蹲拳'])
     cat.wait(0.1)
     cat.shape(f['蹲下'])
     cat.wait(0.3)
     cat.shape(f['走1'])

def action_7():    
     cat.play('swing1.wav')
     cat.shape(f['踢'])
     cat.wait(0.1)
     cat.shape(f['走1'])

def action_8():    
     cat.play('swing1.wav')
     cat.shape(f['前1'])
     cat.wait(0.1)
     cat.addy(20)
     cat.shape(f['前2'])
     cat.wait(0.1)
     cat.addy(20)
     cat.shape(f['前3'])
     cat.wait(0.1)
     cat.addy(20)
     for x in range(3):
         cat.addy(-20)     
     cat.shape(f['走1'])
     
def action_9():    
     cat.play('swing1.wav')
     cat.shape(f['下踢'])
     cat.wait(0.2)
     cat.shape(f['走1'])
     
     
frames = glob.glob('images/*.png')
f = {}
for frame in frames:
    key = frame.split('.')[0].split('\\')[-1]
    f[key] = frame

screen = Screen()
screen.setup(480,360)

bo = Sprite(shape='波.png',visible=False)
bo.scale(0.5)
cat = Sprite(shape=f['走1'])
cat.wait(1)
action_1()
cat.wait(1)
action_2()
cat.wait(1)
action_3()
cat.wait(1)
action_4()
cat.wait(1)
action_5()
cat.wait(1)
action_6()
cat.wait(1)
action_7()
cat.wait(1)
action_8()
cat.wait(1)
action_9()
screen.mainloop()
