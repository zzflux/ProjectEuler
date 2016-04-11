#General tools
#Written by Jon McMahon
#December 22, 2015

def product(it):
    p = 1
    for x in it:
        p *= x
    return p

def factorial(n):
    return product(range(1, n+1))
