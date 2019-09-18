'''
Author: Walker Kroubalkian
Dynamic Approach to Project Euler Problem #18
'''

import time

f = open("PE18Triangle.txt","r")

if(f.mode == "r"):
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(map(int,x.split()))
else:
    raise ValueError("Cannot read from file")

def projectEulerProblemEighteen(triangle):
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
print projectEulerProblemEighteen(realContents)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

1074
--- 5.19752502441e-05 seconds ---

for input of triangle = given triangle
'''