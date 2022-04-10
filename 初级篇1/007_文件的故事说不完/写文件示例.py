"""写文件示例.py"""

filename = "fish2.txt"
f = open(filename,mode='w')
f.write("还在为养不活鱼而烦恼？这些鱼非常好养，大半年也不会挂一条！")
f.close()

