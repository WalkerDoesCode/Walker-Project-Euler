'''
Author: Walker Kroubalkian
Dynamic Approach to Project Euler Problem #82
'''

import time

f = open("PE82Grid.txt","r")

if(f.mode == "r"):
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(map(int,x.split(",")))
else:
    raise ValueError("Cannot read from file")

def projectEulerProblemEightyTwo(myGrid):
    newGrid = []
    rows = len(myGrid)
    cols = len(myGrid[0])
    for x in range(rows):
        newGrid.append([myGrid[x][0]])
    for y in range(1,cols):
        theColumn = []
        for x in range(rows):
            theColumn.append(myGrid[x][y])
        forwardPartials = [0]
        t = 0
        for x in theColumn:
            t+=x
            forwardPartials.append(t)
        backwardPartials = [t]
        for x in range(rows-1,-1,-1):
            t-=theColumn[x]
            backwardPartials.append(t)
        newColumn = []
        for z in range(rows):
            minFound = newGrid[z][y-1]+myGrid[z][y]
            for a in range(rows):
                if(a<z):
                    total = myGrid[z][y] + forwardPartials[z]-forwardPartials[a] + newGrid[a][y-1]
                elif(a>z):
                    total = myGrid[z][y] + forwardPartials[a+1] - forwardPartials[z+1] + newGrid[a][y-1]
                else:
                    total = minFound
                if(total<minFound):
                    minFound = total
            newColumn.append(minFound)
        for x in range(rows):
            newGrid[x].append(newColumn[x])
    minFound = newGrid[0][cols-1]
    for a in range(1,rows):
        v = newGrid[a][cols-1]
        if(v<minFound):
            minFound = v
    return minFound


start = time.time()
print projectEulerProblemEightyTwo(realContents)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

260324
--- 0.0795319080353 seconds ---

for input of given grid.
'''