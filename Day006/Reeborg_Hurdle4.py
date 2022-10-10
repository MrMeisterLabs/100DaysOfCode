
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_reeborg():
    
    # Turn left and keep moving if no wall on the right
    
    turn_left()
    
    while wall_on_right():
        move()
        
   # When right wall ends, turn right, move one step and turn right again
        
    turn_right()
    move()
    turn_right()
    
    # If there's nothing in front, keep moving
   
    while front_is_clear():
        move()
      
    # Which means, if front is not clear, turn left.
    
    turn_left()
    
while not at_goal():
    
    if wall_in_front():
        
        jump_reeborg()
    
    else:
        move