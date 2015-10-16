from utils import die, def_input
import time

def drown():
    """
    Main function to go through 'Cave' room.
    """
    
    print "You are at the end of your journey!"
    print "A shitload of gold streches further than you can see.\n" \
    "How much do you take?"
    proper_choice = False
    
    while not proper_choice:
        proper_choice = gold()
    return True
    
def gold():
    """
    Repeatable choice checker. If cannot determine, what
    should be done, returns False.
    """
    decision = def_input()
    try:
        gold = int(decision)
    except ValueError:
        print "Unknown choice. Try again."
        return False
    if gold > 50:
        print "You cannot carry that much!"
    elif gold > 10 and gold <= 50:
        print "It's a heavy load, but you manage to move."
        return goblin(True)
    elif gold > 0 and gold <= 10
        print "You're not greedy! You leave the cave to come back home."
        return goblin(False)
        
        
def goblin(is_heavy):        
    """
    Event - goblins try to kill you. Are you too heavy to run away?
    """
    print "Some goblins try to attack you as you leave the cave!"

    if is_heavy == False:
        print "Your treasure is not heavy so you run away with ease."
        return True
    else:
        print "You can barely move, they will kill you! ",\
        "You're outnumbered!"
        print "Quick, press Enter to leave all gold here and run!"
        start_time = time.time()
        dec = raw_input()
        end_time = time.time()
        if end_time - start_time > 1.5:
            print "You waited too long. DIE BYATCH!"
            die("Goblins kill you!")
        elif dec != ''
            print "You couldn't decide what to do, so they butchered you!"
            die("Goblins kill you!")
        else:
            print "You had to leave the treasure, but managed to stay "\
            "alive."        
            return True
