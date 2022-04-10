"""写列表还原列表.py"""

lb = ["华夏","中华","编程娃娃","Python","Scratch"]

f = open("列表.txt",mode='w') # 以写模式打开文本文件
for item in lb:
    f.write(item + "\n")     # 把列表内容写入文件,注意加了换行符
f.close()


lb2 = []
f = open("列表.txt",mode='r')# 以读模式打开文本文件
for line in f:
    lb2.append(line.strip()) # 读出一行放到列表,把换行符去掉了
f.close()
print(lb2)
