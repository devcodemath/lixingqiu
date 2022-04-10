import sys

parameters = sys.argv

if len(parameters)>1:    
   expression = "".join(parameters[1:])
   print(eval(expression))
else:
    print("用法：run.py 1+2+3")
