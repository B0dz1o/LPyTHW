word_indices = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth']
indices = ['1st', '2nd', '3rd']
for i in range(4,10):
    index_str = "%dth" % i
    indices.append(index_str)

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
    
def animal_index(index):
    return animals[index]

def animal(i):
    if isinstance(i, basestring):
        index = int(i[0]) - 1
        return animal_index(index)
    else:
        return animal_index(i)
        
def index_transform(index):
    if isinstance(index, basestring):
        return int(index[0]) - 1
    else:
        return index        
        
ex_tuple = (1, '3rd', '1st', 3, '5th', 2, '6th', 4)
for i in ex_tuple:
    index = index_transform(i)
    tup = (word_indices[index], indices[index], index, animal(index))
    tup2 = (index, indices[index], animal(index))
    print "The %s (%s) animal is at %d and is a %s." % tup
    print "The animal at %d is the %s animal and is a %s\n" % tup2
