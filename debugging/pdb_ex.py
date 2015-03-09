import sys
from random import choice
import pdb

random1 = range(1, 13)
random2 = range(1, 13)

while True:
    print "To exit this game type 'exit'"
    pdb.set_trace()
    answer = raw_input("What is {} times {}? "
                       .format(choice(random1), choice(random2)))

    if answer == exit:
        print "Now exiting game!"
        sys.exit()

    elif answer == choice(random2) * choice(random1):
        print "Correct!"
    else:
        print "Wrong!"
