"""nonlocal测试.py"""
def function(init):
    counter = init
    def increase():
        nonlocal counter
        counter = counter + 1
        return counter
    
    return increase()

x = function(10)
print(x)
