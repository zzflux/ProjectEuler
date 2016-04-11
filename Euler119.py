#Project Euler problem #119
#Digit power sum
#Jon McMahon, March 2016

import itertools

HOWMANY = 30

def equalsSumOfDigitsToPower(number):
    if len(str(number)) < 2:
        return False
    else:
        digitsum = sum(int(digit) for digit in str(number))
        if digitsum == 0 or digitsum == 1:
            return False
        power = 0
        last = 0
        while number > last:
            last = digitsum ** power
            power += 1
            if last == number:
                return True
        return False

def numbersThatPass(test, start = 0, step = 1):
    for x in itertools.count(start = start, step = step):
        #print('Testing', x)
        if test(x):
            yield x

if __name__ == '__main__':
    ctr = 0
    gener = numbersThatPass(equalsSumOfDigitsToPower)
    while ctr < HOWMANY:
        ctr += 1
        print('#', ctr, 'is', next(gener))
    
