"""walk.py,递归显示打印所有文件夹包括子文件夹项目"""
import os
 
def walk(path):
    """递归遍历路径"""
    for item in os.listdir(path):
        subitem  = path + os.sep + item
        if os.path.isdir(subitem ):      # 可能是文件或文件夹
            walk(subitem )               # 如果是路径，则遍历它       
        print(subitem ) 

path = "C:\\ffmpeg"
walk(path)
