'''
Author: Walker Kroubalkian
Library Approach to Project Euler Problem #19
'''

import datetime
import time

def projectEulerProblemNineteen(m1, d1, y1, m2, d2, y2):
    start = datetime.datetime(y1, m1, d1)
    end = datetime.datetime(y2, m2, d2)
    day = datetime.timedelta(days = 1)
    week = datetime.timedelta(days = 7)
    while(start.weekday()!=6 and start<=end):
        start+=day
    
    total = 0
    while(start<=end):
        if start.day==1:
            total+=1
        start+=week
    return total

start = time.time()
print projectEulerProblemNineteen(1, 1, 1901, 12, 31, 2000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

171
--- 0.000821828842163 seconds ---

for input of start date = January 1, 1901, end date = December 31, 2000
'''