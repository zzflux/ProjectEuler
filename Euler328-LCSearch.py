#Project Euler problem #328
#Lowest-cost Search

#caching idea: The patten for n items in the list applies to any list of n possibiities
#continued: simply check whether this size has occurred before


SAFE = 12

ALTMAX = 500 
REALMAX = 200000
EVERY = 200
MODE = 'for real'
SET_WITH_JUST_NEGATIVE_TWO = frozenset((-2,))

import random


def worstCaseCost(rmin, rmax, alreadyChecked = {}):
    rangelen =  rmax - rmin + 1
    if rangelen == 1:
        return 0
    if rangelen == 2:
        return rmin
    elif rangelen == 3:
        return (rmax + rmin) // 2
    else:
        if (rmin, rmax) in alreadyChecked:
            return alreadyChecked[(rmin, rmax)]
        else:
            toret = min(part + max(worstCaseCost(rmin, part - 1), worstCaseCost(part + 1, rmax)) for part in range(rmin + 1, rmax))
            alreadyChecked[(rmin, rmax)] = toret
            return toret


def worstCaseCostAndAnalysis(rmin, rmax, alreadyChecked = {}, alreadyChecked2 = {}):
    rangelen =  rmax - rmin + 1
    if rangelen == 1:
        return 0,-1
    if rangelen == 2:
        return rmin,-2
    elif rangelen == 3:
        return (rmax + rmin) // 2,-2
    else:
        if False:
            pass
        else:
            toret = min( ((part, part + max(worstCaseCost(rmin, part - 1), worstCaseCost(part + 1, rmax))) for part in range(rmin + 1, rmax)), key=lambda x:x[1])
            alreadyChecked[(rmin, rmax)] = toret[1]
            print('Range:', rmin, 'to', rmax, 'Length:', rangelen, 'Best value:', toret[0], 'Best index:', toret[0] - rmin, 'or', -1* (rangelen - (toret[0] - rmin)))
            return (toret[1], -1* (rangelen - (toret[0] - rmin)))            

def worstCaseCostOptimized(rmin, rmax, directCache = {}, secondaryCache = {}):
    #print('Optimized function called on', rmin, 'to', rmax)
    #print('DIAG: called on', rmin, 'to', rmax)
    rangelen = rmax - rmin + 1
    if rangelen < 0:
        raise ValueError('rmin must be less than or equal to rmax')
    elif rmax < 0 or rmin < 0:
        raise ValueError('rmin and rmax must not be negative')
    elif rangelen == 1 or rangelen == 0:
        #print('Optimized function returning for', rmin, 'to', rmax)
        return 0
    elif rangelen == 2:
        #print('Optimized function returning for', rmin, 'to', rmax)
        return rmin
    elif rangelen == 3:
        #print('Optimized function returning for', rmin, 'to', rmax)
        return rmax - 1
    elif rangelen == 4:
        #print('Optimized function returning for', rmin, 'to', rmax)
        return rmax - 1 + rmin
    else:
        if (rmin, rmax) in directCache:
            #print('Optimized function returning for', rmin, 'to', rmax)
            return directCache[(rmin, rmax)]
        else:
            negIndicesToTry = set()
            middle = rangelen//2
            minBestIndex = -1 * (middle - middle % 8)
            if rangelen in secondaryCache and secondaryCache[rangelen] <= rmin:
                #print('Secondary cache hit on range', rmin, 'to', rmax)
                negIndicesToTry.add(minBestIndex)
            else:
                negIndicesToTry.update(range(-8, minBestIndex - 1, -8))
                negIndicesToTry.update(range(-1, max(-rangelen, -9), -1))                
                #negIndicesToTry.update((-2, -4))
            nindex, answer = min(((i, rmax + i + 1 + max(worstCaseCostOptimized(rmin, rmax + 1 + i - 1), worstCaseCostOptimized(rmax +i + 1 + 1,rmax))) for i in negIndicesToTry), key = lambda x: int(x[1]))
            #print('ideal negindex:', nindex)            
            if (rangelen not in secondaryCache or rmin < secondaryCache[rangelen]) and (rangelen > 4) and (nindex == minBestIndex):
                secondaryCache[rangelen] = rmin
            if (rmin, rmax) not in directCache:
                pass                
                directCache[(rmin, rmax)] = answer
            #print('Optimized function returning for', rmin, 'to', rmax)
            return answer

def freqAnalyze(lst):
    ctr = 1
    outarr = []
    last = None
    for x in lst:
        if x == last:
            ctr += 1
        else:
            if last != None:
               outarr += [''.join((str(last), ' x ', str(ctr)))] 
            last = x
            ctr = 1
    return outarr
        

if __name__ == '__main__' and MODE == 'explore':
    negindices = set()
    for rlen in range(20,50):
        for minimum in range(1,200):
            worstCaseCostAndAnalysis(minimum, minimum + rlen - 1)
            
   

if __name__ == '__main__' and MODE == 'explore2':
    TOP = 100
    total = 0
    for x in range(1, TOP + 1): 
        ans = worstCaseCostOptimized(1, x)
        print('Worst case cost for 1 to', x, 'is', ans)
        total += ans
    print('Total:', total)
    print('Real total:', sum(worstCaseCost(1,x) for x in range(1, TOP + 1)))

if __name__ == '__main__' and MODE == 'testing':
    disagreements = []
    for x in range(1, 111):
        y = worstCaseCostOptimized(1,x)
        z = worstCaseCost(1,x)
        print('Optimized function: 1 to', x, 'is', y)
        print('Real answer: 1 to', x, 'is', z)
        if z != y:
            disagreements.append((x, y, z))
    print(disagreements)

if __name__ == '__main__' and MODE == 'testing2':
    print(worstCaseCostOptimized(1,52))
    input('waiting')


if __name__ == '__main__' and MODE == 'for real':
    total = 0
    for x in range(1, REALMAX + 1):
        total += worstCaseCostOptimized(1, x)
        if not x % EVERY:
            print('About', x / REALMAX * 100, '% done')
    print('Answer:', total)
    
    
if __name__ == '__main__' and MODE == 'almost for real':
    total = 0
    for x in range(1, ALTMAX + 1):
        total += worstCaseCostOptimized(1, x)
        if not x % EVERY:
            print('About', x / ALTMAX * 100, '% done')
    print('Answer:', total)
