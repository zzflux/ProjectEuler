#Project Euler problem #315
#Digital root clocks
#by Jon McMahon

from copy import deepcopy
import DivisibilityTools as dv

DIGITS = [[1, 1, 1, 1, 1, 1, 0], #digit 0
          [0, 0, 1, 1, 0, 0, 0], #digit 1
          [0, 1, 1, 0, 1, 1, 1], #digit 2
          [0, 1, 1, 1, 1, 0, 1], #digit 3
          [1, 0, 1, 1, 0, 0, 1], #digit 4
          [1, 1, 0, 1, 1, 0, 1], #digit 5
          [1, 1, 0, 1, 1, 1, 1], #digit 6
          [1, 1, 1, 1, 0, 0, 0], #digit 7
          [1, 1, 1, 1, 1, 1, 1], #digit 8
          [1, 1, 1, 1, 1, 0, 1]] #digit 9
ALL_OFF = [0] * 7

def digitRoot(x):
    return sum(int(d) for d in str(x))

def rootSequence(starting):
    current = starting
    while current >= 10:
        yield current
        current = digitRoot(current)
    yield current

def calcDiff(state1, state2):
    #print('Getting diff between', state1, 'and', state2)
    return sum(x != y for x,y in zip(state1, state2))

def calcTotalDiffs(states1, states2):
    #print('---')
    return sum(calcDiff(a, b) for a,b in zip(states1, states2))

def intToDigits(i, length):
    state = [[0 for c in range(7)] for r in range(length)]
    ctr = 0
    for d in str(i)[::-1]:
        state[ctr] = DIGITS[int(d)]
        ctr += 1
    return state[::-1]
    

def clock(starting, permLastState = False):
    totalTransitions = 0
    lastState = [[0 for _ in range(7)] for _ in range(len(str(starting)))]
    lastdisp = 0
    for disp in rootSequence(starting):
        lastdisp = disp
        nextState = intToDigits(disp, len(str(starting)))
        if permLastState:
            totalTransitions += 2 * calcTotalDiffs(nextState, lastState)
        else:
            totalTransitions += calcTotalDiffs(nextState, lastState)
            lastState = deepcopy(nextState)
    if not permLastState:
        totalTransitions += calcTotalDiffs([[0 for _ in range(7)] for _ in range(len(str(starting)))], intToDigits(lastdisp, len(str(starting))))
    return totalTransitions

if __name__ == '__main__':
    print('Answer:', sum(clock(t, True) - clock(t, False) for t in dv.primeGeneratorLessThan(2 * 10 ** 7) if t > 10 ** 7))
        
            
    
