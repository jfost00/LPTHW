from sys import exit
from time import sleep
energy = False
energy2 = False
sword = False
monster1 = False
monster2 = False
monster3 = False

def empty_any():
    print "This room is empty: "
    print "You may choose to go 'forward', 'backward', 'left', or 'right'"
    next = raw_input("> ")
    
    if next == "forward" and monster3 == False:
        monster_room3()
    elif next == "forward" and monster3 == True:
        room3()
    elif next == "right" and monster1 == False:
        monster_room1()
    elif next == "right" and monster1 == True:
        room1()
    elif next == "backward":
        startover()
    elif next == "left" and energy == True:
        energy_room_over()
    elif next == "left" and energy == False:
        energy_room()
    else:
        dead("You stumble around till you starve.")
    
def empty_left():
    print "This room is empty: "
    print "You may choose to go 'forward' or 'left'"
    next = raw_input("> ")
    if next == "forward" and monster1 == False:
        monster_room1()
    elif next == "forward" and monster1 == True:
        room1()
    elif next == "left":
        startover()
    else: 
        dead("You stumble around till you starve.")
    
def empty_right():
    print "This room is empty: "
    print "You may choose to go 'backward' or 'right'"
    next = raw_input("> ")
    if next == "backward" and energy == False:
        energy_room()
    if next == "backward" and energy == True:
        energy_room_over()
    elif next == "right" and monster3 == False:
        monster_room3()
    elif next == "right" and monster3 == True:
        room3()
    else: 
        dead("You stumble around till you starve.")
    
        
    
def empty_forward():
    print "This room is empty: "
    print "You can only go 'forward'"
    next = raw_input("> ")
    if next == "forward":
        big_monster()
    else: 
        dead("You stumble around till you starve.")

### energy 2 
def energy_room_over2():
    print "You have already received the energy"
    energy = True
    print "You may choose to go 'forward' or 'right'"
    next = raw_input("> ")

    if next == "forward": 
        empty_forward()
    elif next == "left" and monster3 == False:
        monster_room3()
    elif next == "left" and monster3 == True:
        room3()
    elif next == "right" and monster2 == False:
        monster_room2()
    elif next == "right" and monster2 == True:
        room2()
    elif next == "backward" and monster1 == False:
        monster_room1()
    elif next == "backward" and monster1 == True: 
        room1()
    else:
        dead("You stumble around till you starve.")

def energy_room2():
    print "This room has ENERGY!!"
    print "You have recieved a power boost"
    energy = True
    print "You may choose to go 'forward' 'left', 'backward', or 'right'"
    next = raw_input("> ")
    
    if next == "forward": 
        empty_forward()
    elif next == "left" and monster3 == False:
        monster_room3()
    elif next == "left" and monster3 == True:
        room3()
    elif next == "right" and monster2 == False:
        monster_room2()
    elif next == "right" and monster2 == True:
        room2()
    elif next == "backward" and monster1 == False:
        monster_room1()
    elif next == "backward" and monster1 == True: 
        room1()
    else:
        dead("You stumble around till you starve.")
###

### energy         
def energy_room_over():
    print "You have already received the energy"
    energy = True
    print "You may choose to go 'forward' or 'right'"
    next = raw_input("> ")
    
    if next == "forward":
        empty_right()
    elif next == "right":
        empty_any()
    else:
        dead("You stumble around till you starve.")
    
def energy_room():
    print "This room has ENERGY!!"
    print "You have recieved a power boost"
    energy = True
    print "You may choose to go 'forward' or 'right'"
    next = raw_input("> ")
    
    if next == "forward":
        empty_right()
    elif next == "right":
        empty_any()
    else:
        dead("You stumble around till you starve.")
###
        
        
def sword_room_over():
    print "You have already received the sword."
    sword = True
    print "You may choose to go 'forward or 'left'"
    next = raw_input("> ")
    
    if next == "forward" and monster2 == False:
        monster_room2()
    elif next == "forward" and monster2 == True:
        room2()
    elif next == "left" and monster1 == False:
        monster_room1()
    elif next == "left" and monster1 == True:
        room1()
    else:
        dead("You stumble around till you starve.")
        
def sword_room():
    print "This room has a sword!!"
    print "You have recieved the sword"
    sword = True
    print "You may choose to go 'forward or 'left'"
    next = raw_input("> ")
    
    if next == "forward" and monster2 == False:
        monster_room2()
    elif next == "forward" and monster2 == True:
        room2()
    elif next == "left" and monster1 == False:
        monster_room1()
    elif next == "left" and monster1 == True:
        room1()
    else:
        dead("You stumble around till you starve.")
        
    
    
def monster_room1():
    print "This room has a monster!"
    print "The monster is attacking"
    print "You can either laugh or fight:"
    next = raw_input("> ")
    if next == "fight":
        print "The monster is dead"
        monster1 = True
        print "You may choose to go 'forward', 'backward', 'left', or 'right'"
        
        next = raw_input("> ")
        if next == "forward" and energy == False:
            energy_room2()
        elif next == "forward" and energy == True:
            energy_over_room2()
        elif next == "backward":
            empty_left()
        elif next == "left":
            empty_any()
        elif next == "right" and sword == False:
            sword_room()
        elif next == "right" and sword == True:
            sword_room_over()
        else: 
            dead("You stumble around till you starve.")
        
        
#    elif next == "laugh":
#        dead("The monster killed you!")
    
    
def monster_room2():
    print "This room has a monster!"
    print "The monster is attacking"
    print "You can either laugh or fight:"
    next = raw_input("> ")
    if next == "fight":
        print "The monster is dead"
        monster2 = True
        print "You may choose to go 'forward', 'backward', or 'left'"
        next = raw_input("> ")
        
        if next == "forward": 
            empty_forward()
        elif next == "backward" and sword == False:
            sword_room()
        elif next == "backward" and sword == True:
            sword_room_over()
        elif next == "left" and energy2 == False:
            energy_room2()
        elif next == "left" and energy2 == True:
            energy_over_room2()
        else: 
            dead("You stumble around till you starve.")
            
        
#    elif next == "laugh":
#        dead("The monster killed you!")

def monster_room3():
    print "This room has a monster!"
    print "The monster is attacking"
    print "You can either laugh or fight:"
    next = raw_input("> ")    
    if next == "fight":
        print "The monster is dead"
        monster3 = True
        print "You may choose to go 'forward', 'backward', 'left', or 'right'"
        next = raw_input("> ")
        
        if next == "forward":
            empty_forward()
        elif next == "left":
            empty_right()
        elif next == "right" and energy2 == False:
            energy_room2()
        elif next == "right" and energy2 == True:
            energy_over_room2()
        else: 
            dead("You stumble around till you starve.")
        
#    elif next == "laugh":
#        dead("The monster killed you!")
    
    
def room1():
    print "You have defeated the monster"
    print "You may choose to go 'forward', 'backward', 'left', or 'right'"    
    next = raw_input("> ")
    if next == "forward" and energy == False:
        energy_room2()
    elif next == "forward" and energy == True:
        energy_over_room2()
    elif next == "backward":
        empty_left()
    elif next == "left":
        empty_any()
    elif next == "right" and sword == False:
        sword_room()
    elif next == "right" and sword == True:
        sword_room_over()
    else: 
        dead("You stumble around till you starve.")
    
def room2():
    print "You have defeated the monster"
    print "You may choose to go 'forward', 'backward', or 'left'"
    next = raw_input("> ")

    if next == "forward": 
        empty_forward()
    elif next == "backward" and sword == False:
        sword_room()
    elif next == "backward" and sword == True:
        sword_room_over()
    elif next == "left" and energy2 == False:
        energy_room2()
    elif next == "left" and energy2 == True:
        energy_over_room2()
    else: 
        dead("You stumble around till you starve.")

def room3():
    print "You have defeated the monster"
    print "You may choose to go 'forward', 'backward', 'left', or 'right'"
    next = raw_input("> ")

    if next == "forward":
        empty_forward()
    elif next == "left":
        empty_right()
    elif next == "right" and energy2 == False:
        energy_room2()
    elif next == "right" and energy2 == True:
        energy_over_room2()
    else: 
        dead("You stumble around till you starve.")
    
    
def big_monster():
    print "This is the MONSTER!"
    print "THE MONSTER IS ATTACKING!!!"
    print "Do you laugh, fight, or use the sword??"
    next = raw_input("> ")
    
    if next == "sword":
        prize()
    
def prize(): 
    print "CONGRATULATIONS, You have beaten the game!"
    print ''' 
    #################
    ###           ###
    ###     $     ###
    ###    $$$    ###
    ###   $$$$$   ###
    ###  $$$$$$$  ###
    ### $$$$$$$$$ ###
    #################
    '''

def dead(why):
    print "\n" * 3
    print why, "game over"
    print "Try again later..."
    exit(0)
    
def startover():
    print "You are back at the begining:"
    
    next = raw_input("> ")
    
    if next == "forward":
        empty_any()
    elif next == "right":
        empty_left()
    else:
        dead("You stumble around till you starve.")
    
def start():
    print '''
    ##############################################################
    ### The Maze Game                                          ###
    ###--------------------------------------------------------###
    ### ~ Created by Jeff Foster                               ###
    ### all of the source code will be available               ###
    ### on my github account https://github.com/jfost00        ###
    ###                                                        ###
    ### Object: find the end of the maze                       ###  
    ###                          _____  _----                  ###
    ###  O     - |\    /|   /\       / |                       ###  
    ### \|/    - | \  / |  /__\    /   |-----                  ###
    ### / /    - |  \/  | /    \ /____ |_____                  ###  
    ###                                                        ###
    ###                                                        ### 
    ##############################################################
    '''
    sleep(3)
    print "You have entered the maze: "
    print "You may choose to go 'forward' or 'right'"
    
    next = raw_input("> ")
    
    if next == "forward":
        empty_any()
    elif next == "right":
        empty_left()
    else:
        dead("You stumble around till you starve.")
        
start()