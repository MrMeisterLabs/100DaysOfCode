# Find the Reeborg bot exercise on Reeborg's World website

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


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
    print(jump_counter)
    if jump_counter == 3:
        break