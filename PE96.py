'''
Author: Walker Kroubalkian
Backtracking Brute Force Approach to Project Euler Problem #96
'''

import time

def stringToArray(myString):
    a = []
    for x in myString:
        a.append(int(x))
    return a

f = open("PE96Sudoku.txt","r")

if f.mode=="r":
    contents = f.readlines()
    realContents = []
    i = 0
    for x in contents:
        if(i%10!=0):
            if x[len(x)-1]=="\n":
                realContents.append(stringToArray(x[0:len(x)-1]))
            else:
                realContents.append(stringToArray(x))
        i+=1
else:
    raise ValueError("Cannot read from file")

def countZeros(n):
    t = 0
    for x in n:
        for y in x:
            if y==0:
                t+=1
    return t

def copyArray(n):
    t = []
    for x in n:
        r = []
        for y in x:
            r.append(y)
        t.append(r)
    return t

def optionCell(n,r,c):
    if(n[r][c]!=0):
        return []
    notPoss = []
    for x in range(9):
        notPoss.append(n[r][x])
        notPoss.append(n[x][c])
    lr = r-r%3
    tc = c-c%3
    for a in range(3):
        for b in range(3):
            notPoss.append(n[lr+a][tc+b])
    options = []
    for d in range(1,10):
        if d not in notPoss:
            options.append(d)
    return options

def optionRow(n,r):
    rowOptions = []
    for c in range(9):
        rowOptions.append(optionCell(n,r,c))
    return rowOptions

def potentialOptions(n):
    p = []
    for r in range(9):
        p.append(optionRow(n,r))
    return p

def possibleGrid(n):
    p = potentialOptions(n)
    for r in range(9):
        for c in range(9):
            if n[r][c]==0 and len(p[r][c]) == 0:
                return False
    return p

def solveGrid(n):
    total = countZeros(n)
    v = possibleGrid(n)
    if v == False:
        return False
    while total>0:
        found = False
        for r in range(9):
            for c in range(9):
                if len(v[r][c]) == 1 and n[r][c] == 0:
                    a = v[r][c][0]
                    n[r][c] = a
                    for x in range(9):
                        d = v[r][x]
                        if a in d:
                            d.remove(a)
                            v[r][x] = d
                    for x in range(9):
                        d = v[x][c]
                        if a in d:
                            d.remove(a)
                            v[x][c] = d
                    tr = r-r%3
                    lc = c-c%3
                    for x in range(3):
                        for y in range(3):
                            d = v[tr+x][lc+y]
                            if a in d:
                                d.remove(a)
                                v[tr+x][lc+y] = d
                    v[r][c] = []
                    found = True
                    break
            if found:
                break
        if not found:
            return n
        total-=1
    return n

def solveSudoku(n):
    possible = [n]
    maxZeros = countZeros(n)
    while(maxZeros>0):
        newPoss = []
        for x in possible:
            a = solveGrid(x)
            if a!=False:
                zeroR = -1
                zeroC = -1
                for r in range(9):
                    for c in range(9):
                        if a[r][c]==0:
                            zeroR = r
                            zeroC = c
                if zeroR>-1:
                    v = optionCell(a, zeroR, zeroC)
                    for z in v:
                        temp = copyArray(a)
                        temp[zeroR][zeroC] = z
                        newPoss.append(temp)
                else:
                    return a
        possible = newPoss
        if len(possible)==0:
            return False
        for z in possible:
            v3 = countZeros(z)
            if v3==0:
                return z
            if v3>maxZeros:
                maxZeros = 3
    return possible[0]

def isCorrectGrid(myGrid):
    for r in range(9):
        theRow = []
        for x in myGrid:
            if x==0 or x in theRow:
                return False
            else:
                theRow.append(x)
    for c in range(9):
        theCol = []
        for r in range(9):
            x = myGrid[r][c]
            if x==0 or x in theCol:
                return False
            else:
                theCol.append(x)
    for tr in range(0,9,3):
        for lc in range(0,9,3):
            theSquare = []
            for a in range(3):
                for b in range(3):
                    x = myGrid[tr+a][lc+b]
                    if x==0 or x in theSquare:
                        return False
                    else:
                        theSquare.append(x)
    return True

def projectEulerProblemNinetySix(n):
    l = len(n)
    total = 0
    for x in range(0,l,9):
        grid = n[x:x+9]
        a = solveSudoku(grid)
        if a==False or not isCorrectGrid(a):
            print False
        else:
            total+=100*a[0][0]+10*a[0][1]+a[0][2]
    return total
'''
sampleGrid = [[1, 0, 0, 9, 2, 0, 0, 0, 0],
              [5, 2, 4, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 7, 0], 
              [0, 5, 0, 0, 0, 8, 1, 0, 2], 
              [0, 0, 0, 0, 0, 0, 0, 0, 0], 
              [4, 0, 2, 7, 0, 0, 0, 9, 0], 
              [0, 6, 0, 0, 0, 0, 0, 0, 0], 
              [0, 0, 0, 0, 3, 0, 9, 4, 5], 
              [0, 0, 0, 0, 7, 1, 0, 0, 6]]

answer = solveSudoku(sampleGrid)
for x in answer:
    print x
'''

start = time.time()
print projectEulerProblemNinetySix(realContents)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

24702
--- 2.47313904762 seconds ---

for input of given list of Sudoku Grids.
'''