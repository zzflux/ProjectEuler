MIN_EXP = 1
MAX_EXP = 20

if __name__ == '__main__':
    for power in range(MIN_EXP, MAX_EXP + 1):
        line = "{"
        for n in range(0, 9):
            line += str(n ** power)
            line += ', '
        line += str(9 ** power)
        line += '},\n'
        print(line)
        
