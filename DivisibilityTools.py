#Divisibility Toolkit
#Written by Jon McMahon
#12/20/2015

#Generator for prime numbers strictly less than top (unbounded if no top given)
def primeGeneratorLessThan(top = None):
    if top != None and top <= 2:
        return
    primes = [2]
    yield 2
    current = 3
    while top == None or current < top:
        notPrime = False
        for d in primes:
            if d * d > current:
                break
            elif current % d != 0:
                continue
            else:
                notPrime = True
                break
        if not notPrime:
            yield current
            if not top or not current * current > top:
                primes.append(current)
        current += 2

def primeGeneratorLength(length):
    gen = primeGeneratorLessThan()
    for ctr in range(length):
        yield next(gen)
        
def primeListLessThan(n):
    return list(primeGeneratorLessThan(n))

def primeListLength(length):
    return list(primeGeneratorLength(length))

def primeListWithDigits(n):
    lst = []
    for p in primeGeneratorLessThan(10 ** n):
        if p >= 10 ** (n - 1):
            lst.append(p)
    return lst

def primeCheckWithList(num, primeList):
    if num <= 1:
        return False
    if num == 2:
        return True
    if not primeList[-1] ** 2 > num:
        raise ValueError("Insufficiently large prime checklist")
    for d in primeList:
        if num % d == 0:
            return False
        if d * d > num:
            return True

def primeCheck(x):
     if x == 2:
          return True
     elif x % 2 == 0:
          return False
     else:
          d = 3
          while d * d <= x:
                if x % d == 0:
                    return False
                d += 2
     return True
