#Project Euler problem #66
#Diophantine equation
#Jon McMahon, April 2016
#Unsolved

import math

Y_CAP = int(1e6)
MAX_D = 1000

def isInt(x):
    return x == int(x)

def diophantineMinX(D):
    if isInt(math.sqrt(D)):
        return float('-inf')
    else:
        try:
            return min(math.sqrt(D * y ** 2 + 1) for y in range(1, Y_CAP) if isInt(math.sqrt(D * y ** 2 + 1)))
        except ValueError:
            return float('-inf')
        
def main():
    print('Answer:', max(((d, diophantineMinX(d)) for d in range(MAX_D + 1)), key = lambda x: x[1])[0])

    
if __name__ == '__main__':
    main()
