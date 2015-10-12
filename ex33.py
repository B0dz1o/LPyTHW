def while_tester(limes, increment = 1):
    i = 0
    numbers = []

    while i < limes :
        print "At the top i is %d" % i
        numbers.append(i)
        
        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d\n" % i
        
        
    print "The numbers: "

    for num in numbers:
        print num,
        
def for_tester(limes, increment = 1):
    i = 0
    numbers = []
    
    for i in range(0, limes, increment):
        print "At the top i is %d" % i
        numbers.append(i)
        
        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d\n" % i
    
        print "The numbers: "

    for num in numbers:
        print num,

