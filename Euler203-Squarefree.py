#Project Euler problem #203
#Squarefree binomial coefficients
#Jon McMahon, April 2016
#Solved

import DivisibilityTools as dt
import GeneralTools as gt
import math

HIGHEST_ROW = 51

def isSquarefree(x):
    return all(x % (d ** 2) for d in dt.primeGeneratorLessThan(int(math.sqrt(x + 1) + 1)))

def pascalsTriangleRow(n):
    nfact = gt.factorial(n)
    for k in range(n + 1):
        yield nfact // (gt.factorial(n - k) * gt.factorial(k))

def main():
    distinct = set()
    for row in range(51):
        #print('row', row)
        for x in pascalsTriangleRow(row):
            if isSquarefree(x):
                distinct.add(x)
    print('Answer:', sum(distinct))



if __name__ == '__main__':
    main()
