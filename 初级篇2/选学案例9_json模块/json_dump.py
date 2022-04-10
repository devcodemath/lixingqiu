"""
一. dumps 和 dump:

dumps和dump   序列化方法,把内容"倒"到文件中.

dumps只完成了序列化为str，
dump必须传文件描述符，将序列化的str保存到文件中

"""

import json

color_list = ('red','orange','yellow','blue','cyan','blue','purple')

f = open("color.txt",mode='w')
json.dump(color_list,f)    # 可以理解为把颜色表倒入文件中
f.close()
