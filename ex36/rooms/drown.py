from utils import die, def_input
from cave import cave
import start
from time import sleep

def drown():
    """
    Main function to go through 'Drown' room.
    """
    
    print "You still attempt to stay at the surface, but your armor",
    print "and weapons are too heavy."
    print "Should you continue your struggle or become defensless against " \
    "monsters?"    
    print "1.\tGet rid of all junk\n2.\tKeep fighting"
    proper_choice = False
    
    while not proper_choice:
        proper_choice = swim()
    return True
    
def swim():
    """
    Repeatable choice checker. If cannot determine, what
    should be done, returns False.
    """
    decision = def_input()
    if decision == '1' or decision == '1.':
        print "You managed to survive and got off the water."
        print "You wander carefully, but finally, you find a golden cave."
        print "Yaaaaaaaay!"
        return cave()
    elif decision == '2' or decision == '2.':
        print "Darkness covers your sight. You lose conscience..."
        for i in range(0,5):
            print '...'
            sleep(1)
        print "You lucky bastard! A fisherman caught you and brought you "\
        "home, where you can recover."
        print "You can start your adventure again!"
        return start.start()
    else:
        print "Unknown choice. Try again."
        return False    
