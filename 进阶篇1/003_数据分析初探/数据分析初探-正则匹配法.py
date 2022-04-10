"""数据分析初探-正则匹配法.py
本程序把诸如 'http://www.nkjfrc.com/PersonalDetail.aspx?ID=23114'
这样的链接查找出来."""
import re

f = open("人才网页源码.html")
htmlcode = f.read()
f.close()

reg = re.compile("http://www.nkjfrc.com/PersonalDetail.aspx\?ID=\d+")

result = re.findall(reg,htmlcode)

for link in result:
    print(link)

