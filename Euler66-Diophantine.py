#Project Euler problem #66
#Diophantine equation
#Jon McMahon, April 2016
#Unsolved

import math
import itertools

Y_CAP = int(1e6)
MAX_D = 1000
maxy = 0

def isInt(x):
    return x == int(x)

def diophantineMinX(D):
    flag = False
    global maxy
    print('D=', D)
    if isInt(math.sqrt(D)):
        return float('-inf')
    else:
        for y in itertools.count(start = 1):
            if y > maxy:
                maxy = y
                flag = True
            x = math.sqrt(D * y ** 2 + 1)
            if isInt(x):
                if flag:
                    print('Max y reached:', maxy)
                return int(x)
        
def main():
    print('Answer:', max(((d, diophantineMinX(d)) for d in range(MAX_D + 1)), key = lambda x: x[1])[0])

    
if __name__ == '__main__':
    main()
