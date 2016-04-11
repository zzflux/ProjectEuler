#Project Euler problem #89
#Roman Numerals
#by Jon McMahon

import sys

R_NUMERALS = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
R_NUMERALS_REV = dict(zip(R_NUMERALS.values(), R_NUMERALS.keys()))
R_NUMERALS_REV[4] = 'IV'
R_NUMERALS_REV[9] = 'IX'
R_NUMERALS_REV[40] = 'XL'
R_NUMERALS_REV[90] = 'XC'
R_NUMERALS_REV[400] = 'CD'
R_NUMERALS_REV[900] = 'CM'

def main():
    if len(sys.argv) <= 1:
        print('Error: need filename.')
        sys.exit(1)
    solver(sys.argv[1])


def solver(fn):
    print('Answer:', sum(len(line.strip()) - len(compactRn(line.strip())) for line in open(fn)))
               
def rnToInt(st):
    ctr = 0
    lastVal = float('inf')
    for c in st:
        if R_NUMERALS[c] <= lastVal:
            if lastVal != float('inf'):
                ctr += lastVal
        else:
            ctr -= lastVal
        lastVal = R_NUMERALS[c]
    ctr += lastVal
    return ctr

def intToRn(i):
    running = ''
    for v in sorted(R_NUMERALS_REV.keys(), reverse=True):
        go = True
        while go:
            go = False
            if i >= v:
                running += R_NUMERALS_REV[v]
                i -= v
                go = True
    return running

def compactRn(st):
    #print(st, '->', intToRn(rnToInt(st)))
    return intToRn(rnToInt(st))

if __name__ == '__main__':
    main()



