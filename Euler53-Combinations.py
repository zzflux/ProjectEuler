#Project Euler problem #53
#Combinatoric selections
#Status: solved

import GeneralTools

def factorial(x):
    return GeneralTools.product(range(x, 1, -1))

def nCr(n, r):
    return factorial(n)//(factorial(r)*factorial(n-r))

if __name__ == "__main__":
    print("Answer:", sum(nCr(n,r) > 10 ** 6 for n in range(1, 100 + 1) for r in range(1, n + 1)))
    
                
#done
