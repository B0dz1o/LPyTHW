# -*- coding: utf-8 -*-
from utils import die, def_input
from cave import cave

def dragon():
    """
    Main function to go through 'Dragon' room.
    """
    
    print "A hungarian dragon stands in your way!"
    print "What's your decision?"
    print "1.\tZ różczki\n2.\tZ aksa"
    proper_choice = False
    
    while not proper_choice:
        proper_choice = dragon_fight()
    return True
    
def dragon_fight():
    """
    Repeatable choice checker. If cannot determine, what
    should be done, returns False.
    """
    decision = def_input()
    if decision == '1' or decision == '1.':
        print "Ciućmoku", \
        "Jesteś rycerzem, a nie mejdżem."
        print "You're a knight, cannot cast magic."
        die("Dragon sets you on fire")
    elif decision == '2' or decision == '2.':
        print "One quick slash along the belly of the beast",
        print "is more than enough. No time to celebrate, though.", \
        "You cut of one dragonscale as your trophy and follow the way."
        return cave()
    else:
        print "Unknown choice. Try again."
        return False    
