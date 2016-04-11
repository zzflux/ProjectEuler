#Project Euler problem 51
#Prime digit replacements

import DivisibilityTools as dv
import itertools as it

#Constants
MAX_LENGTH = 10
FAMILY_SIZE = 6
#End constants


def positionMatches(lst1, lst2, mask = None):
    lst = []
    if len(lst1) != len(lst2):
        print("Can't match between", lst1, "and", lst2)
        raise ValueError
    for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
            if mask == None or index in mask:
                lst.append(index)
    return lst

def main():
    endarmed = False
    lowestfound = 10 ** (MAX_LENGTH + 1)
    for length in range(1, MAX_LENGTH + 1):
        print("Trying length", length)
        primesOfLength = dv.primeListWithDigits(length)
        combs, tmp = it.tee(it.combinations(primesOfLength, FAMILY_SIZE))
        print("Combinations:", list(tmp))
        for c in combs:
            mininlist = min(c)
            lastnum = next(combs)[0]
            currentmask = range(length)
            for n in c:
                currentmask = positionMatches(str(lastnum), str(n), currentmask)
            if currentmask:
                endarmed = True
                if mininlist < lowestfound:
                    lowestfound = mininlist
        if endarmed:
            break
    print("Answer:", lowestfound)
                
    

if __name__ == "__main__":
    main()
