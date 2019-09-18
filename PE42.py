'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #42
'''

import time

f = open("PE42Words.txt", "r")

if(f.mode == "r"):
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(x.split(","))
else:
    raise ValueError("Cannot read from file")

finalList = realContents[0]

def getValueString(myString):
    total = 0
    
    for x in myString:
        if("A"<=x<="Z"):
            total+=(ord(x)-ord("A")+1)

    return total

def projectEulerProblemFortyTwo(myList):
    totalsList = []
    maxTotal = 0
    for x in myList:
        a = getValueString(x)
        totalsList.append(a)
        if(a>maxTotal):
            maxTotal = a
    triangles = []
    c = 1
    while(c*(c+1)/2<=maxTotal):
        triangles.append(c*(c+1)/2)
        c+=1
    finalCount = 0
    for x in totalsList:
        if x in triangles:
            finalCount+=1
    return finalCount

start = time.time()
print projectEulerProblemFortyTwo(finalList)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

162
--- 0.00270199775696 seconds ---

for input of n = given list of words
'''