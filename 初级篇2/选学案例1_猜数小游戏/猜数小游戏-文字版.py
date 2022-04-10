"""猜数小游戏.py"""

from time import sleep
from random import randint

def slow_print(string):
    """一个字一个字的打印"""
    for char in string:
        print(char,end=' ',flush=True)
        sleep(0.2)
    print()
    
slow_print("Hello,我是计算机，欢迎来到猜数小游戏。")
slow_print("我会生成一个从1到100以内的整数，你猜猜它是多少吧。\n")
number = randint(1,100)

while True:
    answer = input("请输入整数：")
    if int(answer) == number :
        slow_print("恭喜，恭喜，你猜对了！")
        break
    if int(answer) < number:
        slow_print("小了。")
    if int(answer) > number:
        slow_print("大了。")

slow_print("猜数小游戏结束了。再见！") 

        
