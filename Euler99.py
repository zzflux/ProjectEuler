#Project Euler problem #99
#Largest exponential
#Jon McMahon, March 2016

import math
import itertools

FILENAME = 'p099_base_exp.txt'
SEPAR = ','

def logLine(x):
    base, exponent = x.strip().split(SEPAR)
    return int(exponent) * math.log(int(base))

if __name__ == '__main__':
    data = [(n, l) for n,l in zip(itertools.count(start = 1), open(FILENAME))]
    linenum, _ = max(data, key = lambda x: logLine(x[1]))
    print('Answer:', linenum)
