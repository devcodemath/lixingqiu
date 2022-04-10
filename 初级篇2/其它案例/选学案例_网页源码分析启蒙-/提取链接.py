f = open("网页源码.txt")
htmlcode = f.read()
f.close()

sep = "href=\""                  #经分析源码,链接以href="开头,先以这个为分隔符

tmplist = htmlcode.split(sep)
for link in tmplist:
    url = link.split("\"")[0]    #把双引号后面的字符去掉.
    if "https://" in url : print(url)
    
