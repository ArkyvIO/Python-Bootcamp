from turtle import Turtle, Screen

def move_forward():
    bob.forward(10)

bob = Turtle()
screen = Screen()

screen.listen()

screen.onkey(move_forward, "Up")

screen.exitonclick()