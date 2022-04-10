"""字典方法演示.py"""

words = {'apple':"苹果",'peach':'桃','banana':'香蕉','red':'红色','cyan':'青色'}
print(words.get('red'))         # 得到键名为red的值 
 
print(words.get('orange'))      # 得到键名为orange的值，它并不存在值 
print(words.pop('apple'))       # 弹出键名为apple的值，并从字典删除apple
print(words)

words.popitem()                 # 随机弹出键值对
print(words)
 
words.setdefault('yellow','黄') # 设置键名为yellow的值
 
print(words)
words.setdefault('yellow','黑') # 由于键名已存在，所以返回其值
print(words)

d = {}.fromkeys(['a','b','c'])  # 从序列创建字典，所有值者为None
print(d)

words.update(d)                 # 更新words字典
print(words)
