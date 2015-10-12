# -*- coding: utf-8 -*-

def prompt():
    return raw_input('> ')

print "Stoisz przed strumykiem. Co robisz?"
print "1. Idź dalej drogą."
print "2. Spróbuj przepłynąć strumyk."

droga = prompt()

if droga == "1":
    print "Spotykasz smoka. Co robisz?"
    print "1. Idziecie na piwo."
    print "2. Atakujesz."
    print "3. Atakujesz, ale mocniej :)"
    
    smok = prompt()
    
    if smok == "1" or smok == "3":
        print "Wygrałeś!"
    elif smok == "2":
        print "Za słabo, smok cię pokonał. Żegnaj!"
    else:
        "Za długo zwlekałeś z decyzją, przegrałeś!"

if droga == "2":
    print "Syrena wciąga cię pod wodę. Szybko, decyduj!"
    print "1. Próbuj się wyswobodzić."
    print "2. Budzisz się."
    
    syrena = prompt()
    
    if syrena == "1":
        print "Niestety, nie udało się. Zginąłeś w odmętach."
    elif syrena == "2":
        print "Uff, to był tylko sen."
    else:
        print "Nie wiesz, co ze sobą począć, przegrałeś!"
    
else:
    print "Nieprawidłowy wybór, koniec gry!"

        

