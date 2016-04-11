#Project Euler problem #27
#Digit factorials

import GeneralTools as gt

def factorial(n):
    return gt.product(range(1, n+1))

digitFactorials = [factorial(x) for x in range(10)]

def isSumOfFactorialDigits(n):
    #print('Testing', n)
    #if not n % 10000:
    #    print('Testing', n)
    return int(n) == sum(digitFactorials[int(d)] for d in str(n))

if __name__ == '__main__':
    maxdigits = 7
    print('Answer:', sum(a for a in range(3, 10 ** (maxdigits + 1)) if isSumOfFactorialDigits(a)))
    
