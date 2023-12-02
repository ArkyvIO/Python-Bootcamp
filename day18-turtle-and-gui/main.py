from turtle import Turtle, Screen
from defs import draw_square, draw_dashed_line, draw_increasing_shapes

# Create turtle
turtle = Turtle()
# Make the turtle an arrow
turtle.shape("arrow")

# Draw a square
# draw_square(turtle)

# Draw dashed line
# draw_dashed_line(turtle, 100)

# Draw ever increasing shapes by sides
draw_increasing_shapes(turtle, 10)

# Create screen
screen = Screen()
# Make screen exit on click
screen.exitonclick()
