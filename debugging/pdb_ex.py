import sys
from random import choice
import pdb

random1 = range(1, 13)
random2 = range(1, 13)

while True:
    print "To exit this game type 'exit'"
    #pdb.set_trace()
    num1 = choice(random1)
    num2 = choice(random2)
    answer = raw_input("What is {} times {}? ".format(num1, num2))

    if answer == "exit":
        print "Now exiting game!"
        sys.exit()

    elif int(answer) == num1 * num2:
        print "Correct!"
    else:
        print "Wrong!"
