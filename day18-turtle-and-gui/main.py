from turtle import Turtle, Screen
from defs import draw_square, draw_dashed_line

# Create turtle
turtle = Turtle()
# Make the turtle an arrow
turtle.shape("arrow")

# Draw a square
# draw_square(turtle)

# Draw dashed line
draw_dashed_line(turtle, 100)

# Create screen
screen = Screen()
# Make screen exit on click
screen.exitonclick()
