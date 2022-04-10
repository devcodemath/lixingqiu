"""
二. loads 和 load 

loads和load  反序列化方法, 把文件内容转换回Python对象.

loads 只完成了反序列化，
load 只接收文件描述符，完成了读取文件和反序列化

"""
import json
 
f = open("color.txt",mode='r')
string = f.read()
f.close()
x = json.loads(string )

print(x)
  
