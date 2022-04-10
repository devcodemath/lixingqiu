import turtle

cats = ['猫/0.gif','猫/1.gif','猫/2.gif','猫/3.gif',
        '猫/4.gif','猫/5.gif','猫/6.gif','猫/7.gif',
        '猫/8.gif','猫/9.gif', '猫/10.gif','猫/11.gif',
        '猫/12.gif','猫/13.gif','猫/14.gif','猫/15.gif']

for c in cats:
    turtle.addshape(c)

while True:
    for c in cats:
        turtle.shape(c)
        
