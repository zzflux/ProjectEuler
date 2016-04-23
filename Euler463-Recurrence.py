#Project Euler problem #463
#A weird recurrence relation
#Jon McMahon, April 2016
#Unsolved

def f(x):
    if x == 1 or x == 3:
        return x
    elif not x % 2:
        return f(x // 2)
    elif not ((x - 1) % 4):
        return 2 * f((x - 1) // 2 + 1) - f((x - 1) // 4)
    elif not ((x - 3) % 4):
        return 3 * f((x - 3) // 2 + 1) - 2 * f((x - 3) // 4)
    else:
        raise ValueError
    
if __name__ == '__main__':
    #for n in range(1, 9):
    #    print('f of', n, ' =', f(n))
    print('S(2 ^ 20) =', sum(f(n) for n in range(1, 2 ** 20 + 1)))
