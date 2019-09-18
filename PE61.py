'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #61
'''

import time

def projectEulerProblemSixtyOne():
    triangles = []
    c = 2
    v = 1
    while(v<10000):
        if(v>=1000):
            triangles.append(v)
        v+=c
        c+=1
    squares = []
    c = 32
    v = c*c
    while(v<10000):
        squares.append(v)
        c+=1
        v += (2*c-1)
    pentagons = []
    c = 2
    v = 1
    while(v<10000):
        if(v>=1000):
            pentagons.append(v)
        v+=(3*c-2)
        c+=1
    hexagons = []
    c = 2
    v = 1
    while(v<10000):
        if(v>=1000):
            hexagons.append(v)
        v+=(4*c-3)
        c+=1
    heptagons = []
    c = 2
    v = 1
    while(v<10000):
        if(v>=1000):
            heptagons.append(v)
        v+=(5*c-4)
        c+=1
    octagons = []
    c = 2
    v = 1
    while(v<10000):
        if(v>=1000):
            octagons.append(v)
        v+=(6*c-5)
        c+=1
    total = triangles[:]
    for x in squares:
        if x not in total:
            total.append(x)
    for x in pentagons:
        if x not in total:
            total.append(x)
    for x in hexagons:
        if x not in total:
            total.append(x)
    for x in heptagons:
        if x not in total:
            total.append(x)
    for x in octagons:
        if x not in total:
            total.append(x)
    possibleTuples = []
    for o in octagons:
        a = o%100
        p1 = []
        for x in total:
            if(x/100==a):
                p1.append(x)
        for o1 in p1:
            b = o1%100
            p2 = []
            for x in total:
                if(x/100==b):
                    p2.append(x)
            for o2 in p2:
                c = o2%100
                p3 = []
                for x in total:
                    if(x/100==c):
                        p3.append(x)
                for o3 in p3:
                    d = o3%100
                    p4 = []
                    for x in total:
                        if(x/100==d):
                            p4.append(x)
                    for o4 in p4:
                        e = o4%100
                        p5 = []
                        for x in total:
                            if(x/100==e and x%100 == o/100):
                                p5.append(x)
                        for o5 in p5:
                            possibleTuples.append([o,o1,o2,o3,o4,o5])
    realPossible = []
    for a in possibleTuples:
        whole = []
        hpRep = False
        heRep = False
        peRep = False
        sqRep = False
        trRep = False
        repeat = False
        for x in a:
            if x not in whole:
                whole.append(x)
            else:
                repeat = True
                break
            if(x in hexagons):
                heRep = True
            elif(x in triangles):
                trRep = True
            elif(x in heptagons):
                hpRep = True
            elif(x in pentagons):
                peRep = True
            elif(x in squares):
                sqRep = True
        if(hpRep and heRep and peRep and sqRep and trRep and not repeat):
            realPossible.append(a)
    maxFound = -1
    for x in realPossible:
        t = 0
        for y in x:
            t+=y
        if(t>maxFound):
            maxFound = t
    return maxFound
    

start = time.time()
print projectEulerProblemSixtyOne()
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

28684
--- 0.0513989925385 seconds ---

for given problem.
'''