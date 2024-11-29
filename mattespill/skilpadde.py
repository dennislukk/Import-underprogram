from turtle import *

shape("turtle")
shapesize(2)
bgcolor("darkblue")
color("yellow")

sides = 4
length = 100
angle = 360 / sides

for i in range(sides):
    forward(length)
    right(angle)

forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)

shape("turtle")
shapesize(2)
bgcolor("darkblue")
color("green")

for i in range(4):
    forward(100)
    right(90)


