'''
Author: Project Euler (with Python 2.7 implementation by Walker Kroubalkian)
Very Dynamic Approach to Project Euler Problem #31
'''

import time

def projectEulerProblemThirtyOne(coins, amount):
    ways = [0]*(amount+1)
    ways[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], amount+1):
            ways[j] = ways[j] + ways[j-coins[i]]
    return ways[amount]

start = time.time()
print projectEulerProblemThirtyOne([1, 2, 5, 10, 20, 50, 100, 200], 200)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

73682
--- 7.15255737305e-06 seconds ---

for input of n=200, currency = [1,2,5,10,20,50,100,200]
'''