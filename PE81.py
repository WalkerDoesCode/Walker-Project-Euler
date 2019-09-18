'''
Author: Walker Kroubalkian
Dynamic Approach to Project Euler Problem #81
'''

import time

f = open("PE81Grid.txt","r")

if(f.mode == "r"):
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(map(int,x.split(",")))
else:
    raise ValueError("Cannot read from file")

def projectEulerProblemEightyOne(myGrid):
    firstRow = []
    total = 0
    for x in myGrid[0]:
        total+=x
        firstRow.append(total)
    newGrid = [firstRow]
    for c in range(1,len(myGrid)):
        newRow = [myGrid[c][0]+newGrid[c-1][0]]
        for x in range(1,len(myGrid[c])):
            v = myGrid[c][x]+min(newGrid[c-1][x],newRow[x-1])
            newRow.append(v)
        newGrid.append(newRow)
    return newGrid[len(myGrid)-1][len(myGrid[0])-1]

start = time.time()
print projectEulerProblemEightyOne(realContents)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

427337
--- 0.00197601318359 seconds ---

for input of given grid.
'''