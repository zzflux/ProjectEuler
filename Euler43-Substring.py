#Project Euler problem #43
#Substring divisibility
#Jon McMahon 2016

import itertools as itools

INDICES = ((2,3,4), (3,4,5), (4,5,6), (5,6,7), (6,7,8), (7,8,9), (8,9,10))
DIVISORS = (2,3,5,7,11,13,17)
DIGITS = '0123456789'


def checkNumber(s):
    for ssi, div in zip(INDICES, DIVISORS):
        st = ''.join(s[i-1] for i in ssi)
        if int(st) % div:
            #print(st, 'not divisible by', div)
            return False
    return True

if __name__ == '__main__':
    print('Answer:', sum(int(''.join(p)) for p in itools.permutations(DIGITS) if checkNumber(''.join(p))))                       
