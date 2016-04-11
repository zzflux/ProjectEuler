#Project Euler problem #329
#Prime frog
#Status: solved

import DivisibilityTools
from fractions import Fraction

mode = "Run"

UPPER = 500
CROAKSEQ = "PPPPNNPPPNPPNPN"
twoThirds = Fraction(2,3)
oneHalf = Fraction(1,2)
oneThird = Fraction(1,3)
oneFivehundredth = Fraction(1,500)

def probMatch(pPrimeCroak, desiredCroakSeq, init, minimum, maximum):
    if len(desiredCroakSeq) == 0:
        return 1
    if init > maximum or init < minimum:
        return 0
    if init == maximum:
        nextPos = [init - 1]
    elif init == minimum:
        nextPos = [init + 1]
    else:
        nextPos = [init - 1, init + 1]
    if desiredCroakSeq[0]:
        return sum([pPrimeCroak[init] * probMatch(pPrimeCroak, desiredCroakSeq[1:], pos, minimum, maximum) * Fraction(1,len(nextPos)) for pos in nextPos])
    else:
        return sum([(1-pPrimeCroak[init]) * probMatch(pPrimeCroak, desiredCroakSeq[1:], pos, minimum, maximum) * Fraction(1,len(nextPos)) for pos in nextPos])

if __name__ == "__main__" and mode == "Run":
    print("Working...")
    primes = DivisibilityTools.primeListLessThan(UPPER + 1)
    primalityMatrix = [n in primes for n in range(UPPER + 1)]
    probPrimeCroak = [twoThirds if p else oneThird for p in primalityMatrix]
    primeCroakDesired = [True if x == "P" else False for x in CROAKSEQ]

    testList = [probMatch(probPrimeCroak, [True], x, 1, UPPER) for x in range(UPPER + 1)]
    if testList[1:] == probPrimeCroak[1:]:
        print("Self test passed")
    else:
        print("Self test FAILED")
        print("test list length:", len(testList))
        print("known list length:", len(probPrimeCroak))

    answer = Fraction(0,1)
    fract = Fraction(1,UPPER)
    for x in range(1, UPPER + 1):
        print("Trying start at", x)
        answer += probMatch(probPrimeCroak, primeCroakDesired, x, 1, UPPER) * fract
    print("Answer:", str(answer))
    
#done
