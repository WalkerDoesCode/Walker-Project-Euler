'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #68
'''

import time

def subset(myList,n):
    if(n == 0):
        return [[]]
    l = len(myList)
    if(n>l):
        return []
    a = myList[0]
    b = subset(myList[1:],n)
    c = subset(myList[1:],n-1)
    for x in c:
        t = x[:]
        t.append(a)
        t = sorted(t)
        b.append(t)
    return b

def complement(a,b):
    c = []
    for x in a:
        if x not in b:
            c.append(x)
    return c

def permutations(myList):
    l = len(myList)
    if(l==1):
        return [myList]
    a = myList[0]
    b = permutations(myList[1:])
    total = []
    for x in b:
        for z in range(l):
            t = x[0:z]
            t.append(a)
            t.extend(x[z:])
            total.append(t)
    return total

def projectEulerProblemSixtyEight():
    maxFound = -1
    digits = [1,2,3,4,5,6,7,8,9]
    arrangements = subset(digits,4)
    for x in arrangements:
        t = 0
        for y in x:
            t+=y
        if(t%5==0):
            theSum = (100-t)/5
            
            a = sorted(x)
            c = complement(digits,x)
            d = permutations(c)
            e = a
            e.append(10)
            for w in d:
                v = []
                for z in range(5):
                    temp = theSum-(w[z]+w[(z+1)%5])
                    v.append(temp)
                v = sorted(v)
                possible = True
                for f in range(5):
                    if(v[f]!=e[f]):
                        possible = False
                        break
                if(possible):
                    s = ""
                    s+=str(e[0])
                    for a in range(5):
                        if(w[a]+w[(a+1)%5] == theSum - e[0]):
                            break
                    s+=str(w[a])+str(w[(a+1)%5])
                    for b in range(1,5):
                        temp = theSum-(w[(a+b)%5]+w[(a+b+1)%5])
                        s+=str(temp)
                        s+=str(w[(a+b)%5])
                        s+=str(w[(a+b+1)%5])
                    if(int(s)>maxFound):
                        maxFound = int(s)
    return str(maxFound)

start = time.time()
print projectEulerProblemSixtyEight()
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

6531031914842725
--- 0.0102789402008 seconds ---

for given puzzle.
'''