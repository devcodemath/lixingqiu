"""百度新闻首页采集器.py"""
import os
import requests               # 可通过      pip3 install requests 安装
from bs4 import BeautifulSoup # 导入靓汤类，pip install beautifulsoup4安装 

url = "https://news.baidu.com"

resp = requests.get(url,timeout=5, verify=True)# 返回响应对象
#print(dir(resp))                              # status_code为200正常     
htmlcode = resp.text                      # 网页的HTML代码
soup = BeautifulSoup(htmlcode,"lxml")     # 新建靓汤对象
 
links = soup.find_all('a')                # 查找所有a标签
urls = {}                                 # 新建字典
for link in links:                        # 迭代所有链接
    href = link.get('href')               # 取链接
    if href == None :continue             # 过滤没有href属性的
    if not "http://" in href : continue   # 过滤没有http://的
    if len(link.text) < 5 :continue       # 过滤链接文本小于5的    
    if href[-4::] == ".apk": continue     # 过滤最后4个字符为.apk的
    if "baidu.com" in href or len(href)>50 : 
        urls[href] = link.text            # 满足条件则放入字典
 
html = ""
for link in urls:                         # 迭代每个链接
    html = html + "<p><a target=_blank href='"
    html = html + link + "'>" + urls[link] + "</a></p>\n"

filename = "百度新闻列表.html"
f = open(filename,mode='w')               # 打开文件
f.write(html)                             # 写入合成的文本
f.close()                                 # 关闭文件
os.system(filename)                       # 调用默认程序打开文件

    
