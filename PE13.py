'''
Author: Walker Kroubalkian
Basic Python Approach to Project Euler Problem #13
'''

import time
f = open("PE13Numbers.txt","r")

if f.mode=="r":
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(int(x))
else:
    raise ValueError("Cannot read from file")

def projectEulerProblemThirteen(numbers, n):
    total = 0
    for x in numbers:
        total+=x
    return str(total)[0:n]

start = time.time()
print projectEulerProblemThirteen(realContents, 10)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

5537376230
--- 1.59740447998e-05 seconds ---

for input of given numbers and n=10
'''