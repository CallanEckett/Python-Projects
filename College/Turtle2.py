#program written by Callan Eckett 23/10/2015
#This program is going to draw and animate a windmill

from tkinter import *
from turtle import *

turtle = Turtle()

turtleScreen = turtle.getscreen()
turtleScreen.bgcolor("yellow")

begin_poly()

for i in range(3):
	speed(1)
	forward(100)
	right(105)
	forward(50)
	right(105)
	forward(100)

	left(90)

end_poly()
register_shape("mill", get_poly())

reset()
shape("mill")
speed(1)
left(90)
up()
back(120)
down()
pensize(20)
pencolor("blue")
forward(180)

up()
color("green", "red")
turtlesize(outline=5)
speed(100)
angle = 3.6
for i in range(500):
	left(angle)
	angle -= 0.01

	if angle == 0:
		speed(0)

mainloop()