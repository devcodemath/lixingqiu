"""请把它定义成一个函数."""

numbers = [ 3,-5,-8,9,10,0,-88,-23]
counter = 0
for n in numbers:
    if n > 0 :
        print(n)
        counter = counter + 1

print("列表中有",counter,"个正数.")
