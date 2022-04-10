"""颜色增加与颜色设定命令,作者:李兴球"""

import colorsys
def coloradd(color,dh):
    """颜色增加
        color是三元组,分别为0-255的值.此函数把颜色转换成hls模式,对h进行增加dh的操作
       然后转换回去,dh是小于1的浮点数.
    """
    if len(color)==3 :
        h,l,s, = colorsys.rgb_to_hls(color[0]/255,color[1]/255,color[2]/255)
        h =  h + dh
        r,g,b = colorsys.hls_to_rgb(h,l,s)
        return int(r*255),int(g*255),int(b*255)
    else:
        return color
addcolor = coloradd   #定义别名

def colorset(color):
    """设定颜色,color范围为1到360"""
    color = color % 360
    color = color / 360.0    
    r,g,b = colorsys.hsv_to_rgb(color,1.0,1.0)
    
    return int(r*255),int(g*255),int(b*255)
    
setcolor = colorset    #定义别名
 

if __name__ == "__main__":
        
    color = (255,0,0)
    for i in range(0,256,8):
        color = coloradd(color,i/255)
        print(color) 
