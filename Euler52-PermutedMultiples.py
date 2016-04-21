#Poject Euler problem #52
#Permuted multiples
#Jon McMahon, April 2016
#Solved

import itertools
import string

EVERY = 10000

def digitsIsPermutation(sx, sy):
    return all(sx.count(d) == sy.count(d) for d in string.digits)

def main():
    for digits in itertools.count(start = 1):
        #print('Trying', digits, 'digit numbers')
        for x in range(int('1' + '0' * (digits - 1)), int('1' + '6' * (digits -1)) + 1):
            if all(digitsIsPermutation(str(m * x), str(x)) for m in range(2,7)):
                print('Answer:', x)
                return 0

if __name__ == '__main__':
    main()
