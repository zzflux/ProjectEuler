#Project Euler problem #74
#Digit factorial chains
#Jon McMahon

import GeneralTools as gt

FACTORIALS = [gt.factorial(x) for x in range(10)]

digitFactorial = lambda x: sum(FACTORIALS[int(n)] for n in str(x))

MINIMUM = 1
MAXIMUM = 10 ** 6 - 1
TARGET_CHAIN = 60


if __name__ == '__main__':
    ctr = 0
    for start in range(MINIMUM, MAXIMUM + 1):
        already = set((start,))
        current = digitFactorial(start)
        while current not in already:
            already.add(current)
            current = digitFactorial(current)
            #if len(already) > TARGET_CHAIN:
            #    break
        if len(already) == TARGET_CHAIN:
            ctr += 1
    print('Answer:', ctr)
    
        
