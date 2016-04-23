#Project Euler problem #187
#Semiprimes
#Jon McMahon, April 2016
#Solved

PRIME_FILENAME = 'FirstTenMillionPrimes.txt'
MAX = 10 ** 8

if __name__ == '__main__':
    ctr = 0
    print('Loading primes...', end='')
    primes = [int(x) for x in open(PRIME_FILENAME) if int(x) < MAX // 2]
    print('done')
    for firstIndex in range(len(primes)):
        for secondIndex in range(firstIndex, len(primes)):
            prod = primes[firstIndex] * primes[secondIndex]
            if prod < MAX:
                ctr += 1
            else:
                break
    print('Answer:', ctr)
