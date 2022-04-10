s = ""
while True:
    s = input("请输入一个字符串：")
    if s[::-1] == s :
        print("它是回文字符串。")
    else:
        print("不是回文字符串。")
    print()
    
