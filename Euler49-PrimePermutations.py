#Project Euler problem #49
#Prime permutations
#Jon McMahon 2016

import DivisibilityTools as dtools
import itertools as itools
import math

DIGITS = 4
SEQ_LEN = 3
BLACKLIST = ((1487, 4817, 8147),)
PRIMELIST = dtools.primeListWithDigits(DIGITS)
PRIMESET = frozenset(PRIMELIST)
GREATEST_PRIME = max(PRIMELIST)
SMALLEST_PRIME = min(PRIMELIST)

def sequenceGenerator(prefix = None):
    #print('Called with prefix=', prefix)
    if not prefix:
        for p in PRIMELIST:
            for grp in sequenceGenerator((p,)):
                if len(grp) == SEQ_LEN:
                    yield grp
    elif len(prefix) == 1:
        #print('Set1:', set(int(''.join(_)) for _ in itools.permutations(str(prefix[-1]))))
        #print('Set2:', '*primes*')
        #print('Set3:', set(range(prefix[-1] + 1, GREATEST_PRIME + 1)))
        #print('Intersection:', sorted(set(int(''.join(_)) for _ in itools.permutations(str(prefix[-1]))) & PRIMESET & set(range(prefix[-1] + 1, GREATEST_PRIME + 1))))
        for nextprime in sorted(set(int(''.join(_)) for _ in itools.permutations(str(prefix[-1]))) & PRIMESET & set(range(prefix[-1] + 1, GREATEST_PRIME + 1))):
            #print('Supposedly calling on', prefix + (nextprime,))
            for g in sequenceGenerator(prefix + (nextprime,)):
                yield g
    elif len(prefix) == SEQ_LEN:
        yield prefix
    else:
        #print('Seq len:', len(prefix))
        np = 2 * prefix[-1] - prefix[0]
        if np in (PRIMESET & set(int(''.join(_)) for _ in itools.permutations(str(prefix[-1])))):
            for g in sequenceGenerator(prefix + (np,)):
                yield g
        else:
            #print('Impossible')
            pass
    
if __name__ == '__main__':
    for seq in sequenceGenerator():
        if not seq in BLACKLIST:
            print('Answer:', ''.join(str(_) for _ in seq))
    
            
