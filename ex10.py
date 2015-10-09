tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

j = 1
while j < 1000000 :
    for i in ["/","-","|","\\","|"]:
        j += 1
        print "%s   %d\r" % (i,j),
