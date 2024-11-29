from turtle import *

shape("turtle")
shapesize(2)
bgcolor("darkblue")
color("yellow")
speed(300)

def polygon(sides, length):
    angle = 360 / sides
    
    for i in range(sides):
        forward(length)
        right(angle)

polygon(4, 100) 

polygon(3, 100)
polygon(5, 100)
polygon(6, 100)
forward(125)
right(180)
polygon(3, 150)
polygon(5, 150)
polygon(7, 150)


def polylines(sides, length, angle):
    for i in range(sides):
        forward(length)
        right(angle)

polylines(91, 200, 91)

def spiral(sides, length, angle):
    for i in range(sides):
        forward(length)
        right(angle)
        length = length + 5

spiral(100, 5, 125)

done()