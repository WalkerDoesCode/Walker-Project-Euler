'''
Author: Walker Kroubalkian
Dynamic Approach to Project Euler Problem #67
'''

import time

f = open("PE67Triangle.txt","r")

if(f.mode == "r"):
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(map(int,x.split()))
else:
    raise ValueError("Cannot read from file")

def projectEulerProblemSixtySeven(triangle):
    rows = len(triangle)
    currentRow = triangle[rows-1]
    c = (rows-2)
    while(c>=0):
        temp = []
        for i in range(c+1):
            temp.append(triangle[c][i] + max(currentRow[i],currentRow[i+1]))
        currentRow = temp
        c-=1
    return currentRow[0]

start = time.time()
print projectEulerProblemSixtySeven(realContents)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

7273
--- 0.00120997428894 seconds ---

for input of triangle = given triangle
'''