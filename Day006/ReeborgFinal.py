while not at_goal():
    
    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
        
    elif front_is_clear():
        move()
    
    else:
        turn_left()
        if wall_in_front():
            turn_left()
        move()
















