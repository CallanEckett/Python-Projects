#Program written by Callan Eckett
#This program will draw a shape on the screen and allow the user to move it.

#importing all functions from tkinter and turtle libraries 
from tkinter import *
from turtle import *

#set up turtle
turtle = Turtle()

#set up screen
turtleScreen = turtle.getscreen()
#set up the background colour of the screen
turtleScreen.bgcolor("pink")
write("Shape Moving Program", font=("Arial", 24, "bold"))

shapeName = textinput("Please answer the question", "Type in the shape")
shapeLineColor = textinput("Please answer the question", "Type in the shape line color")
shapeFillColor = textinput("Please answer the question", "Type in the shape fill color")
shapeSize = textinput("Please answer the question", "Type in the shape size")

up()
goto(0, 0)
shape(shapeName)
color(shapeLineColor)
fillcolor(shapeFillColor)

shapesize(int(shapeSize))
up()
goto(0, -50)
down()
begin_fill()
up()
onscreenclick(goto,1)

mainloop()