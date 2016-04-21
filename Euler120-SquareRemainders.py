#Project Euler problem #120
#Square remainders
#Jon McMahon, April 2016
#Solved

def maximizer(a):
    return 2 * a * ((a - 1) // 2)

if __name__ == '__main__':
    print('Answer:', sum(maximizer(x) for x in range(3, 1001)))
