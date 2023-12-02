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