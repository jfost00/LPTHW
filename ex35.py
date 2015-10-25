from sys import exit

def gold_room(): 
    print "\n" * 3
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
    print "This room is full of gold. How much will you take?"
    
    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("not a number")
        
    if how_much <= 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else: 
        dead("You greedy bastard!")
        
def bear_room(): 
    print "\n" * 3
    print ''' 
    #################
    ###           ###
    ### ()____()  ###
    ### | o   o | ###
    ###  | \@/ |  ###
    ###   -----   ###
    ###  (     (  ###
    #################
    '''
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    
    while True:
        next = raw_input("> ")
        
        if next == "Take honey":
            dead("The bear looks at you and then slaps your face off.")
        elif next == "Taunt bear" and not bear_moved:
            print "\n" * 3
            print ''' 
            #################
            ###           ###
            ### ________  ###
            ### |      |  ###
            ### |      |  ###
            ###  o -----  ###
            ### |      |  ###
            #################
            '''
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "Taunt bear" and bear_moved: 
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "Open door" and bear_moved: 
            gold_room()
        else: 
            print "I got no idea what that means (invalid command)"
            
def cthulhu_room():
    print "\n" * 3
    print '''
    ##################
    ###  _ _       ### 
    ###  0 0       ###
    ###   >        ### 
    ### {(o(oo}    ### 
    ###  {o)(o)}   ### 
    ###   {{o}{O}} ###
    ###      (o)   ###
    ###            ###    
    ##################
    '''
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    next = raw_input("> ")
    
    if "flee" in next:
        startover()
    elif "eat my head" in next: 
        dead("Well that was tasty")
    else:
        cthulhu_room()
        
def dead(why):
    print "\n" * 3
    print why, "Good job! game over"
    print "Try again later..."
    exit(0)
    
def startover():
    print "\n" * 3
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around till you starve.")
    
def start():
    print '''
    #########################
    ### Gold Runner       ###
    ###----------------------
    ###   O      $$       ###
    ###  -|-    $$$$      ###
    ###  / /   $$$$$$     ###
    ###----------------------
    ### Created: Zed Shaw ###
    ### LPTHW             ###
    #########################
    '''
    print "\n" * 5
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    next = raw_input("> ")
    
    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around till you starve.")
        
start()
