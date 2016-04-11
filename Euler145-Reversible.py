#Project Euler problem #145
#How many reversible numbers are there below one-billion?
#Status: solved

ODD_DIGITS = set('13579')
MAX = 10 ** 9

def allOddDigits(n):
    return all(d in ODD_DIGITS for d in str(n))

def reverse(num):
    return int(str(num)[::-1])

if __name__ == "__main__":
    print("Answer:", sum(x % 10 and allOddDigits(x + reverse(x)) for x in range(1, MAX)), "reversible numbers less than", MAX)

#done
