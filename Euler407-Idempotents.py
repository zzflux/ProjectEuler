#Project Euler problem #407
#Idempotents
#Jon McMahon, April 2016
#Unsolved

def maxidempotent(n):
    for x in range(n - 1, -1, -1):
        if pow(x, 2, n) == x:
            return x


    
if __name__ == '__main__':
    ctr = 0
    for n in range(1, 10 ** 7 + 1):
        ctr += maxidempotent(n)
        if not n % 1000:
            print('n =', n, '(', n/10**7 * 100, '%)')
    print('Answer:', ctr)
