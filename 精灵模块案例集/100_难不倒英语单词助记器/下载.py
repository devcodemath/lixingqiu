"""
   通过有道接口下载中学英语单词发音成mp3，
   为了儿子的英语学习，制作一个较完备的英语单词助记软件。
   这个程序把发音先下载下来。
"""
import os
import xlrd
import requests

def save_audio(word,content):    
    global c
    try:
       f = open('audio/' + word + ".mp3",mode = 'wb')
       f.write(content)
       f.close()
       c = c + 1
       print(word,'的发音成功存入  ',c)
    except:
       print(word,'的发音没有存入进去')        
    
filename="中学单词库.xls"
data = xlrd.open_workbook(filename) # 打开xls文件
table = data.sheets()[0]            # 打开第一张表
nrows = table.nrows                 # 获取表的行数
enhandict = {}                      # 英汉词典

for i in range(nrows):              # 循环逐行
    word = str(table.row_values(i)[1])
    if word.endswith("\xa0"):word = word[:-1]
    yb = table.row_values(i)[2]     # 音标
    fy = table.row_values(i)[3]     # 翻译
    enhandict[word] = (fy,yb)       # 加入到英汉词典

c = 0
for word in enhandict:
    if os.path.exists('audio/' + word + ".mp3"):continue  # 已存在则不下载
    try:
        r = requests.get('http://dict.youdao.com/dictvoice?type=1&audio=' + word)
        save_audio(word,r.content)
    except:
        pass
