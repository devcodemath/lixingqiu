"""数据分析初探.py
本程序把诸如 'http://www.nkjfrc.com/PersonalDetail.aspx?ID=23114'
这样的链接查找出来."""

f = open("人才网页源码.html")
htmlcode = f.read()
f.close()

keywords = "http://www.nkjfrc.com/PersonalDetail.aspx?ID="
key_len = len(keywords)

index = 0
while True:
    index = htmlcode.find(keywords,index) # 从index开始,查找包括keywords的字符串
    if index == -1 :print("查找完毕.");break
    index = index + key_len            # 加上关键词的长度
    string = ""    
    while True:
        number = htmlcode[index]       # 根据索引取字符
        if not number.isdigit(): break # 不是数字就中断循环
        string = string + number       # 累加到string
        index = index + 1              # 索引加1         
    print( keywords + string)
    
      
