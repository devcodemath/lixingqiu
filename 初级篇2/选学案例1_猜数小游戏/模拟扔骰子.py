from random import randint

min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print("正在扔骰子")
    print("结果是....")
    print(randint(min, max)) 

    roll_again = input("还要再扔吗?(y)")
