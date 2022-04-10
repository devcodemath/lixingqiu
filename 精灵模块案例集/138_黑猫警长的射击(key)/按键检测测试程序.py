from sprites import *

screen = Screen()
spacekey = Key('space')   # 实例化空格键'a','Up','down','Left','Right'
screen.listen()           # 监听屏幕按键

while True:
    if spacekey.down():      # 如果按了空格键
       print('按了空格键')
    screen.update()
