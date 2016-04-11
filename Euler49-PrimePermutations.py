#Project Euler problem #49
#Prime permutations
#Jon McMahon 2016

import DivisibilityTools as dtools
import itertools as itools
import math

DIGITS = 4
NUMS = 3
BLACKLIST = ((1487, 4817, 8147))

def checkProperty(nums, pList = None):
    #print('Checking', nums)
    comp = None
    for i, j in zip(range(len(nums) - 1), range(1,len(nums))):
        if comp == None:
            comp = nums[j] - nums[i]
            if comp <= 0:
                return False
        else:
            if nums[j] - nums[i] != comp:
                return False
    numsAsStrs = [str(n) for n in nums]
    perms = list(''.join(_) for _ in itools.permutations(numsAsStrs[0]))
    if not all(n in perms for n in numsAsStrs):
        return False
    if pList == None:
        for n in nums:
            if not dtools.primeCheck(n):
                return False
    else:
        if not all(dtools.primeCheckWithList(n, pList) for n in nums):
            return False
    return True
    
    
    
if __name__ == '__main__':
    wholePrimeList = dtools.primeListLessThan(math.sqrt(10 ** DIGITS)+1)
    primes = dtools.primeListWithDigits(DIGITS)
    for partperm in itools.permutations(primes, 2):
        #print('Partperm:', partperm)
        perm = partperm + (partperm[-1] - partperm[0],)
        if checkProperty(perm, wholePrimeList) and perm not in BLACKLIST:
            string = ''.join(str(i) for i in perm)
            print('Answer:', string)
            
