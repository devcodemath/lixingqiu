def countspaces(string):
    """统计string前面的空格数"""
    spaces = 0
    for char in string:      # 
        if char !=' ':break
        if char == ' ':spaces += 1
    return spaces
                
def insertbreak(programes,breakstatement):
    """
       给循环增加中断指令,以便按中止时循环会退出
       programes:代码列表,breakstatement:中断指令,
       只支持空格为缩进的代码!!

    """
    index = 0
    amounts = len(programes)
    while index < amounts:    
        code = programes[index]
        tmpcode = code.strip()
        if tmpcode.startswith('while') or tmpcode.startswith('for') and ":" in tmpcode:
        
            # 检测在冒号后是否有语句,如果有,则移到下一行
            singleline = code.split(":")
            #aftercolon = singleline[-1].strip()  
            aftercolon = ":".join(singleline[1:])
            aftercolon = aftercolon.strip()        # 冒号后去除两边空格字符串
            if len(aftercolon)>0:                  # 如果冒号后有语句
              if not aftercolon.startswith("#"):   # 如果不是#号开头则认为是一条语句
                  programes[index] = singleline[0] + ":" # 冒号前面的代码
                  # 统计singleline[0]前面的空格数
                  spaces = countspaces(singleline[0]) + 4 # 加4表示要缩进
                  insertedcode = spaces * " " + breakstatement
                  programes.insert(index+1,insertedcode)
                  index = index + 1
                  # 把冒号后面的代码插下到列表的下一项,后面代码的依次往后移
                  programes.insert(index+1,spaces * " " + aftercolon)
                  index = index + 1                  
              else:
                   # 否则在冒号后只是注释,则直接在while或for循环下面插入一条中断 
                   spaces = countspaces(programes[index+1])# 统计for或while下一行代码前面空格数
                   insertedcode = spaces * " " + breakstatement
                   programes.insert(index+1,insertedcode)
                   index = index + 1
              amounts = len(programes)
                   
            else:
               # 否则在冒号后并没有语句,则直接在while或for循环下面插入一条中断 
               spaces = countspaces(programes[index+1])# 统计for或while下一行代码前面空格数
               insertedcode = spaces * " " + breakstatement
               programes.insert(index+1,insertedcode)
               index = index + 1
               amounts = len(programes)
        index = index + 1

allcodes = """
for y in range(3):
a='for x in range(1000):print(abcd);break'
s = 'while x>3: pass'
y = 0
for x in zip(abcd,efg):#这是for循环呀
  for x in range(4):print(x,end='')
  while True:
      import os
      for _ in range(10):
         for x in range(10000000000000):
           bug.fd(10)
           bug.rt(10)
         for y in range(acd):
            pass
       while True:   # 哟西这是一个while循环呢
            pass
            for _ in range(100):
                   pass
                   while True:pass
       for x in 'abcdefg':    # THis is a test
           print('x')
           print('为了我国的')
       while True:for _ in range(10):print(10) 
"""
allcodes = allcodes.split("\n")
stopcode = 'if stopexec == True:break'

insertbreak(allcodes,stopcode)
临时 = '\n'.join(allcodes)
f = open('c:/abcd.py',mode='w',encoding='utf-8')
f.write(临时)
f.close()
print(临时)
