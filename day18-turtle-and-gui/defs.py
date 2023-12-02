from random import random, choice

def draw_square(turtle):
    turtle.speed(3)
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
        
def draw_dashed_line(turtle, line_length):
    turtle.speed(3)
    for _ in range(int(line_length / 10)):
        turtle.forward(10)
        turtle.up()
        turtle.forward(10)
        turtle.down()
        
def draw_increasing_shapes(turtle, iterations):
    turtle.speed(5)
    for sides in range(3, iterations + 3):
        turtle.color(random(), random(), random())
        for _ in range(sides):
            turtle.forward(100)
            turtle.right(360 / sides)
        sides += 1

def draw_random_walk(turtle, steps):
    turtle.speed(5)
    for _ in range(steps):
        turtle.color(random(), random(), random())
        turtle.forward(25)
        action = choice(["no_change", "right", "left"])
        if action == "no_change":
            continue
        elif action == "right":
            turtle.right(90)
        else:
            turtle.left(90)
            
def draw_spirograph(turtle, radius, circles):
    turtle.speed(0)
    for _ in range(circles):
        turtle.color(random(), random(), random())
        turtle.circle(radius)
        turtle.left(360 / circles)