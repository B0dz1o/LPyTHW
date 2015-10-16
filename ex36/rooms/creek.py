from utils import die, def_input
from cave import cave
from drown import drown

def creek():
    """Main function to go through 'Creek' room"""
    print "After a few days of wandering, you've found a creek."
    print "When you kneel to take a sip of crystal clear water,",
    print "a luring song comes to your ears."
    print "You meet a siren, endowed with an astonishing voice."
    print "Should you come closer?"
    print "1.\tYes\n2.\tNo, resist your temptation"
    proper_choice = False
    
    while not proper_choice:
        proper_choice = siren()
    return True
        
        
def siren():
    """
    Repeatable choice checker. If cannot determine, what
    should be done, returns False.
    """
    decision = def_input()
    if decision == '1' or decision == '1.':
        print "Siren attempts to suffocate you.", \
        "You're exhausted, but manage to let go of her grip.", \
        "Yet you fall to the water and let the flow take you away."
        return drown()
    elif decision == '2' or decision == '2.':
        print "It could be the love of your life,",
        print "but what the heck. Adventure, here I go!"
        return cave()
    else:
        print "Unknown choice. Try again."
        return False



