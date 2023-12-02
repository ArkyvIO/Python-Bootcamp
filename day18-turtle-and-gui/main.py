from turtle import Turtle, Screen
from defs import draw_square

# Create turtle
turtle = Turtle()
# Make the turtle an arrow
turtle.shape("arrow")

# Draw a square
draw_square(turtle)

# Create screen
screen = Screen()
# Make screen exit on click
screen.exitonclick()
