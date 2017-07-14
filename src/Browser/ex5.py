#agree = 3
a ="%r %r %r %r"
print a %(1, 2, 'agree', 4)
print a %(a, a, a, a)
print a %("I had this thing.", 
          "That you could type up right", 
          "But it didn't Sing", 
          "So I' said goodnight")

x = "There are %d types of people." % 10

print "I said %s:." %x

fat_cat ="""
I'll do a list:
\t*Cat food
\t*Fishes
\t*Catnip\n\t*Grass
"""

fat_cat2 ='''
I'll do a list:
\t*Cat food
\t*Fishes
\t*Catnip\n\t*Grass
'''
print fat_cat

print fat_cat2

print "I like\n show list %s" %fat_cat2