from turtle import Turtle, Screen
from defs import draw_square, draw_dashed_line, draw_increasing_shapes, draw_random_walk, draw_spirograph, hirst
import os

# Create turtle
turtle = Turtle()
# Make the turtle an arrow
turtle.shape("arrow")
# Turtle speed
turtle.speed(0)
# Create screen
screen = Screen()
screen.colormode(255)
# Draw a square
# draw_square(turtle)

# Draw dashed line
# draw_dashed_line(turtle, 100)

# Draw ever increasing shapes by sides
# draw_increasing_shapes(turtle, 10)

# Draw random with step count
# draw_random_walk(turtle, 100)

# Draw a spirograph
# draw_spirograph(turtle, 250, 50)

# Hirst dots
hirst(turtle, "image.jpg", 30, 10)


# Make screen exit on click
screen.exitonclick()
