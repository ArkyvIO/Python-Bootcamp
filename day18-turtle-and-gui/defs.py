from random import random, choice
import colorgram

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
        
def hirst(turtle, image, num_colors, lines):
    turtle.up()
    spacing = 50
    colors_rgb = []
    colors = colorgram.extract(image, num_colors)
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_to_add = (r, g, b)
        if r < 235 and g < 235 and b < 235:
            colors_rgb.append(color_to_add)
    for row in range(lines):
        for column in range(lines):
            turtle.color(choice(colors_rgb))  # Randomly choose a color from colors_rgb list
            turtle.dot(20)
            turtle.forward(spacing)
        if row % 2 == 0:
            turtle.backward(spacing)
            turtle.left(90)
            turtle.forward(spacing)
            turtle.left(90)
        else:
            turtle.backward(spacing)
            turtle.right(90)
            turtle.forward(spacing)
            turtle.right(90)
            