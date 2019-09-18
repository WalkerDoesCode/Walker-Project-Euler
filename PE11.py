'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #11
'''

import time
f = open("PE11Grid.txt","r")

if f.mode=="r":
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(map(int,x.split()))
else:
    raise ValueError("Cannot read from file")

def projectEulerProblemEleven(grid, l):
    rows = len(grid)
    cols = len(grid[0])
    maxProduct = -1
    for r in range(rows):
        for c in range(cols-l):
            total = 1
            for x in range(l):
                total*=grid[r][c+x]
            if(total>maxProduct):
                maxProduct = total
    
    for r in range(rows-l):
        for c in range(cols):
            total = 1
            for x in range(l):
                total*=grid[r+x][c]
            if(total>maxProduct):
                maxProduct = total
    
    for r in range(rows-l):
        for c in range(cols-l):
            total = 1
            for x in range(l):
                total*=grid[r+x][c+x]
            if(total>maxProduct):
                maxProduct = total
    
    for r in range(rows-l):
        for c in range(l-1,cols):
            total = 1
            for x in range(l):
                total*=grid[r+x][c-x]
            if(total>maxProduct):
                maxProduct = total
    
    return maxProduct

start = time.time()
print projectEulerProblemEleven(realContents, 4)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

70600674
--- 0.000658988952637 seconds ---

for input of given grid
'''

    