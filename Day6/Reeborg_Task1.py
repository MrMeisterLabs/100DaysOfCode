# Head over to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# to play the game

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

    
def walk_reeborg():
    move()
    jump()
    move()
    jump()
    
jump_counter = 0    
while True:    
    walk_reeborg()
    jump_counter +=1
    if jump_counter == 6:
        walk()
        jump()
        break