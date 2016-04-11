#Project Euler problem #38
#Pandigital multiples
#Status: solved

def setIsPandigital(lst, digits = '123456789'):
    used = [False] * len(str(digits))
    for n in lst:
        for d in str(n):
            index = str(digits).find(d)
            if index == -1 or used[index]:
                return False
            used[index] = True
    return all(used)

if __name__ == "__main__":
    print("working...")
    already = []
    for s in range(10 ** 4):
        cur = ''
        n = 1
        while len(cur) < 9:
            cur += str(s * n)
            n += 1
            if setIsPandigital([cur]):
                already.append(int(cur))
            
    print("Answer:", max(already))

#done
