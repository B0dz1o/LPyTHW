from utils import die, def_input

def start():
    """Main function to go through start room"""
    print "You're at the crossroads."
    print "Should you choose the left or right road?"
    print "1.\tleft\n2.\tright"
    proper_choice = False
    
    while not proper_choice:
        proper_choice = crossroads()
    
    print "Thank you for playing. Come again later."
    return True
        
def crossroads():
    """
    Repeatable choice checker. If cannot determine, what
    should be done, returns False.
    """
    decision = def_input()
    if decision == '1' or decision == '1.':
        return creek()
    elif decision == '2' or decision == '2.':
        return dragon()
    else:
        print "Unknown choice. Try again."
        return False

