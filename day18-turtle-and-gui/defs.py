def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
        
def draw_dashed_line(turtle, line_length):
    for _ in range(int(line_length / 10)):
        turtle.forward(10)
        turtle.up()
        turtle.forward(10)
        turtle.down()
        
def draw_increasing_shapes(turtle, iterations):
    for sides in range(3, iterations + 3):
        for _ in range(sides):
            turtle.forward(100)
            turtle.right(360 / sides)
        sides += 1
