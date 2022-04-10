f = open("网页源码.txt")
htmlcode = f.read()
f.close()

key = "href=\""                  #经分析源码,链接以href="开头,在字符串中不断地查找它

i = 0
while i < len(htmlcode) -6:

    chars = htmlcode[i:i+6]      #切6个字符
    if chars == key:             #如果和href="相等,那么说明有链接开始了.
        j = i  + 6               #链接是从i后的第6个字符开始
        while htmlcode[j]!='"': j = j + 1    #寻找链接结束的引号,找到了,j就是结束位置
        link = htmlcode[i+6:j]   #链接就是 i+6 到 j
        i = j                    #下次从j索引开始找
        if "https" in link : print(link)
    i = i + 1
