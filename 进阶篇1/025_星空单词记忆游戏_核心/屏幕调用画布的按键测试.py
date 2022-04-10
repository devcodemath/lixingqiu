"""屏幕调用画布的按键测试.py """
from turtle import Screen

def inputevent(event):
    global input_string
    print(event)
    input_string = input_string + event.char
    screen.title(input_string)

input_string = ""
screen = Screen()
screen.setup(400,120)
screen.title("按键测试")
screen.cv.bind("<KeyPress>",inputevent)
screen.listen()
screen.mainloop()

"""
<KeyPress event state=Mod1 keysym=b keycode=66 char='b' x=111 y=-94>
"""
