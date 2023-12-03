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

plausible_choices = ['s', 'd', 'r', 'h', 'i']

choice = input("Would you like a (s)quare, (d)ashed, (i)ncreasing, (r)andom, or (h)irst grahpic: ")[0].lower()

while choice not in plausible_choices:
    choice = input("That choice wasn't recognized, please try again.")
    
if choice == "s":
    # Draw a square
    draw_square(turtle)
elif choice == "d":
    # Draw dashed line
    draw_dashed_line(turtle, 100)
elif choice == "i":
    # Draw ever increasing shapes by sides
    draw_increasing_shapes(turtle, 10)
elif choice == "r":
    # Draw random with step count
    draw_random_walk(turtle, 100)
elif choice == "s":
    # Draw a spirograph
    draw_spirograph(turtle, 250, 50)
elif choice == "h":
    # Hirst dots
    hirst(turtle, "image.jpg", 30, 10)


# Make screen exit on click
screen.exitonclick()
