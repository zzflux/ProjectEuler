#Project Euler problem #387
#Harshad numbers
#Status: solved

import DivisibilityTools
import math

NONZERO_DIGITS = "123456789"
ALL_DIGITS = "0" + NONZERO_DIGITS

def sumDigits(i):
    return sum([int(x) for x in str(i)])

def isHarshad(i):
    return i % sumDigits(i) == 0

def isStrongHarshad(i, primeCheckList):
    return isHarshad(i) and DivisibilityTools.primeCheckWithList(i // sumDigits(i), primeCheckList)

def rtHarshadsToLength(length, existingNum = 0):
    ngList = []
    if existingNum:
        digitbase = ALL_DIGITS
    else:
        digitbase = NONZERO_DIGITS
    for d in digitbase:
        if isHarshad(10 * existingNum + int(d)):
            ngList.append(10 * existingNum + int(d))
    if len(ngList) == 0:
        return
    yield from ngList
    if(len(str(ngList[0]))) >= length:
        return
    for x in ngList:
        yield from rtHarshadsToLength(length, x)

def strongRTHarshadsToLength(length, primeList):
    return [x for x in list(rtHarshadsToLength(length)) if isStrongHarshad(x, primeList)]

def constructPrimes(lst, primeCheckList, maximum):
    for x in lst:
        for d in ALL_DIGITS:
            cp = 10 * x + int(d)
            if cp < maximum:
                if DivisibilityTools.primeCheckWithList(cp, primeCheckList):
                    yield cp

TEN_POWER = 14

if __name__ == "__main__":
    print("Calculating primes...", end='')
    pcl = DivisibilityTools.primeListLessThan(int(math.sqrt(10 ** TEN_POWER)) + 10)
    print("done")
    print("Calculating Harshads...", end='')
    sth = strongRTHarshadsToLength(TEN_POWER, pcl)
    print("Harshads: ", sth)
    print("done")
    print("Calculating answer...", end='')
    answerNumbers = list(constructPrimes(sth, pcl, 10 ** TEN_POWER))
    print("done")
    print("Answer:", sum(answerNumbers))

#done
