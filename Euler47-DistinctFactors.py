#Project Euler problem #47
#Distinct prime factors
#Status: solved

TGT_NUM = 4

def primeFactorize(x, ls = None):
    if ls == None:
        lst = []
    else:
        lst = ls
    for i in range(2, x):
        if x % i == 0:
            primeFactorize(i, lst)
            primeFactorize(x // i, lst)
            return lst
    lst.append(x)
    return lst


def countUniques(lst):
    return len([lst[i] for i in range(len(lst)) if lst[i] not in [lst[x] for x in range(len(lst)) if x != i]])

def countDistinct(lst):
    ctr = 0
    already = []
    for x in lst:
        if not x in already:
            already.append(x)
            ctr += 1
    return ctr

if __name__ == "__main__":
    cand = 2
    consec = 0
    while not consec == TGT_NUM:
        if not countDistinct(primeFactorize(cand)) >= TGT_NUM:
            consec = 0
        else:
            consec += 1
        cand += 1
    print("Series:", list(range(cand - 1, cand - 1 - consec, -1))[::-1])
    
    
#done
