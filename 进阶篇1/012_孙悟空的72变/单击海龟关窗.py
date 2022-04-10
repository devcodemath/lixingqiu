"""单击海龟关窗.py"""

from turtle import Turtle

t = Turtle(shape='turtle')
t.onclick(lambda x,y:t.screen.bye())
t.screen.mainloop()
