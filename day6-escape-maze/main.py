def turn_right():
    for x in range(0,3):
        turn_left()

while front_is_clear():
    move()

turn_left()
        
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()