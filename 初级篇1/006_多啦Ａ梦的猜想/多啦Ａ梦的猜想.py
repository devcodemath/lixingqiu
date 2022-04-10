"""多啦A梦的猜想.py"""

from time import sleep

def slow_print(string):
    """一个字一个字的打印"""
    for char in string:
        print(char,end=' ',flush=True)
        sleep(0.2)
    print()

slow_print("嗨，我是机器猫多啦A梦，")
slow_print("我能猜出你的想法。")
slow_print("请输入数字来表示你的猜想吧。\n")

while True:
    hope = input()
    hope = int(hope)
    if hope == 0:
        slow_print("你将拥有崭新的一天")
    elif hope == 1:
        slow_print("条条道路通罗马。")
    elif hope == 2:
        slow_print("道路是曲折的，前途是光明的。")
    elif hope == 3:
        slow_print("你是不是想去旅游啊。")
    elif hope == 4:
        slow_print("事事如意，年年顺心。")
    elif hope == 5:
        slow_print("一二三四五，上山打老虎。")
    elif hope > 5:
        slow_print("火炬照耀你前行。")
    elif hope == -1:
        break
    else:
        slow_print("让我再想想。")
        
