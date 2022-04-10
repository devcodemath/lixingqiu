"""
   txt2image.py
   本程序提供txt2image函数，它能把单行文本转换成图像。
   这个函数来源于李兴球编写的sprites模块中的同名函数。
"""
import os
from PIL import Image,ImageFont,ImageDraw,ImageTk

__author__= '李兴球'
__blog__ = 'www.lixingqiu.com'

def txt2image(txt,filename=None,fontfile="msyh.ttf",
              fontsize=18,color=(25,0,255,255)):
    """
        文本转图像实用小程序,只支持单行文本,默认为微软雅黑字体,
        txt：文本
        filename：要写入的文件名，如果为空则不写入，并且返回图形对象
        fontfile:ttf字体文件
        fontsize:字体大小
        color:颜色,通过写alpha值可支持半透明图形。        
    """
    
    windowsdir = os.environ.get('WINDIR')
    try:
       fnt = ImageFont.truetype(fontfile,fontsize)
    except:
       fontfile = 'msyh.ttc'                      # win10的微软雅黑为ttc
       p = windowsdir + os.sep + 'fonts' + os.sep + fontfile
       fnt = ImageFont.truetype(p,fontsize)
    
    size = fnt.getsize(txt)
    pic = Image.new('RGBA', size)
    d = ImageDraw.Draw(pic)
    d.text((0,0),txt,font=fnt,fill=color)
    if filename!=None:
        pic.save(filename)
        return size
    else:
        return pic

if __name__== "__main__":

    im = txt2image('本程序由李兴球编写')
    print(im)
