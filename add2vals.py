from struct import calcsize
import sys
from unittest import result
import calc

argnumers = len(sys.argv) -1

if argnumbers == 2 :
    print("")
    print("The result is " + str(calc.add2(str(sys.argv[1]), str(sys.arg[2]))))
    print("")
    sys.exit(0)

if argnumbers != 2 :
    print("")
    print("You entered " +str(argnumbers) + " values")
    print("")
    sys.exit(1)