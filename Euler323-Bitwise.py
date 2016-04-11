#Project Euler problem #323
#Bitwise-OR operations on random integers
#Status: unsolved

import random

TRIALS = 10 ** 6
BITS = 7

MODE = 2

def func(n):
    return sum([(1-0.5**k)**BITS for k in range(n + 1)])

if __name__ == "__main__" and MODE == 2:
    for v in range(1, 10):
        print("f(", v, ") = ", func(v), sep='')

MODE = 1        

if __name__ == "__main__" and MODE == 1:
    random.seed()
    record = []
    for i in range(TRIALS):
        ctr = 0
        x = 0
        while x != 2 ** BITS - 1:
            x |= random.randint(0, 2 ** BITS - 1)
            ctr += 1
        record.append(ctr)
    print("Bits:", BITS)
    print("Trials:", TRIALS)
    print("Min:", min(record))
    print("Max:", max(record))
    print("Avg:", sum(record)/len(record))
