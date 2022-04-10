"""最简单词记忆游戏.py"""

from random import choice

words_list = {'red':'红色','orange':'橙色','yellow':'黄色','green':'绿色','cyan':'青色','blue':'蓝色','purple':'紫色','black':'黑色','white':'白色','gray':'灰色','magenta':'品红'}
while True:
    word = choice(list(words_list.keys())) # 随机选择一个单词
    translate = words_list[word]           # 取出其翻译
    input_string = input(translate + "的英文是?\n") # 要求输入
    if input_string == word :              # 如果输入的和单词相等
        print("     输入正确\n")           # 打印输入正确
    else:
        print("     输入错误\n")           # 打印输入错误
        
        
