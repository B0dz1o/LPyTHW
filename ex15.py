from sys import argv

script, filename = argv

txt = open("res/" + filename)

print "Here's your file %r:" % filename
print txt.read()
txt.close()

#print "Type the filename again:"
#file_again = raw_input("> ")

#txt_again = open("res/" + file_again)

#print txt_again.read()
