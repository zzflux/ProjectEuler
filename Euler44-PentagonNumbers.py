#Project Euler problem #44
#Pentagon numbers
#Jon McMahon, April 2016
#Unsolved

import itertools

def pentagonGenerator(count = None):
    if count:
        if count >= 1:
            nvals = range(1, count + 1)
        else:
            raise ValueError()
    else:
        nvals = itertools.count(start = 1)
    for n in nvals:
        yield n * (3 * n - 1)//2

def getPentagon(n):
    return n * (3 * n - 1)//2

def isPentagon(num, inlist = set(), maximum = 0, pg = pentagonGenerator()):
    while num > maximum:
        maximum = next(pg)
        inlist.update((maximum,))
    return num in inlist

if __name__ == '__main__':
    for difference in pentagonGenerator():
        print('Trying difference of', difference)
        for smallerIndex in itertools.count(start = 1):
            smaller = getPentagon(smallerIndex)
            #print('Smaller:', smaller, 'larger:', smaller + difference)
            #print('Checking', smaller + difference, 'and', smaller + difference + smaller)
            if isPentagon(smaller + difference) and isPentagon(smaller + difference + smaller):
                print('Answer:', difference)
                exit(0)
            if getPentagon(smallerIndex + 1) - smaller > difference:
                break
    

