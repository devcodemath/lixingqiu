"""
   大坝.py
"""
import turtle

turtle.delay(0)
turtle.speed(0)
 
turtle.bk(200)
turtle.ht()
turtle.setheading(90)
for _ in range(150):
    turtle.fd(_)
    turtle.bk(_)
    turtle.setx(turtle.xcor()+1)
    
for _ in range(150):
    turtle.fd(100)
    turtle.bk(100)
    turtle.setx(turtle.xcor()+1)
    
for _ in range(150,0,-1):
    turtle.fd(_)
    turtle.bk(_)
    turtle.setx(turtle.xcor()+1)

turtle.done()
