"""给文件添加内容示例.py"""

filename = "fish2.txt"
f = open(filename,mode='a')
f.write("\n草鱼不仅爱吃玉米，更爱吃新鲜的水草")
f.close()


