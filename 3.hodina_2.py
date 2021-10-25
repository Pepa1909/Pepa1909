from turtle import *
velikost_x= int(input("jak velké do x? "))
velikost_y= int(input("jak velké y? "))
speed(0)
up()
left(180)
forward(300)
left(90)
forward(250)
left(90)
down()
for _ in range(velikost_y): 
    for _ in range(velikost_x):
        for _ in range(4):
            forward(50)
            left(90)
        forward(50)
    left(180)
    forward(50*velikost_x)
    right(90)
    forward(50)
    right(90)
exitonclick()