from sys import exit

def_reason = "You died for unknown reason"

def die(why = def_reason):
    """ Function for clean exit, printing the reason.
    Default reason is unknown.""" 
    print why, "Game over!"
    
def def_input(prompt = '> '):
    return raw_input(prompt)
