"""单词记忆小程序-字典版.py"""

from random import choice
from time import sleep

words = {'red':'红','orange':'橙','yellow':'黄','green':'绿','cyan':'青','blue':'蓝','purple':'紫','pink':'粉红','gray':'灰','black':'黑','white':'白'}
amounts = len(words)
score = 0
print("\n" * 3)

print("---------------单词记忆小程序--------------\n")
print("以下是英语单词与其对应的翻译表。\n")
for key in words:
    print(key,"：",words[key])
    
sleep(3)
print("\n在接下来的练习中请输入相应的翻译。")
print("\n记住了吗？练习马上就要开始了。\n")

sleep(6)
print("\n" * 50)

running = True
while running:
    word  = choice(list(words.keys()))                 # 出题，随机选择一个单词
    translate = words[word]                            # 取出此单词的翻译
    answer = input("请写出'" + word + "'的汉语翻译：") # 提示输入答案
    if answer == translate:                            # 如果答案正确
        score = score + 10
        print("回答正确加10分！当前得分：" ,score,"\n")# 打印‘回答正确......
        
    elif answer in ("exit","quit"):                    # 退出程序机制
        print("你选择了退出程序...\n")
        running = False
    elif answer == "":
        print("你选择了忽略...\n")
        continue
    else:
        score = score - 10
        print("回答错误，减10分！当前得分：" ,score,"\n") # 否则就是输入错误了

input("你的得分：",score)

            
        
