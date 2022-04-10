"""
   自动算术出题器
   本程序会自动出加法题，按取消结束程序。
"""
from sprites import *

screen = Screen()
screen.setup(480,360)
s = Sprite()
while True:
  a = random.randint(-100,100)
  b = random.randint(-100,100)
  c = a + b
  info = str(a) + '+' + str(b) + "=?"
  s.say(info,1000,False)
  result = screen.numinput('回答','请输入答案')
  if result !=None:
     result = int(result)
  else:
     break
  screen.title('输入' + str(result) + "   ,答案：" + str(c))
  if result == c :
     s.say('回答正确',100,False)
  else:
     s.say('回答错误',100,False)
  s.wait(1)

s.say('结束')
screen.mainloop()
