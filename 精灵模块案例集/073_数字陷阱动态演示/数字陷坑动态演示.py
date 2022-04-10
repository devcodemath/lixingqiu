"""
   数字陷阱动态演示,
   70年代中期，美国各所名牌大学校园内，人们都像发疯一般，废寝忘食地玩弄一种数学游戏。这个游戏十分简单：任意写出一个自然数N，并且按照以下的规律进行变换：
   如果是个奇数，则下一步变成3N+1。如果是个偶数，则下－步变成N/2。
   以下是Python动态演示版,属于简易算法.
   无论N 是怎样一个数字，都无法逃出落入底部的4-2-1循环，最终都无法逃脱回到谷底1，永远也逃不出这样的宿命。
   自然界中的小水滴在高空中受上升气流的推动，在云层中忽上忽下，越积越大并形成冰，最后突然落下来，变成了冰雹，这就是冰雹的形成过程。 而这个数字陷阱之所以叫冰雹猜想，是因为算来算去，数字上上下下，最后一下子像冰雹似的掉下来，变成了一个数字“1”。
   这就是著名的“冰雹猜想”，也叫“数字陷阱”。通过编程的方法，验算“冰雹猜想”是否成立。
   
"""
from sprites import *

screen = Screen()       # 新建屏幕

s = Sprite()            # 新建角色
s.pencolor('dodger blue') 
while True:
    numbers = []
    n = random.randint(10,20)
    numbers.append(n)
    while n != 1:
        if n%2==0:
            n = n/2
        else:
            n = 3 * n + 1
        numbers.append(n)
    #numbers.append(1)
    # 把数字画出来
    s.clear()
    s.goto(-300,-200)   
    for digit in numbers:
        s.pendown()
        s.addy(digit*4)
        s.penup()
        s.addy(-digit*4-20)
        s.write(digit,align='center')
        s.addy(20)
        s.addx(40)
        s.wait(0.5)
    s.wait(100)
        
