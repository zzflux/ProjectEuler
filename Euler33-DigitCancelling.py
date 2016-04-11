#Project Euler problem #33
#Digit cancelling fractions

import fractions as frac

#constants
DIGITS = 2
#end constants

def cancelDigits(n1, n2):
    initlen = len(str(n1))
    s1 = str(n1)
    s2 = str(n2)
    for i in range(len(s1) - 1, -1, -1):
        if i < len(s1) and s1[i] in s2:
            i2 = s2.index(s1[i])
            s1 = s1[:i] + s1[i+1:]
            s2 = s2[:i2] + s2[i2+1:]
    if initlen == len(s1) or n1 == n2:
        return (-1, 1)
    if len(s1) == 0:
        return (1,1)
    if int(s2) == 0:
        return (1,1)
    else:
        return (int(s1),int(s2))    

def main():
    product = frac.Fraction("1/1")
    for numer in range(10 ** (DIGITS - 1), 10 ** (DIGITS)):
        for denom in range(10 ** (DIGITS - 1), 10 ** (DIGITS)):
            #print("numer:", numer, "denom:", denom)
            if frac.Fraction(numer, denom) == frac.Fraction(*cancelDigits(numer, denom)) and numer % 10 and numer < denom:
                product *= frac.Fraction(numer, denom)
                print("Found", numer, denom)
    print("Answer:", product)

if __name__ == "__main__":
    main()
