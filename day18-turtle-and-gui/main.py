from turtle import Turtle, Screen
from defs import draw_square, draw_dashed_line, draw_increasing_shapes, draw_random_walk

# Create turtle
turtle = Turtle()
# Make the turtle an arrow
turtle.shape("arrow")
# Turtle line thickness, default 1
turtle.pensize(10)

# Draw a square
# draw_square(turtle)

# Draw dashed line
# draw_dashed_line(turtle, 100)

# Draw ever increasing shapes by sides
# draw_increasing_shapes(turtle, 10)

# Draw random with step count
draw_random_walk(turtle, 100)

# Create screen
screen = Screen()
# Make screen exit on click
screen.exitonclick()
