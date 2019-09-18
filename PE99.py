'''
Author: Walker Kroubalkian
Logarithm Approach to Project Euler Problem #99
'''

import time
from math import log

f = open("PE99Exponents.txt","r")

if(f.mode == "r"):
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(map(int,x.split(",")))
else:
    raise ValueError("Cannot read from file")

def projectEulerProblemNinetyNine(myList):
    a = sorted(myList, key = lambda x: x[1]*log(x[0]))
    return myList.index(a[len(a)-1])+1

start = time.time()
print projectEulerProblemNinetyNine(realContents)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

709
--- 0.000494003295898 seconds ---

for input of given list of exponents.
'''